"""Runs the ngspice netlists with several parameter sets and writes the plots to docs/img/.

Usage: python3 sim/plot.py   (ngspice, numpy and matplotlib are required)
"""

import re
import subprocess
import tempfile
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

SIM = Path(__file__).resolve().parent
IMG = SIM.parent / "docs" / "img"
IMG.mkdir(parents=True, exist_ok=True)


def run(netlist: str, params: dict) -> np.ndarray:
    text = (SIM / netlist).read_text()
    for name, value in params.items():
        text, n = re.subn(rf"^\.param {name}=.*$", f".param {name}={value}", text, flags=re.M)
        if n != 1:
            raise KeyError(f"{name} not found in {netlist}")
    with tempfile.TemporaryDirectory() as tmp:
        out = Path(tmp) / "out.txt"
        text = re.sub(r"wrdata \S+", f"wrdata {out}", text)
        cir = Path(tmp) / "run.cir"
        cir.write_text(text)
        subprocess.run(["ngspice", "-b", str(cir)], check=True, capture_output=True)
        return np.loadtxt(out, skiprows=1)


def db(x):
    return 20 * np.log10(np.abs(x))


def lp2(f, fc, q):
    s = 1j * f / fc
    return 1 / (s**2 + s / q + 1)


def hp2(f, fc, q):
    s = 1j * f / fc
    return s**2 / (s**2 + s / q + 1)


# ---------------------------------------------------------------- crossover
def crossover():
    data = {pad: run("crossover.cir", {"pad": pad}) for pad in (0, 1)}
    f = data[0][:, 0]
    ztot = data[0][:, 1] + 1j * data[0][:, 2]

    # Approximate acoustic models (minimum phase): the Seventy 80 rolls off
    # above ~4.5 kHz, the HT-30 horn below ~2.5 kHz and above ~16 kHz.
    woofer = 10 ** (99 / 20) * hp2(f, 80, 0.8) * lp2(f, 4500, 0.9)

    fig, ax = plt.subplots(3, 1, figsize=(9, 11))
    ax[0].semilogx(f, db(woofer), "k--", label="Seventy 80 (közelítő)")
    summary = {}
    for pad, d in data.items():
        vtw = d[:, 3] + 1j * d[:, 4]
        tw = 10 ** (98 / 20) * (vtw / 2.83) * hp2(f, 2500, 0.9) * lp2(f, 16000, 0.7)
        label = "0 dB pad" if pad == 0 else "-3 dB pad"
        ax[0].semilogx(f, db(tw), label=f"HT-30, {label}")
        for pol in (1, -1):
            total = woofer + pol * tw
            name = "normál" if pol == 1 else "fordított"
            ax[0].semilogx(f, db(total), lw=2 if pol == 1 else 1,
                           label=f"Összeg, {label}, {name} polaritás")
            band = (f > 2000) & (f < 12000)
            summary[(pad, pol)] = (db(total[band]).min(), db(total[band]).max())
        itw = np.abs(d[:, 5] + 1j * d[:, 6]) * 25.3 / 2.83
        ax[2].semilogx(f, itw, label=f"Tweeter-áram 80 W-nál, {label}")
    ax[0].set_ylim(80, 110)
    ax[0].set_title("Becsült hangnyomás 2,83 V / 1 m (közelítő modell)")
    ax[0].set_ylabel("dB SPL")

    ax[1].semilogx(f, np.abs(ztot), label="Teljes terhelés (0 dB pad)")
    ax[1].axhline(4, color="r", ls=":", label="4 Ω határ")
    ax[1].set_ylabel("|Z| [Ω]")
    ax[1].set_title("Az erősítő által látott impedancia")
    ax[1].set_ylim(0, 40)

    ax[2].axhline(1.35, color="r", ls=":", label="PTC tartóáram 1,35 A")
    ax[2].set_ylabel("A (szinusz, 25,3 V RMS)")
    ax[2].set_title("Tweeter-ág árama teljes kimeneti feszültségnél")
    for a in ax:
        a.grid(True, which="both", alpha=0.3)
        a.set_xlabel("Hz")
        a.legend(fontsize=7)
    fig.tight_layout()
    fig.savefig(IMG / "keresztvalto.png", dpi=110)

    fc_idx = np.argmin(np.abs(db(data[0][:, 3] + 1j * data[0][:, 4]) - (db(2.83) - 3)))
    print(f"Tweeter -3 dB (elektromos): {f[fc_idx]:.0f} Hz")
    print(f"Minimális impedancia: {np.abs(ztot).min():.2f} ohm @ {f[np.argmin(np.abs(ztot))]:.0f} Hz")
    for (pad, pol), (lo, hi) in summary.items():
        print(f"pad={pad} pol={pol:+d}: 2-12 kHz sáv {lo:.1f} .. {hi:.1f} dB")


# ---------------------------------------------------------------- preamp
def preamp():
    def resp(**p):
        d = run("preamp.cir", p)
        return d[:, 0], db(d[:, 1] + 1j * d[:, 2])

    fig, ax = plt.subplots(2, 2, figsize=(12, 8))
    for g in (0, 0.5, 1):
        f, h = resp(gain=g)
        ax[0, 0].semilogx(f, h, label=f"gain = {g}")
    f, h = resp(lowcut=0)
    ax[0, 0].semilogx(f, h, "--", label="gain = 0, low-cut kiiktatva")
    ax[0, 0].set_title("Erősítés és 80 Hz-es low-cut")

    for b in (0, 0.25, 0.5, 0.75, 1):
        f, h = resp(bass=b)
        ax[0, 1].semilogx(f, h, label=f"bass = {b}")
    ax[0, 1].set_title("Basszus szabályzó")

    for t in (0, 0.25, 0.5, 0.75, 1):
        f, h = resp(treb=t)
        ax[1, 0].semilogx(f, h, label=f"treble = {t}")
    ax[1, 0].set_title("Magas szabályzó")

    for p in (0, 0.5, 1):
        f, h = resp(pres=p)
        ax[1, 1].semilogx(f, h, label=f"presence = {p}")
        peak = np.argmax(h)
        print(f"presence={p}: csúcs {h[peak]:.1f} dB @ {f[peak]:.0f} Hz")
    ax[1, 1].set_title("Presence (a 4-5 kHz-es rés pótlása)")

    for a in ax.flat:
        a.grid(True, which="both", alpha=0.3)
        a.set_xlabel("Hz")
        a.set_ylabel("dB")
        a.legend(fontsize=7)
    fig.tight_layout()
    fig.savefig(IMG / "eloerosito.png", dpi=110)

    for b in (0, 1):
        f, h = resp(bass=b)
        print(f"bass={b}: 50 Hz {h[np.argmin(abs(f-50))]:.1f} dB, 100 Hz {h[np.argmin(abs(f-100))]:.1f} dB")
    for t in (0, 1):
        f, h = resp(treb=t)
        print(f"treb={t}: 10 kHz {h[np.argmin(abs(f-10000))]:.1f} dB")
    for g in (0, 1):
        f, h = resp(gain=g)
        print(f"gain={g}: 1 kHz {h[np.argmin(abs(f-1000))]:.1f} dB")


if __name__ == "__main__":
    crossover()
    preamp()

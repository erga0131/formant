import numpy as np
import sounddevice as sd

fs = 44100
f0=1000
d = 1

t = np.linspace(0, d, d * fs, endpoint=False)
x = np.sin(2 * np.pi * f0 * t)

sd.play(x, fs)
sd.wait()
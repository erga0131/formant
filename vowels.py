import numpy as np
import sounddevice as sd

text = "あいうえお"

fs = 44100
d = 0.5
t = np.linspace(0, d, int(d * fs), endpoint=False)

# 母音ごとの周波数と振幅の設定
vowel_params = {
    "あ": {
        "F0": 300,
        "freq": [300, 600, 900, 1200, 1500],
        "amp":  [0.40, 0.15, 0.35, 0.30, 0.10]
    },
    "い": {
        "F0": 300,
        "freq": [300, 600, 3000, 3300, 3300],
        "amp":  [0.52, 0.03, 0.02, 0.02, 0.01]
    },
    "う": {
        "F0": 300,
        "freq": [300, 600, 1200, 1500, 1800],
        "amp":  [0.32, 0.11, 0.02, 0.02, 0.01]
    },
    "え": {
        "F0": 300,
        "freq": [300, 600, 900, 1800, 2100, 2400],
        "amp":  [0.20, 0.45, 0.10, 0.15, 0.03, 0.01]
    },
    "お": {
        "F0": 300,
        "freq": [300, 600, 900, 1200],
        "amp":  [0.35, 0.30, 0.25, 0.10]
    }
}

x_total = np.array([])

for char in text:
    freq = vowel_params[char]["freq"]
    x = sum([vowel_params[char]["amp"][i] * np.sin(2 * np.pi * freq[i] * t) for i in range(len(freq))])
    x_total = np.concatenate((x_total, x))

sd.play(x_total, fs)
sd.wait()

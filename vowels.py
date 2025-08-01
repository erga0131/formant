import numpy as np
import sounddevice as sd

text = "あいうえお"

fs = 44100
d = 0.5
t = np.linspace(0, d, int(d * fs), endpoint=False)
freq=300

# 母音ごとの周波数と振幅の設定

vowel_params = {
    "あ": {
        "freq": [freq*1, freq*2, freq*3, freq*4, freq*5],
        "amp":  [0.40, 0.15, 0.35, 0.30, 0.10]
    },
    "い": {
        "freq": [freq*1, freq*2, freq*10, freq*11],
        "amp":  [0.52, 0.03, 0.02, 0.02, 0.03]
    },
    "う": {
        "freq": [freq*1, freq*2, freq*4, freq*5, freq*6],
        "amp":  [0.45, 0.20, 0.05, 0.05, 0.02]
    },
    "え": {
        "freq": [freq*1, freq*2, freq*3, freq*8, freq*9],
        "amp":  [0.20, 0.40, 0.03, 0.05, 0.01]
    },
    "お": {
        "freq": [freq*1, freq*2, freq*3, freq*4],
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

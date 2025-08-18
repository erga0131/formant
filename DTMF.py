import numpy as np
import sounddevice as sd

text = "1199##9 6633221 9966332 9966332 1199##9 6633221"

fs = 44100
d = 0.5
t = np.linspace(0, d, int(d * fs), endpoint=False)

vowel_params = {
    "1": {
        "freq": [697, 1209],
    },
    "2": {
        "freq": [697, 1336],
    },
    "3": {
        "freq": [697, 1477],
    },
    "4": {
        "freq": [770, 1209],
    },
    "5": {
        "freq": [770, 1336],
    },
    "6": {
        "freq": [770, 1477],
    },
    "7": {
        "freq": [852, 1209],
    },
    "8": {
        "freq": [852, 1336],
    },
    "9": {
        "freq": [852, 1477],
    },
    "*": {
        "freq": [941, 1209],
    },
    "0": {
        "freq": [941, 1336],
    },
    "#": {
        "freq": [941, 1477],
    },
    " ": {
        "freq": [0],
    },
}

x_total = np.array([])

for char in text:
    freq = vowel_params[char]["freq"]
    x = sum(np.sin(2 * np.pi * freq[i] * t) for i in range(len(freq)))
    x_total = np.concatenate((x_total, x))

sd.play(x_total, fs)
sd.wait()

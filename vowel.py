import numpy as np
import sounddevice as sd
from matplotlib import pyplot as plt

fs = 44100 #サンプリング周波数
d = 3 #鳴らす秒数
t = np.linspace(0, d, d * fs, endpoint=False)

#あ
#freq = [270, 540, 810, 1080, 1350]
#amp  = [0.40, 0.15, 0.35, 0.30, 0.10]

#い
#freq = [270, 540, 2920, 3460, 3190]
#amp = [0.52, 0.03, 0.02, 0.02, 0.01]

#う
#freq = [270, 540, 1080, 1350, 1620]
#amp = [0.32, 0.11, 0.02, 0.02, 0.01]

#え
#freq = [270, 540, 810,1890, 2160, 2430]
#amp  = [0.30, 0.40, 0.10, 0.15, 0.10, 0.03]

#お
#freq = [270, 540, 810, 1080]
#amp  = [0.35, 0.30, 0.25, 0.10]

#1000Hz
#freq = [1000]
#amp = [1.0]

x = sum([amp[i] * np.sin(2 * np.pi * freq[i] * t) for i in range(len(freq))])

plot_d = 0.01  # 10ms
plt.plot(t[:int(fs * plot_d)], x[:int(fs * plot_d)])
plt.title("Waveform ("+str(plot_d)+" s)")
plt.grid(True)
plt.show()

fourier = np.fft.fft(x)
freqs = np.fft.fftfreq(len(x)) * fs
fig2, ax2= plt.subplots()
ax2.stem(freqs, np.abs(fourier))
ax2.set_xlim(- 3200, 3200)
plt.show()

sd.play(x, fs)
sd.wait()

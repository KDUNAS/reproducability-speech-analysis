import matplotlib.pyplot as plt
#%matplotlib inline
import seaborn
seaborn.set(style="dark")
plt.rcParams['figure.figsize'] = (16, 5)
from IPython.display import Audio
import numpy as np
import librosa
import librosa.display


## Read an Audio File
x, sr = librosa.load("../data/digits.wav")
librosa.display.waveplot(x, sr=sr)
plt.title("Raw waveform of example audio flle")
Audio(x, rate=sr)

frame_length = 1024
hop_length = 512

# Note that almost all of pysptk functions assume input array is C-contiguous and np.float4 element type
frames = librosa.util.frame(x, frame_length=frame_length, hop_length=hop_length).astype(np.float64).T
frames.shape

## Calculate energy
energy = (frames**2).sum(axis=1)
plt.plot(energy)

## Zero Crossing Rate
#nums = [3, 2, 1]
#newnums = [n+1 for n in nums]
zcr = np.array([librosa.core.zero_crossings(f, threshold=0.01).sum() for f in frames])
plt.plot(zcr)

## Normalisation
# Use the ptp method to get the peak-to-peak range for an array
zcr = zcr/zcr.ptp()
energy = energy/energy.ptp()
combined = zcr+energy
plt.plot(combined)

## use a Threshold
plt.plot(combined > 0.1)

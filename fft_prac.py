# Learn how to convert microphone input into frequency domain 

import numpy as np
import sounddevice as sd
import time

SAMPLERATE = 44100 # hz
BLOCKSIZE = 2048
CHANNELS = 1

window = np.hanning(BLOCKSIZE)

def process_block(indata, samplerate):
    mono = indata[:, 0].astype(np.float32)
    
    fft = np.fft.rfft(mono * window)
    mags = np.abs(fft)
# Source: https://github.com/Infineon/i2s-microphone/blob/master/application_examples/raspberrypi/audio_processing/basic_audio_processing.py

import sounddevice as sd
import numpy as np
from scipy.io.wavfile import write
from scipy import signal

samplerate = 48000
seconds = 10
downsample = 1
inputGainDB = 12
device = "snd_rpi_i2s_card"

# Helper function for the high-pass filter
def butterHighpass(cutoff, fs, order = 5):
    
    nyq = 0.5 * fs
    normalCutoff = cutoff / nyq
    b, a = signal.butter(order, normalCutoff, btype = "high", analog = False)
    
    return b, a

# High-pass filter for digital audio data
def butterHighpassFilter(data, cutoff, fs, order = 5):

    b, a = butterHighpass(cutoff, fs, order = order)
    y = signal.filtfilt(b, a, data)
    
    return y

# This function allows to set the audio gain in decibel
def setGainDB(audiodata, gain_db):

    audiodata *= np.power(10, gain_db/10)
    return np.array([1 if s > 1 else -1 if s < -1 else s for s in audiodata], dtype = np.float32)

def processAudioData(audiodata):
    
    # Extract mono channels from input data.
    ch1 = np.array(audiodata[::downsample, 0], dtype = np.float32)
    ch2 = np.array(audiodata[::downsample, 1], dtype = np.float32)

    # High-pass filter the data at a cutoff frequency of 10Hz.
    ch1 = butterHighpassFilter(ch1, 10, samplerate)
    ch2 = butterHighpassFilter(ch2, 10, samplerate)

    # Amplify audio data.
    ch1 = setGainDB(ch1, inputGainDB)
    ch2 = setGainDB(ch2, inputGainDB)

    # Output the data in the same format as it came in.
    return np.array([[ch1[i], ch2[i]] for i in range(len(ch1))], dtype = np.float32)

# Record stereo audio data for the given duration in seconds.
rec = sd.rec(int(seconds * samplerate), samplerate = samplerate, channels = 2)

# Wait until the recording is done
sd.wait()

# Process the audio data as explained above
processed = processAudioData(rec)

# Write the processed audio data to a wav file.
write("out.wav", int(samplerate/downsample), processed)

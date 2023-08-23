# Source: https://makersportal.com/blog/2018/8/23/recording-audio-on-the-raspberry-pi-with-python-and-a-usb-microphone

import pyaudio
import wave

form1 = pyaudio.paInt16 # 16-bit resolution
chans = 1 # 1 channel
sampRate = 44100 # 44.1kHz sampling rate
chunk = 4096 # 2^12 samples for buffer
recordSecs = 3 # seconds to record
devIndex = 2 # device index found by p.get_device_info_by_index(ii)
wavOutputFilename = 'test1.wav' # name of .wav file

# create pyaudio instantiation
audio = pyaudio.PyAudio()

# create pyaudio stream
stream = audio.open(format = form1, rate = sampRate, channels = chans,
                    input_device_index = devIndex, input = True,
                    frames_per_buffer = chunk)
print("recording")

frames = []

# loop through stream and append audio chunks to frame array
for ii in range(0,int((sampRate / chunk) * recordSecs)):
    data = stream.read(chunk)
    frames.append(data)

print("finished recording")

# stop the stream, close it, and terminate the pyaudio instantiation
stream.stop_stream()
stream.close()
audio.terminate()

# save the audio frames as .wav file
wavefile = wave.open(wavOutputFilename,"wb")
wavefile.setnchannels(chans)
wavefile.setsampwidth(audio.get_sample_size(form1))
wavefile.setframerate(sampRate)
wavefile.writeframes(b''.join(frames))
wavefile.close()

import sounddevice as sd
import soundfile as sf
import time

def async_playback(fileName):
    data, fs = sf.read(fileName)
    sd.play(data, fs)
    return data, fs

data, fs = async_playback('../../data/sample_test_file.wav')
print ('This program is playing the audio file asynchronously')

time.sleep(1)
sd.stop()
print('sound device stopped')
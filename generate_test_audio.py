import wave, struct, math
audio = wave.open('test.wav', 'wb')
audio.setnchannels(1)
audio.setsampwidth(2)
audio.setframerate(44100)
# 1 second of 440Hz sine wave
samples = [int(32767.0*math.sin(float(i)*2*math.pi*440.0/44100.0)) for i in range(44100)]
audio.writeframesraw(struct.pack('<' + str(len(samples)) + 'h', *samples))
audio.close()

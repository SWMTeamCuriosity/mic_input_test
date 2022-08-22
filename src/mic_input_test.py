RATE = 44100
RECORD_SECONDS = 1
CHUNK = 1024
CHANNELS = 1
p = pyaudio.PyAudio()

stream = p.open(format=pyaudio.paInt16,
                                channels=CHANNELS,
                                rate=RATE,
                                input=True,
                                output=True,
                                frames_per_buffer=CHUNK)

print("* recording")
frames = []
for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    frames.append(data)


print("* done recording")
# stop stream (4)
stream.stop_stream()
stream.close()

# close PyAudio (5)
p.terminate()
# save to file

file.setnchannels(1)
file.setsampwidth(p.get_sample_size(pyaudio.paInt16))
file.setframerate(RATE)

# Write and Close the File
file.writeframes(b''.join(frames))
file.close()')

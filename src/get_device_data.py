import pyaudio

def get_device_data(audio) :
    for index in range(audio.get_device_count()):
        desc = audio.get_device_info_by_index(index)
        print("DEVICE: {device}, INDEX: {index}, RATE: {rate} ".format(
                    device=desc["name"], index=index, rate=int(desc["defaultSampleRate"])
        ))

if __name__ == "__main__" :
    f = pyaudio.PyAudio()
    get_device_data(f)
    print( f.get_default_input_device_info() )

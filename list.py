import pyaudio

p = pyaudio.PyAudio()
info = p.get_host_api_info_by_index(0)
numdevices = info.get('deviceCount')
for i in range(0, numdevices):
    info = p.get_device_info_by_host_api_device_index(0, i)
    print("%d\t%d\t%d\t%s"%(i,info['maxInputChannels'], info['maxOutputChannels'], info['name']))
    # if (p.get_device_info_by_host_api_device_index(0, i).get('maxInputChannels')) > 0:
    #     name = p.get_device_info_by_host_api_device_index(0, i).get('name')
    #     print("Input Device id ", i, " - ", name)
    #     if "Loopback" in name:
    #         print("%d"%i)

import audio.pytool_audio as pyaudio


# 参数输入
sr = 96000
bit_depth = 24
ch_num = 2
frame_ms = 10


# 调用举例
kbps = pyaudio.get_br_of_audio(sr, bit_depth, ch_num, frame_ms)
print('{}kbps'.format(kbps))

bits = pyaudio.get_bits_of_audio(sr, bit_depth, ch_num, frame_ms)
print('{}bits'.format(bits))

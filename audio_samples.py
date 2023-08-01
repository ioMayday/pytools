import audio.pytool_audio


# 参数输入
sr = 96000
bit_depth = 24
ch_num = 2
frame_ms = 10


# 调用举例
kbps = get_br_of_audio(sr, bit_depth, ch_num, frame_ms)
print('{}kbps'.format(kbps))
bits = get_bits_of_audio(sr, bit_depth, ch_num, frame_ms)
print('{}bits'.format(bits))

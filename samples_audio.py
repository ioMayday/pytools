import audio.pytool_audio as pyaudio


# 音频参数计算调用举例
sr = 96000
bit_depth = 24
ch_num = 2
frame_ms = 10
kbps = pyaudio.get_br_of_audio(sr, bit_depth, ch_num, frame_ms)
print('{}kbps'.format(kbps))
bits = pyaudio.get_bits_of_audio(sr, bit_depth, ch_num, frame_ms)
print('{}bits'.format(bits))


# 幅值到分贝相互转换
bit_depth = 24
sp = 1024
db = -78.27
dbfs = pyaudio.sample_to_dbfs(sp, bit_depth)
sample = pyaudio.dbfs_to_sample(db, bit_depth)
print('sample: {0:0.2f}, dBFS: {1:0.2f}'.format(sample, dbfs))

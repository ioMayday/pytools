# 语音处理中，音频常用参数计算


# 计算声道信息下对应样点数
def get_samples_of_audio(sr, ch_num, frame_s):
    samples = sr * frame_s * ch_num
    return samples


# 计算声道信息下不压缩时原始码率kbps
def get_br_of_audio(sr, bit_depth, ch_num, frame_ms):
    frame_s = frame_ms / 1000 
    samples = get_samples_of_audio(sr, ch_num, frame_s)
    total_bits = samples * bit_depth
    bps = total_bits / frame_s
    kbps = bps / 1000
    return kbps


# 计算码率及帧长条件下的比特
def br_to_bits(kbps, frame_ms):
    bits = kbps * frame_ms
    return bits


# 计算比特到码率
def bits_to_br(bits, frame_ms):
    kbps = bits / frame_ms
    return kbps


# 计算字节数到比特数
def byte_to_bit(byte_num):
    bits = 8 * byte_num
    return bits


# 计算比特数到字节数
def bit_to_byte(bits):
    byte_num = bits / 8
    return byte_num


# 计算声道信息下对应比特
def get_bits_of_audio(sr, bit_depth, ch_num, frame_ms):
    kbps = get_br_of_audio(sr, bit_depth, ch_num, frame_ms)
    bits = br_to_bits(kbps, frame_ms)
    return bits


# 计算字节数到码率，字节数为压缩后的1帧字节流大小，码率为压缩后的实际码率
def bytes_to_br(byte_num, frame_ms):
    bits = byte_to_bit(byte_num)
    kbps = bits_to_br(bits, frame_ms)
    return kbps
    

# 计算码率到字节数
def br_to_bytes(kbps, frame_ms):
    bits = br_to_bits(kbps, frame_ms)
    byte_num = bit_to_byte(bits)
    return byte_num


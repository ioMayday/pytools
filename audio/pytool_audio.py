# 语音处理中，音频常用参数计算
import math as mt

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


"""
幅值到分贝相互转换dB/dBFS
bit_depth: 位深
VAL2LOG_COEF: 幅值到能量缩放系数
LOG_POW_BASE: 对数变换的底
return: db/dbfs/val
"""

# 常量定义
BIT_DEPTH_I16 = 16
BIT_DEPTH_I24 = 24
BIT_DEPTH_I32 = 32
BIT_DEPTH_F32 = -32
VAL2LOG_COEF  = 20
LOG_POW_BASE  = 10


# 根据位深获取最大幅值
def get_sample_ref_val(bit_depth):
# 仅支持整型16/24/32位和浮点32位位深
    ref_val = 0
    if bit_depth == BIT_DEPTH_F32:         # float32
        ref_val = 1.0
    elif ((bit_depth == BIT_DEPTH_I16) or   # int16
          (bit_depth == BIT_DEPTH_I24) or   # int24
          (bit_depth == BIT_DEPTH_I32)):    # int32
        ref_val = 2 ** (bit_depth - 1) - 1
    else:
        print('not supported bitdepth =', bit_depth)
        return -1
    return ref_val


# dBFS到采样值
def dbfs_to_sample(db, bit_depth):
    # assumed that bit_depth is verfied
    ref_val = get_sample_ref_val(bit_depth)
    sample = pow(LOG_POW_BASE, db / VAL2LOG_COEF) * ref_val
    return sample


# 采样值到dBFS
def sample_to_dbfs(sample, bit_depth):
    # assumed that bit_depth is verfied
    ref_val = get_sample_ref_val(bit_depth)
    sample_clip = min(abs(sample), ref_val)
    ratio = sample_clip / ref_val
    dBFS = VAL2LOG_COEF * mt.log(ratio, LOG_POW_BASE)
    return dBFS

# db到采样值
def db_to_sample(db):
    val = pow(LOG_POW_BASE, db / VAL2LOG_COEF)
    return val

# 采样值到db
def sample_to_db(val):
    db = VAL2LOG_COEF * mt.log(val, LOG_POW_BASE)
    return db

# -*- coding: utf-8 -*-
'''
功能：自动化语音打分
博客：Python世界：基于PESQ的自动化语音打分脚本实践
地址：https://blog.csdn.net/qq_17256689/article/details/142185696
'''

import os
import wave

def pesq_one_seq(path_wav_in, path_wav_out, path_pesq_exe):
    # 检验wav参数
    with wave.open(path_wav_in, "rb") as wav_in:
        sample_rate_in = wav_in.getframerate()
        ch_in = wav_in.getnchannels()
    if (sample_rate_in != 8000 and sample_rate_in != 16000):
        print(wav_in, "{} sr not supported!".format(sample_rate_in))
        return
    if (ch_in != 1):
        print(wav_in, "{} ch not supported!".format(ch_in))
        return

    with wave.open(path_wav_out, "rb") as wav_out:
        sample_rate_out = wav_out.getframerate()
        ch_out = wav_out.getnchannels()
    if (sample_rate_out != sample_rate_in or ch_in != ch_out):
        print("wav in/out not same! in: {0}, {1}, out: {2}, {3}".format(
            sample_rate_in, ch_in, sample_rate_out, ch_out))
        return

    # exe入参处理
    param_sr = "+" + str(sample_rate_in)
    if (sample_rate_in == 16000):
        param_bw = "+wb"
    else:
        param_bw = " "
    param = "{0} {1} {2} {3} {4}".format(path_pesq_exe, param_sr, param_bw, path_wav_in, path_wav_out)
    print(param)

    # exe运行
    os.system(param)
    time.sleep(5)
    return


def run_exe_pesq():
    path_pesq_exe = r"E:\pesq.exe"
    path_wav_in = r'E:\wav_in'
    path_wav_out = r"E:\wav_out"
    namelist = os.listdir(path_wav_in)
    name_wav_out = os.listdir(path_wav_out)
    for file_name in namelist:
        for name_out in name_wav_out:
           name_in_rm_postfix = file_name.split('.')[0]
           if name_in_rm_postfix in name_out:
                wav_in = os.path.join(path_wav_in, file_name)
                wav_out = os.path.join(path_wav_out, name_out)
                pesq_one_seq(wav_in, wav_out, path_pesq_exe)
    return


if __name__ == '__main__':
    print('start!')

    # 正式运行
    run_exe_pesq()

    print('done!')



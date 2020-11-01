from os import path
from pydub import AudioSegment

import os
import glob

src_path = '/data/luomingshuang/olr/data'
dst_path = '/data/luomingshuang/olr/data_wav'

languages = ['粤语','蒙语','维语','藏语','英语','阿拉伯语']

for language in languages:
    mp3_files = glob.glob(os.path.join(src_path, language, '*', '*.mp3'))
    print('the {} mp3 files: '.format(language), len(mp3_files))
    for mp3 in mp3_files:
        print(mp3)
        items = mp3.split('/')
        dirname = dst_path+'/'+items[-3]+'/'+items[-2]
        wavname = items[-1][:-3]+'wav'
        if not os.path.exists(dirname):
            os.makedirs(dirname)
        dst = dirname+'/'+wavname

        ###generate mp3 object
        sound = AudioSegment.from_file(mp3, format='mp3')

        ###修改对象参数
        sound1 = sound.set_frame_rate(16000)
        sound1 = sound1.set_channels(1)
        sound1 = sound1.set_sample_width(2)

        ###导出wav文件
        print(dst)
        sound1.export(dst, format='wav')

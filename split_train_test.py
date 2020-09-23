import os
import glob
import random
import shutil
#import shuffle

total_data = '/data/luomingshuang/olr/data_wav_vad'

train_data = '/data/luomingshuang/olr/data_wav_vad/train'

test_data = '/data/luomingshuang/olr/data_wav_vad/test'

languages = ['藏语', '维语', '蒙语', '粤语', '英语', '阿拉伯语']

for language in languages:
    files = glob.glob(os.path.join(total_data, language, '*', '*.wav'))
    random.shuffle(files)
    length = len(files)
    trdirname = train_data+'/'+language
    tsdirname = test_data+'/'+language

    if not os.path.exists(trdirname):os.makedirs(trdirname)
    if not os.path.exists(tsdirname):os.makedirs(tsdirname)

    traindata = files[:int(0.8*length)]
    testdata = files[int(0.8*length):]
    print('the number of {} wav samples: '.format(language), length)
    print('train: ', len(traindata))
    print('test: ', len(testdata))
    for wav in traindata:
        #print(wav)
        #name = wav.split('/')[-1]
        shutil.copy(wav, trdirname)
    for wav in testdata:
        #name = wav.split('/')[-1]
        shutil.copy(wav, tsdirname)

import os
import torch
import glob
import numpy as np
from torch.utils.data import Dataset

import options as opt

from audio_fbank import read_mfcc, sample_from_mfcc

languages = ['藏语', '维语', '蒙语', '粤语', '英语', '阿拉伯语']

class Mydataset(Dataset):
    def __init__(self, data_path, phase):
        #self.path = data_path
        self.path = '/data/luomingshuang/olr/data_new'
        self.phase = phase
        samples = []
        samples = glob.glob(os.path.join(self.path, '阿拉伯语','*', '*', '*.wav'))
        self.samples = samples
        print('the data for {}: '.format(self.phase), len(self.samples))
    
    def __len__(self):
        return len(self.samples)

    def __getitem__(self, idx):
        sample = self.samples[idx]
        items = sample.split('/')
        language = items[-4]
        label = languages.index(language)

        feature = sample_from_mfcc(read_mfcc(sample, opt.SAMPLE_RATE), opt.NUM_FRAMES)
        #feature = np.expand_dims(feature, axis=0)
        feature = feature.transpose(2, 0, 1)

        return torch.FloatTensor(feature), label


sr = 16000
window = 0.025 #(s)=25ms
hop = 0.01 #(s)=10ms
nmels = 40
tisv_frame = 180

nfft = 512

embedding_size = 512

classes = 6

SAMPLE_RATE = 16000

NUM_FRAMES = 160

NUM_FBANKS = 64

TRAIN_TEST_RATIO = 0.8

data_path = '/data/luomingshuang/olr/data_wav_vad'

batch_size = 100

lr = 1e-4

num_workers = 16

max_epochs= 10000

save_dir = 'weights'

weights = 'weights/olr_86_epoch_test_acc_0.9836885321524126.pt'

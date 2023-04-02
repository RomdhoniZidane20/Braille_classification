import os
from shutil import copyfile

os.mkdir('/home/ichiro/KP_braille/resize_images_V2/')
os.path.join('/home/ichiro/KP_braille/resize_images_V2/')

os.mkdir('/home/ichiro/KP_braille/resize_images_V2/train/')
os.mkdir('/home/ichiro/KP_braille/resize_images_V2/valid/')
os.mkdir('/home/ichiro/KP_braille/resize_images_V2/test/')

os.path.join('/home/ichiro/KP_braille/resize_images_V2/train/')
os.path.join('/home/ichiro/KP_braille/resize_images_V2/valid/')
os.path.join('/home/ichiro/KP_braille/resize_images_V2/test/')


alpha = 'a'
for i in range(0, 26):
    os.mkdir('/home/ichiro/KP_braille/resize_images_V2/train/' + alpha)
    os.mkdir('/home/ichiro/KP_braille/resize_images_V2/valid/' + alpha)
    os.mkdir('/home/ichiro/KP_braille/resize_images_V2/test/'  + alpha)
    alpha = chr(ord(alpha) + 1)
# #
rootdir_train = '/home/ichiro/KP_braille/DATASET_BRAILLE_V2/train/'
rootdir_valid = '/home/ichiro/KP_braille/DATASET_BRAILLE_V2/valid/'
rootdir_test  = '/home/ichiro/KP_braille/DATASET_BRAILLE_V2/test/'

for file in os.listdir(rootdir_train):
    letter = file[0]
    copyfile(rootdir_train + file, '/home/ichiro/KP_braille/resize_images_V2/train/' + letter + '/' + file)

for file in os.listdir(rootdir_valid):
    letter = file[0]
    copyfile(rootdir_valid + file, '/home/ichiro/KP_braille/resize_images_V2/valid/' + letter + '/' + file)

for file in os.listdir(rootdir_test):
    letter = file[0]
    copyfile(rootdir_test + file, '/home/ichiro/KP_braille/resize_images_V2/test/' + letter + '/' + file)

import os
import numpy as np
import pandas as pd
from shutil import copyfile
from tensorflow import keras
from keras.preprocessing.image import ImageDataGenerator
from keras import backend as K
from keras import layers as L
from keras.models import Model,load_model
from keras.regularizers import l2
from keras.callbacks import ModelCheckpoint,ReduceLROnPlateau,EarlyStopping

def main():

    # os.mkdir('./images/')
    # alpha = 'a'
    # for i in range(0, 26):
    #     os.mkdir('./images/' + alpha)
    #     alpha = chr(ord(alpha) + 1)

    # rootdir = '/home/ichiro/KP_braille/Braille Dataset/'
    # for file in os.listdir(rootdir):
    #     letter = file[0]
    #     copyfile(rootdir+file, './images/' + letter + '/' + file)

    train_data = '/home/ichiro/KP_braille/images/'
    val_data = '/home/ichiro/KP_braille/images/'

    datagen = ImageDataGenerator(rotation_range=20,
                                shear_range=10,
                                validation_split=0.2)

    train_generator = datagen.flow_from_directory(train_data,
                                                target_size=(28,28),
                                                subset='training')

    val_generator = datagen.flow_from_directory(val_data,
                                                target_size=(28,28),
                                                subset='validation')

    K.clear_session()

    model_ckpt = ModelCheckpoint('BrailleNet.h5', save_best_only=True)
    reduce_lr = ReduceLROnPlateau(patience=8, verbose=0)
    early_stop = EarlyStopping(patience=15, verbose=1)

    entry = L.Input(shape=(28, 28, 3))
    x = L.SeparableConv2D(64, (3, 3), activation='relu')(entry)
    x = L.MaxPooling2D((2, 2))(x)
    x = L.SeparableConv2D(128, (3, 3), activation='relu')(x)
    x = L.MaxPooling2D((2, 2))(x)
    x = L.SeparableConv2D(256, (2, 2), activation='relu')(x)
    x = L.GlobalMaxPooling2D()(x)
    x = L.Dense(256)(x)
    x = L.LeakyReLU()(x)
    x = L.Dense(64)(x)
    x = L.LeakyReLU()(x)
    x = L.Dense(26, activation='softmax')(x)

    model = Model(entry, x)
    model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

    model.fit_generator(train_generator,
                                  validation_data=val_generator,
                                  epochs=666,
                                  # callbacks=[model_ckpt, reduce_lr, early_stop],
                                  verbose=1)

    return model

if __name__ == '__main__':
    model = main()
    model.save("model_braille_sendiri.h5")
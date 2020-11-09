import os
from tensorflow.python.keras.preprocessing.image import ImageDataGenerator
from tensorflow.python.keras.models import Sequential
from tensorflow.python.keras.layers import Dropout,Flatten,Dense
from tensorflow.python.keras.layers import Convolution2D, MaxPooling2D
from tensorflow.python.keras import backend as K


K.clear_session()

training_data = 'training/'
validation_data = 'validation/'


#Global Parameters

epochs=200
height, length=100,100
batch_size=160
steps=3
steps_validation=3
filtrosConvl1=32
filtrosConvl2=64
tamano_filtro1=(3,3)
tamano_filtro2=(2,2)
tamano_pool=(2,2)
clases=3
lr=0.0005

#Image pre_processing


training_data_gen  = ImageDataGenerator(
    rescale=1./255,
    shear_range=0.3,
    zoom_range=0.3,
    horizontal_flip=True
)

validation_data_gen = ImageDataGenerator(
    rescale=1./255,
)


img_training = training_data_gen.flow_from_directory(
    training_data,
    target_size=(height,length),
    batch_size=batch_size,
    class_mode='categorical'
)

img_validation = validation_data_gen.flow_from_directory(
    validation_data,
    target_size=(height,length),
    batch_size=batch_size,
    class_mode='categorical'
)

print(img_training.class_indices)



#Create the Convolutional Neural Networks

convolutional_neural_netwoks = Sequential()

convolutional_neural_netwoks.add(Convolution2D(filtrosConvl1,tamano_filtro1,padding='same',input_shape=(height,length,3), activation='relu'))

convolutional_neural_netwoks.add(MaxPooling2D(pool_size=tamano_pool))

convolutional_neural_netwoks.add(Convolution2D(filtrosConvl2,tamano_filtro2,padding='same', activation='relu'))

convolutional_neural_netwoks.add(MaxPooling2D(pool_size=tamano_pool))

convolutional_neural_netwoks.add(Flatten())

convolutional_neural_netwoks.add(Dense(256,activation='relu'))

convolutional_neural_netwoks.add(Dropout(0.5))

convolutional_neural_netwoks.add(Dense(clases,activation='softmax'))

convolutional_neural_netwoks.compile(loss='categorical_crossentropy', optimizer='adam',metrics=['accuracy'])

convolutional_neural_netwoks.fit_generator(img_training, steps_per_epoch=steps, epochs=epochs, validation_data=img_validation, validation_steps = steps_validation)

dir='modelo/'

if not os.path.exists(dir):
    os.mkdir(dir)

convolutional_neural_netwoks.save('modelo/modelo.h5')
convolutional_neural_netwoks.save_weights('modelo/pesos.h5')










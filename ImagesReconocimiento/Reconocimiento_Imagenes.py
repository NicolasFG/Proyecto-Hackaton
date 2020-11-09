import numpy as np
from keras.preprocessing.image import load_img, img_to_array
from keras.models import load_model

height, length = 100,100
model='modelo/modelo.h5'
weight='modelo/pesos.h5'
convolutional_neural_netwoks =load_model(model)
convolutional_neural_netwoks.load_weights(weight)

def Recognition(file, Campo):
    x = load_img(file, target_size=(height, length))
    x = img_to_array(x)
    x=np.expand_dims(x, axis=0)
    arreglo=convolutional_neural_netwoks.predict(x)
    resultado = arreglo[0]
    respuesta = np.argmax(resultado)

    if Campo == 'Fachada':
        if respuesta == 0:
            print("No conforme")
        elif respuesta == 1:
            print("No Conforme")
        elif respuesta == 2:
            print("Conforme")
    elif Campo == 'Cintillo':
        if respuesta == 0:
            print("No conforme")
        elif respuesta == 1:
            print("Conforme")
        elif respuesta == 2:
            print("No conforme")

    return respuesta






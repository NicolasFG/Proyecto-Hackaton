import numpy as np
import os
from os import listdir
from os.path import isfile, isdir

from timeit import default_timer
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


def Recognition_sin_Campo(file):

    x = load_img(file, target_size=(height, length))
    x = img_to_array(x)
    x=np.expand_dims(x, axis=0)
    arreglo=convolutional_neural_netwoks.predict(x)
    resultado = arreglo[0]
    respuesta = np.argmax(resultado)

    if respuesta == 2:
        return "Fachada"
    elif respuesta == 1:
        return "Cintillo"
    elif respuesta == 0:
        return "Otros"


#ruta = 'testing/Evaluacion'



def Recognition_varios(ruta):
    ver = isdir(ruta)
    respuestaFinal = []
    if ver == True:

        for i in listdir(ruta):

            x = load_img(ruta + '//' + i , target_size=(height,length))
            x = img_to_array(x)
            x = np.expand_dims(x, axis=0)
            arreglo = convolutional_neural_netwoks.predict(x)
            resultado = arreglo[0]
            respuesta = np.argmax(resultado)
            respuestaFinal.append(respuesta)

            if respuesta == 2:
                print("Conforme")
            elif respuesta == 1:
                print("Conforme")
            elif respuesta == 0:
                print("No conforme")

        '''
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
      '''
    return respuesta


'''
inicio = default_timer()
Recognition('validation/Otros/CINTILLO_155.jpg', "Cintillo")
fin = default_timer()
print(fin-inicio)
 '''

#Recognition_varios('testing/Evaluacion2/Cintillos')





import time

import validacion_formulario
import Reconocimiento_Imagenes

print("Validación de Formularios")

validacion_formulario.login_plataforma('HACKATON1', 'Hackaton_1')
print("Test 1:")
validacion_formulario.validar_campos_formulario('12486764')
print("Test 2:")
validacion_formulario.validar_campos_formulario('12488495')
print("Test 3:")
validacion_formulario.validar_campos_formulario('88108038')
print("Test 4:")
validacion_formulario.validar_campos_formulario('12491276')
print("Test 5:")
validacion_formulario.validar_campos_formulario('12472502')

time.sleep(5)


Reconocimiento_Imagenes.Recognition('validation/fachadas/FACHADA_376.jpg', "Fachada")



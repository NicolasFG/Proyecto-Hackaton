import time

import Validacion_Formulario
import Reconocimiento_Imagenes

print("Validación de Formularios")

Validacion_Formulario.login_plataforma('HACKATON1', 'Hackaton_1')
print("Test 1:")
Validacion_Formulario.validar_campos_formulario('12486764')
print("Test 2:")
Validacion_Formulario.validar_campos_formulario('12488495')
print("Test 3:")
Validacion_Formulario.validar_campos_formulario('88108038')
print("Test 4:")
Validacion_Formulario.validar_campos_formulario('12491276')
print("Test 5:")
Validacion_Formulario.validar_campos_formulario('12472502')

time.sleep(5)

Reconocimiento_Imagenes.Recognition('testing/Evaluacion/FOTO10.jpeg', "Fachada")



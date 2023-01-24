from pyfirmata import Arduino, util
import time
                               
Uno = Arduino('COM3')
                                     
print('Olá Mundo!')                 

tempo = 0

while True:    
    
    tempo = tempo + 0.1

    Uno.digital[13].write(1)        
    print('LED ligado', tempo)              
    time.sleep(tempo)                    

    Uno.digital[13].write(0)         
    print('LED desligado', tempo)           
    time.sleep(tempo)                    

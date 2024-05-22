import os
from ejemplo_1.funciones_calculadora import *

seguir='si'
flag_A=False
flag_B=False
flag_C=False

while(seguir == 'si'):
    
    opcion=Menu_principal()
    
    if(opcion=='a' or opcion=='b' or opcion=='c' or opcion=='d' or opcion=='e'):
         match opcion:
            case 'a':
                aux1=Pedir_entero('Primer operando: ')
                flag_A=True
        
            case 'b':
                if(flag_A==True):
                    aux2=Pedir_entero('Segundo operando: ')
                    flag_B=True
                else:
                    print('Antes debe ingresar el primer operando...')
                    
            case 'c':
                if(flag_A==True and flag_B==True):
                    os.system('cls')
                    while(True):
                        
                        operacion=Menu_secundario()
                        if(operacion==1 or operacion==2 or operacion==3 or operacion==4):
                            
                            resultado=realizar_operacion(operacion,aux1,aux2)
                            
                            print('Operacion realizada con exito.')
                            
                            flag_C=True
                            break
                        else:
                            print("Error operacion realizada invalida.")
                            os.system("pause")
                        os.system("cls")
                else:
                    print('Antes de elegir la operacion debe ingresar los operandos...')
                    
            case 'd':
                if(flag_C==True):
                    print(resultado)
                    flag_A=False
                    flag_B=False
                    flag_C=False
                else:
                    print('Antes de mostrar resultado debe seleccionar la operacion a realizar.')
                
            case 'e':
                seguir=Salir_programa()
                
        
    else:
         
        print("Error opcion ingresada invalida.")
    os.system('pause')            
    os.system('cls')           
    
           
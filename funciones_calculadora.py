import os
def realizar_operacion(operacion:int,A:int,B:int)->int:

    match operacion:
                    case 1:
                        Sumar=A+B
                        rta= Sumar
                    case 2:
                        Restar=A-B
                        rta= Restar
                    case 3:
                        Multiplicar=A*B
                        rta= Multiplicar
                    case 4:
                        Dividir=A/B
                        rta= Dividir
    return rta
 
def Menu_principal()->str:
    
    print("""           
            CALCULADORA DE PYTHON
        
    A) Ingresar primer operando.
    
    B) Ingresar segundo operando.
    
    C) Elegir operacion a realizar.
    
    D) Mostrar resultado.
    
    E) Salir.
    
        """)
    opcion=input('Ingrese opcion: ').lower()
    return opcion

def Menu_secundario()->int:
    
    while(True):
        print("""
            Operacion a realizar.
                            
    ingrese  1 para sumar
    ingrese  2 para restar
    ingrese  3 para multiplicar
    ingrese  4 para dividir
                            
                        """)
        try:
            operacion=int(input('Ingrese opcion: '))
            return operacion
        except:
            print("Error. Ingrese opcion valida.")
            os.system("pause")
            os.system("cls")
        

def Pedir_entero(mensaje:str)->int:
    while(True):
        print()
        try:
            aux1=int(input(mensaje))
            print("Numero registrado")
            return aux1
        except:
            print('Error. Ingrese un numero.')
           
        
def Salir_programa()->str:
    while(True):
        print()
        rta=input('Desea salir del programa? ')
        if(rta=="si"):
            seguir="no"
            return seguir
            break
        elif(rta=='no'):
            seguir="si"
            return seguir
        else:
            
            print("Error. conteste con 'si' o 'no' ")
        
        
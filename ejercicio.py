import funciones as fn
opc=0
while True:
    fn.funcionMenu()
    try:
        opc=int(input("Ingresar opcion: "))
        if opc==1:
            fn.funcionGrabar()
        elif opc==2:
            fn.funcionBuscar()
        elif opc==3:
            fn.funcionPareja()
        elif opc==4:
            fn.funcionSalir()
            break
        else:
            print("Rango invalido menu")
    except:
        print("Excepcion menu")
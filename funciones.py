from datetime import date
line='-'*50
anio_actual=2023
'''
    nombre (2 catacteres min)
    rut
    fecha nacimiento (no mas 80 años)
    categoria (oro-plata-bronce)
    celular
    identificador de parejas (nombre equipo)
    correo (debe tener @ y len 6)

    buscar por rut, mostrar nmbre, categoria, fono y email
    
    imprimir pareja por identificador, nombres
'''
listaNombre=['SMOLENKS','MATIAS']
listaRut=[21000000,19000000]
listaNacimiento=[2002,1995]
listaCategoria=['Bronce','Plata']
listaCelular=[123123123,321321321]
listaIdentificador=['PATO','PATO']
listaEmail=['test@test','email@email']

noneTemp=None
strTemp=''
intTemp=0
flagTemp=False
def funcionMenu():
    print (f"{line}\nPadel - Yari Villagrande\n{line}\n1. Grabar\n2. Buscar\n3. Imprimir Parejas\n4. Salir\n{line}")

def funcionGrabar():
    while True:
        try:
            strTemp=str(input("Ingresar nombre [Min 2 Caracteres]: "))
            if len(strTemp)<2:
                print("Nombre minimo 2 caracteres")
            else:
                strTemp=strTemp.upper()
                listaNombre.append(strTemp)
                break
        except:
            print("Excepcion guardar nombre, SOLO LETRAS")

    while True:
        try:
            intTemp=int(input("Ingresar rut [Sin digito verificador]: "))
            if intTemp<10000000:
                print("Minimo 10 Millones")
            else:
                listaRut.append(intTemp)
                break
        except:
            print("Excepcion guardar rut")

    while True:
        try:
            intTemp=int(input("Ingresar año nacimiento: "))
            if intTemp>anio_actual and (anio_actual-intTemp)>80:
                print("Año nacimiento rango invalido")
            else:
                listaNacimiento.append(intTemp)
                break
        except:
            print("Excepcion guardar fecha nacimiento")

    while True:
        try:
            print(f"{line}\n1. Oro\n2. Plata\n3. Bronce\n{line}")
            intTemp=int(input("Ingresar categoria equipo: "))
            if intTemp==1:
                listaCategoria.append('Oro')
                break
            elif intTemp==2:
                listaCategoria.append('Plata')
                break
            elif intTemp==3:
                listaCategoria.append('Bronce')
                break
            else:
                print("Rango invalido categoria")
        except:
            print("Excepcion guardar categoria")

    while True:
        try:
            intTemp=int(input("Ingresar celular [9 Caracteres Minimo]: "))
            if intTemp<100000000:
                print("Rango invalido celular")
            else:
                listaCelular.append(intTemp)
                break
        except:
            print("Excepcion guardar numero celular")

    while True:
        try:
            strTemp=str(input("Ingresar identificador [Nombre Equipo]: "))
            if len(strTemp)<2:
                print("Identificador minimo 2 caracteres")
            else:
                strTemp=strTemp.upper()
                listaIdentificador.append(strTemp)
                break
        except:
            print("Excepcion guardar identificador, SOLO LETRAS")

    while True:
        try:
            strTemp=input("Ingresar email [con '@' y 6 caracteres minimo]: ")

            for i in strTemp:
                if i=='@':
                    flagTemp=True
            
            if flagTemp and len(strTemp)>=6:
                strTemp=strTemp.lower()
                listaEmail.append(strTemp)
                break
            else:
                print("Email invalido")
        except:
            print("Excepcion guardar email")

def funcionBuscar():
    while True:
        try:
            intTemp=int(input("Ingresar Rut [Sin Digito Verificador] a buscar: "))
            for i in range(len(listaRut)):
                if intTemp==listaRut[i]:
                    flagTemp=True
            
            if flagTemp:
                for i in range(len(listaRut)):
                    if intTemp==listaRut[i]:
                        print(f"{line}\n| Nombre: {listaNombre[i]} | Categoria: {listaCategoria[i]} | Fono: {listaCelular[i]} | Email: {listaEmail[i]}")
                break
            else:
                print("Rut no existe")
        except:
            print("Excepcion buscar rut")

def funcionPareja():
    while True:
        try:
            strTemp=input("Ingresar Identificador Pareja [Nombre Equipo] a buscar: ").upper()
            for i in range(len(listaIdentificador)):
                if strTemp==listaIdentificador[i]:
                    flagTemp=True

            if flagTemp:
                print(f"{line}\nIntegrantes: {strTemp}\n{line}")
                for i in range(len(listaIdentificador)):
                    if strTemp==listaIdentificador[i]:
                        print(f"| Nombre: {listaNombre[i]} |")
                break
            else:
                print("Identificador equipo no existe")
        except:
            print("Excepcion buscar identificador")

def funcionSalir():
    print("smolenks aravena se despide con estres")
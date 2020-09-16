from tkinter import Tk, Menu, messagebox, filedialog, ttk, Label, scrolledtext, INSERT, END, Button, Scrollbar, RIGHT, Y, Frame, Canvas, HORIZONTAL, VERTICAL, simpledialog
from Buffer import Buffer
from LexicalAnalyzer import LexicalAnalyzer
from pila import Pila
from afd import afd
import os
import subprocess

root = Tk()
root.title("Analizador")
root.configure(background = "gray")

'''FUNCIONES DEL MENU'''

archivo = ""

Buffer = Buffer()
Analyzer = LexicalAnalyzer()
Afd=afd()

def nuevo():
    global archivo
    editor.delete(1.0, END)#ELIMINAR EL CONTENIDO
    archivo = ""

def abrir():
    global archivo
    archivo = filedialog.askopenfilename(title = "Abrir Archivo", initialdir = "C:/")

    entrada = open(archivo)
    content = entrada.read()

    editor.delete(1.0, END)
    editor.insert(INSERT, content)

    #editor.tag_add("start", "2.8", "2.13")
    consola.tag_config("start", background="black", foreground="yellow")
    


    entrada.close()

    consola.insert(INSERT, "Abriendo archivo " + archivo + "\n")
    consola.insert(INSERT, "Prueba \n", "start")

def salir():
    value = messagebox.askokcancel("Salir", "Está seguro que desea salir?")
    if value :
        root.destroy()

def guardarArchivo():
    global archivo
    if archivo == "":
        guardarComo()
    else:
        guardarc = open(archivo, "w")
        guardarc.write(editor.get(1.0, END))
        guardarc.close()

def guardarComo():
    global archivo
    guardar = filedialog.asksaveasfilename(title = "Guardar Archivo", initialdir = "C:/")
    fguardar = open(guardar, "w+")
    fguardar.write(editor.get(1.0, END))
    fguardar.close()
    archivo = guardar

def afdjs():
    os.system('dot AFD.dot -Tpng -o AFD.png')
    print("Generando reporte...")
    subprocess.Popen("AFD.png",shell=True)


def erroresjs():
    subprocess.Popen("Erroresjs.html",shell=True)

def errorescss():
    subprocess.Popen("Errorescss.html",shell=True)

def erroreshtml():
    subprocess.Popen("Erroreshtml.html",shell=True)

def reportesin():
    subprocess.Popen("Reportesintactico.html",shell=True)

def ejecutar():
    global archivo

    #write()

    print("Ejecutando Analisis Lexico...")

    if archivo == "":
        print("No hay archivos para analizar, guarde el archivo para continuar")

    else:

        tipoarchivo = archivo.split(".")
        print("Extension archivo: " + tipoarchivo[1])

        nombrearchivo = archivo.split("/")
        print("Nombre archivo: " + nombrearchivo[-1])

        path = ""
    


        if tipoarchivo[1] == "js":
            print("Analizando archivo de JavaScript")
            # Lists for every list returned list from the function tokenize
            token = []
            lexeme = []
            row = []
            column = []
            error = []
            rowerror = []
            colerror = []
 
            # Tokenize and reload of the buffer
            #entrada = 'program.c'
            for i in Buffer.load_buffer(archivo):
                t, lex, lin, col, e, re, ce = Analyzer.tokenizejs(i)
                token += t
                lexeme += lex
                row += lin
                column += col
                error += e
                rowerror += re
                colerror += ce

        
            print('\nRecognize Tokens: ', token)
            Analyzer.lin_num = 1

            automata = Afd.abrir_archivo(archivo)
            Afd.escribir_archivo(automata)

            f= open("Erroresjs.html","w+")

            f.write("<html>\n")
            f.write("<head>\n")
            f.write("<title>Reporte errores js</title>\n")
            f.write("</head>\n")
            f.write("<body>\n")
            f.write("<h1 >Reporte Errores JavaScript</h1>\n")
            f.write("<table border=\"1\">\n")
            f.write("<tr>\n")
            f.write("<td> No. </td>\n")
            f.write("<td> Fila </td>\n")
            f.write("<td> Columna </td>\n")
            f.write("<td> Error </td>\n")
            f.write("</tr>\n")

            contadorerror = 1
            for i in range(len(error)):
                f.write("<tr>\n")
                f.write("<td>"+ str(contadorerror) + "</td>\n")
                f.write("<td>"+ str(rowerror[i]) + "</td>\n")
                f.write("<td>"+ str(colerror[i]) + "</td>\n")
                f.write("<td>"+ error[i] + "</td>\n")
                f.write("</tr>\n")
                contadorerror = contadorerror + 1

            f.write("</table>\n")
            f.write("</body>\n")
            f.write("</html>\n")
            f.close() 
            print('Reporte creado')

            contador = 0
            for i in range(len(token)):
                if token[i] == "COMENTARIO" and contador < 2:
                    print(lexeme[i])
                    nuevadir = lexeme[i].split("//")
                    print(nuevadir[1])
                    if nuevadir[1].lower().find("pathw") >=0:
                        path = nuevadir[1].lower().split("pathw:")
                        path = path[1].strip()
                        print("Path: " + path)


                    contador = contador +1

            if os.path.isdir(path):
                print('La carpeta existe.')
            else:
                print('Creando carpeta...')
                os.makedirs(path)
            f= open(path+nombrearchivo[-1],"w+")
            for i in range(len(token)):
                #f.write(token[i] + " " + lexeme[i] + "\n")
                f.write(lexeme[i])
            f.close()
            print('Archivo creado')

        elif tipoarchivo[1] == "css":
            print("Analizando archivo de CSS")

             # Lists for every list returned list from the function tokenize
            token = []
            lexeme = []
            row = []
            column = []
            error = []
            rowerror = []
            colerror = []
            #bitacoratoken = []
            #bitacoralexeme = []
 
            # Tokenize and reload of the buffer
            #entrada = 'program.c'
            for i in Buffer.load_buffer(archivo):
                t, lex, lin, col, e, re, ce = Analyzer.tokenizecss(i)
                token += t
                lexeme += lex
                row += lin
                column += col
                error += e
                rowerror += re
                colerror += ce
                #bitacoratoken += bitt
                #bitacoralexeme += bitl

        
            print('\nRecognize Tokens: ', token)
            Analyzer.lin_num = 1

            #for i in range(len(bitacoratoken)):
                #if bitacoratoken[i] == "ID":
            consola.insert(INSERT, "############## BITACORA CSS##############" + "\n")
            bitacora(archivo)

            f= open("Errorescss.html","w+")

            f.write("<html>\n")
            f.write("<head>\n")
            f.write("<title>Reporte errores css</title>\n")
            f.write("</head>\n")
            f.write("<body>\n")
            f.write("<h1 >Reporte Errores CSS</h1>\n")
            f.write("<table border=\"1\">\n")
            f.write("<tr>\n")
            f.write("<td> No. </td>\n")
            f.write("<td> Fila </td>\n")
            f.write("<td> Columna </td>\n")
            f.write("<td> Error </td>\n")
            f.write("</tr>\n")

            contadorerror = 1
            for i in range(len(error)):
                f.write("<tr>\n")
                f.write("<td>"+ str(contadorerror) + "</td>\n")
                f.write("<td>"+ str(rowerror[i]) + "</td>\n")
                f.write("<td>"+ str(colerror[i]) + "</td>\n")
                f.write("<td>"+ error[i] + "</td>\n")
                f.write("</tr>\n")
                contadorerror = contadorerror + 1

            f.write("</table>\n")
            f.write("</body>\n")
            f.write("</html>\n")
            f.close() 
            print('Reporte creado')

            contador = 0
            for i in range(len(token)):
                if token[i] == "COMENTARIO" and contador < 2:
                    #print(lexeme[i])
                    nuevadir = lexeme[i].split("*")
                    #print(nuevadir[1])
                    if nuevadir[1].lower().find("pathw") >=0:
                        path = nuevadir[1].lower().split("pathw:")
                        path = path[1].strip()
                        print(path)


                    contador = contador +1

            if os.path.isdir(path):
                print('La carpeta existe.')
            else:
                print('Creando carpeta...')
                os.makedirs(path)
            f= open(path+nombrearchivo[-1],"w+")
            i=0
            while i < len(token):
                #f.write(token[i] + " " + lexeme[i] + "\n")
                if token[i]=="INTEGER_CONST" or token[i]=="FLOAT_CONST" :
                    #print(i)
                    lexema = lexeme[i]
                    j = i+1
                    while j < len(token):
                        if lexeme[j].lower() == 'color' or lexeme[j].lower() == 'border-style' or lexeme[j].lower() == 'border' or lexeme[j].lower() == 'text-allign' or lexeme[j].lower() == 'font-weight' or lexeme[j].lower() == 'padding-left' or lexeme[j].lower() == 'padding-top' or lexeme[j].lower() == 'line-height' or lexeme[j].lower() == 'margin-top' or lexeme[j].lower() == 'margin-left' or lexeme[j].lower() == 'display' or lexeme[j].lower() == 'top' or lexeme[j].lower() == 'float' or lexeme[j].lower() == 'min-width' or lexeme[j].lower() == 'background-color' or lexeme[j].lower() == 'opacity' or lexeme[j].lower() == 'font-family' or lexeme[j].lower() == 'font-size' or lexeme[j].lower() == 'padding-right' or lexeme[j].lower() == 'width' or lexeme[j].lower() == 'margin-right' or lexeme[j].lower() == 'position' or lexeme[j].lower() == 'right' or lexeme[j].lower() == 'clear' or lexeme[j].lower() == 'max-height' or lexeme[j].lower() == 'background-image' or lexeme[j].lower() == 'background' or lexeme[j].lower() == 'font-style' or lexeme[j].lower() == 'font' or lexeme[j].lower() == 'padding-bottom' or lexeme[j].lower() == 'padding' or lexeme[j].lower() == 'display' or lexeme[j].lower() == 'height' or lexeme[j].lower() == 'margin-bottom' or lexeme[j].lower() == 'margin' or lexeme[j].lower() == 'bottom' or lexeme[j].lower() == 'left' or lexeme[j].lower() == 'max-width' or lexeme[j].lower() == 'min-height' or lexeme[j].lower() == 'rgba' or lexeme[j].lower() == 'url':

                            print("Eliminando Error")
                            #print(j)
                            f.write(lexeme[j])
                            i = j
                            j = len(token)
                            #print(j)
                        else:
                            f.write(lexema)
                            f.write(lexeme[j])
                            i = j
                            j = len(token)
                        j=j+1

                else:
                    f.write(lexeme[i])
                i=i+1
            f.close()
            print('Archivo creado')

        elif tipoarchivo[1] == "html":
            print("Analizando archivo de HTML")

            # Lists for every list returned list from the function tokenize
            token = []
            lexeme = []
            row = []
            column = []
            tokenerror = []
            lexemeerror = []
 
            # Tokenize and reload of the buffer
            #entrada = 'program.c'
            for i in Buffer.load_buffer(archivo):
                t, lex, lin, col, te, le = Analyzer.tokenizehtml(i)
                token += t
                lexeme += lex
                row += lin
                column += col
                tokenerror += te
                lexemeerror += le


        
            print('\nRecognize Tokens: ', token)
            Analyzer.lin_num = 1

            contador = 0
            for i in range(len(token)):
                if token[i] == "COMENTARIO" and contador < 2:
                    #print(lexeme[i])
                    nuevadir = lexeme[i].split("--")
                    #print(nuevadir[1])
                    if nuevadir[1].find("pathw") >=0:
                        path = nuevadir[1].split("pathw:")
                        path = path[1].strip()
                        print(path)


                    contador = contador +1

            if os.path.isdir(path):
                print('La carpeta existe.')
            else:
                print('Creando carpeta...')
                os.makedirs(path)
            f= open(path+nombrearchivo[-1],"w+")

            i = 0
            while i < len(token):
                #f.write(token[i] + " " + lexeme[i] + "\n")
                if token[i] == "MENOR_QUE":
                    f.write(lexeme[i])
                    #print(i)
                    j = i+1
                    while j < len(token):
                        if token[j] == "MAYOR_QUE":
                            f.write(lexeme[j])
                            #print(j)
                            i = j
                            j = len(token)
                            #print(j)
                        elif token[j] == "OTROS_SIMBOLOS":
                            print("Eliminando Errores")
                            #print(j)
                        else:
                            f.write(lexeme[j])
                        j=j+1

                else:
                    f.write(lexeme[i])
                #f.write(lexeme[i])
                i = i+1
            
                
            f.close() 
            print('Archivo creado')

            f= open("Erroreshtml.html","w+")

            f.write("<html>\n")
            f.write("<head>\n")
            f.write("<title>Reporte errores html</title>\n")
            f.write("</head>\n")
            f.write("<body>\n")
            f.write("<h1 >Reporte Errores HTML</h1>\n")
            f.write("<table border=\"1\">\n")
            f.write("<tr>\n")
            f.write("<td> No. </td>\n")
            f.write("<td> Fila </td>\n")
            f.write("<td> Columna </td>\n")
            f.write("<td> Error </td>\n")
            f.write("</tr>\n")

            contadorerror = 1
            i = 0
            while i < len(tokenerror):
                #f.write(token[i] + " " + lexeme[i] + "\n")
                if tokenerror[i] == "MENOR_QUE":
                    #print(i)
                    j = i+1
                    while j < len(tokenerror):
                        if tokenerror[j] == "MAYOR_QUE":
                            #print(j)
                            i = j
                            j = len(tokenerror)
                            #print(j)
                        elif tokenerror[j] == "OTROS_SIMBOLOS":

                            f.write("<tr>\n")
                            f.write("<td>"+ str(contadorerror) + "</td>\n")
                            f.write("<td>"+ str(row[j]) + "</td>\n")
                            f.write("<td>"+ str(column[j]) + "</td>\n")
                            f.write("<td>"+ lexemeerror[j] + "</td>\n")
                            f.write("</tr>\n")
                            contadorerror = contadorerror + 1
                            
                            #print(j)
                        
                        j=j+1

                
                i = i+1

            f.write("</table>\n")
            f.write("</body>\n")
            f.write("</html>\n")
            f.close() 
            print('Reporte creado')
        
        elif tipoarchivo[1] == "rmt":
            print("Analizando archivo Rmt")

            p = Pila()

            # Lists for every list returned list from the function tokenize
            token = []
            lexeme = []
            row = []
            column = []
 
            # Tokenize and reload of the buffer
            #entrada = 'program.c'
            for i in Buffer.load_buffer(archivo):
                t, lex, lin, col = Analyzer.tokenizermt(i)
                token += t
                lexeme += lex
                row += lin
                column += col

        
            print('\nRecognize Tokens: ', token)
            Analyzer.lin_num = 1

            f= open("Reportesintactico.html","w+")

            f.write("<html>\n")
            f.write("<head>\n")
            f.write("<title>Reporte sintactico</title>\n")
            f.write("</head>\n")
            f.write("<body>\n")
            f.write("<h1 >Reporte Sintactico</h1>\n")
            f.write("<table border=\"1\">\n")
            f.write("<caption>Expresiones</caption>\n")
            

            i = 0
            expresion = ""
            estado = ""
            estadolexico = ""
            while i < len(token):
                #f.write(token[i] + " " + lexeme[i] + "\n")
                if token[i] == "NEWLINE":
                    print("Nueva expresion")
                    #f.write(lexeme[i])
                    if p.estaVacia() is True and estado == "" and estadolexico == "":
                        #print("pila vacia, correcto")
                        estado = "Correcto"
                    elif p.estaVacia() is True and estado == "" and estadolexico == "Error":
                        #print("pila vacia, correcto")
                        estado = "Incorrecto"
                    elif p.estaVacia() is False:
                        estado = "Incorrecto"


                    f.write("<tr>\n")
                    f.write("<td>"+ expresion + "</td>\n")
                    f.write("<td>"+ estado + "</td>\n")
                    f.write("</tr>\n")
                    expresion = ""
                    estado = ""
                    estadolexico=""

                    while p.estaVacia() is False:
                        p.extraer()

                elif token[i] == "SKIP":
                    print("Ignorar")

                elif token[i] == "MISMATCH":
                    estadolexico = "Error"
                    expresion = expresion + " " + lexeme[i]

                else:
                    #f.write(lexeme[i])
                    expresion = expresion + " " + lexeme[i]

                    if token[i] == "PARENTESIS_IZQ":
                        #print("Agregando a pila")
                        p.incluir("(")
                    elif token[i] == "PARENTESIS_DER":
                        #print(p.tamano())
                        #print("Removiendo en pila")
                        if p.estaVacia() is True:
                            #print("pila vacia, error")
                            estado = "Incorrecto"
                        else:
                            #print("pila llena, se ha removido")
                            p.extraer()
                            

                i = i+1

            if p.estaVacia() is True and estado == "" and estadolexico == "":
                #print("pila vacia, correcto")
                estado = "Correcto"
            elif p.estaVacia() is True and estado == "" and estadolexico == "Error":
                #print("pila vacia, correcto")
                estado = "Incorrecto"
            elif p.estaVacia() is False:
                estado = "Incorrecto"

            while p.estaVacia() is False:
                p.extraer()

            f.write("<tr>\n")
            f.write("<td>"+ expresion + "</td>\n")
            f.write("<td>"+ estado + "</td>\n")
            f.write("</tr>\n")
            expresion = ""
            estado = ""
            estadolexico=""

            f.write("</table>\n")
            f.write("</body>\n")
            f.write("</html>\n")
            f.close() 
            print('Archivo creado')
            #print(p.inspeccionar())
            #print(p.tamano())

        
        else:
            print("No se ha podido ejecutar el analisis, Archivo no soportado")

def bitacora(entrada):
    expresiones = open(entrada)
    linea = [" "]
    #impresion = ''
    while linea != '':
        #Leer linea a linea del .txt
        linea = expresiones.readline().split(' ')
        #print(linea)
        if linea == ['']:
            expresiones.close()
            break
        #Resultado para el archivo
        #' '.join() une los elementos 
        #linea[:-1] todos menos el ultimo elemento
            
        #impresion += "La respuesta para ["+' '.join(linea)+"] es: "'\n'
        #impresion += self.describir_lexico(' '.join(linea))
        describir_bitacora(' '.join(linea))

def describir_bitacora(elementos):
    #Tomar elemento por elemento
        elemento = elementos
        #print(elemento)
        #print(len(elementos))
        #print(elemento[len(elemento) - 1])
        #caracteres = elementos.split(' ')
        i = 0
        #impresion = ""
        
        while i < len(elemento):
            #print(elemento[i])
            #Si es un numero
            if elemento[i].isdigit():
                consola.insert(INSERT, "Caracter: " + elemento[i] + " Transicion a estado: 1 " + "\n")
                start = elemento[i]
                end=""
                j=i+1
                while j < len(elemento):
                    if elemento[j].isdigit():
                        consola.insert(INSERT, "Caracter: " + elemento[j] + " Transicion a estado: 1 " + "\n")
                        end = end + elemento[j]
                    elif elemento[j] == ".":
                        consola.insert(INSERT, "Caracter: " + elemento[j] + " Transicion a estado: 6 " + "\n")
                        punto = elemento[j]
                        k=j+1
                        if elemento[k].isdigit():
                            consola.insert(INSERT, "Caracter: " + elemento[k] + " Transicion a estado: 7 " + "\n")
                            end = end + punto + elemento[k]
                            k = k+1
                            while k < len(elemento):
                                if elemento[k].isdigit():
                                    consola.insert(INSERT, "Caracter: " + elemento[k] + " Transicion a estado: 7 " + "\n")
                                    end = end + elemento[k]

                                else:
                                    consola.insert(INSERT, "Estado 7 - Token NUMERO DECIMAL aceptado - Lexema: " +  start + end + "\n")
                                    #impresion += start + end +" es un numero"'\n'
                                    #print("numero")
                                    i=k-1
                                    j=len(elemento)
                                    k=len(elemento)
                        
                                k=k+1
                        else:
                            consola.insert(INSERT, "Estado 1 - Token NUMERO aceptado - Lexema: " +  start + end + "\n")
                            consola.insert(INSERT, "Caracter: " + punto  + " Transicion a estado: 0 " + "\n")
                            i = k -2
                            j=len(elemento)
                       
                    else:
                        consola.insert(INSERT, "Estado 1 - Token NUMERO aceptado - Lexema: " +  start + end + "\n")
                        #impresion += start + end +" es un numero"'\n'
                        #print("numero")
                        i = j-1
                        j=len(elemento)
                        
                    j=j+1
                        
            
            #Si es una variable (minusculas)
            elif elemento[i].isalpha():
                consola.insert(INSERT, "Caracter: " + elemento[i] + " Transicion a estado: 2 " + "\n")
                start = elemento[i]
                end = ""
                j=i+1
                while j < len(elemento):
                    if elemento[j].isalpha() or elemento[j].isdigit() or elemento[j] == "-":
                        consola.insert(INSERT, "Caracter: " + elemento[j] + " Transicion a estado: 3 " + "\n")
                        end = end + elemento[j]
                    else:
                        #impresion += start + end +" es un id"'\n'
                        #print("id")
                        consola.insert(INSERT, "Estado 3 - Token ID aceptado - Lexema: " +  start + end + "\n")
                        i = j-1
                        j=len(elemento)
                        
                    j=j+1
            elif elemento[i] == "\"":
                consola.insert(INSERT, "Caracter: " + elemento[i] + " Transicion a estado: 4 " + "\n")
                start = elemento[i]
                end = ""
                j=i+1
                while j < len(elemento):
                    if elemento[j] == "\"":
                        #impresion += start + end + elemento[j] + " es una cadena"'\n'
                        consola.insert(INSERT, "Caracter: " + elemento[j] + " Transicion a estado: 5 " + "\n")
                        consola.insert(INSERT, "Estado 5 - Token CADENA aceptado - Lexema: " +  start + end + elemento[j] + "\n")
                        i = j
                        j=len(elemento)
                        
                    else:
                        consola.insert(INSERT, "Caracter: " + elemento[j] + " Transicion a estado: 4 " + "\n")
                        end = end + elemento[j]
                        
                        #print("id")
                        
                        
                    j=j+1

            
            elif elemento[i] == "/":
                consola.insert(INSERT, "Caracter: " + elemento[i] + " Transicion a estado: 8 " + "\n")
                start = elemento[i]
                end = ""
                j=i+1
                if elemento[j] == "*":
                    consola.insert(INSERT, "Caracter: " + elemento[j] + " Transicion a estado: 9 " + "\n")
                    end = end + elemento[j]
                    j=j+1
                    while j < len(elemento):
                        if elemento[j] == "*":
                            #impresion += start + elemento[j] + " es un comentario"'\n'
                            consola.insert(INSERT, "Caracter: " + elemento[j] + " Transicion a estado: 10 " + "\n")
                            end = end + elemento[j]
                            k=j+1
                            if elemento[k] == "/":
                                consola.insert(INSERT, "Caracter: " + elemento[k] + " Transicion a estado: 11" + "\n")
                                consola.insert(INSERT,"Estado 12 - Token COMENTARIO aceptado - Lexema: " +  start + end + elemento[k] + "\n")
                                i=k
                                j=len(elemento)
                        
                        else:
                            #impresion += start + "diagonal"'\n'
                            consola.insert(INSERT, "Caracter: " + elemento[j] + " Transicion a estado: 9 " + "\n")
                            end = end + elemento[j]
                            i=j
                        
                        j=j+1
                else:
                    consola.insert(INSERT, "Estado 8 - Token SIMBOLO aceptado - Lexema: " +  elemento[i] + "\n")

            #Si es un operador (+-*/)
            elif elemento[i] == "-" or elemento[i] == "{" or elemento[i] == "}" or elemento[i] == ":" or elemento[i] == ";" or elemento[i] == "*" or elemento[i] == "#" or elemento[i] == "," or elemento[i] == "." or elemento[i] == "%" or elemento[i] == "(" or elemento[i] == ")":
                #impresion += elemento[i]+" es un operador"'\n'
                consola.insert(INSERT, "Estado 0 - Token SIMBOLO aceptado - Lexema: " +  elemento[i] + "\n")
                #print("operador")

            elif elemento[i] == " ":
                print("ignorar")
            elif elemento[i] == "\n":
                print("ignorar")
            elif elemento[i] == "\t":
                print("ignorar")
                
            else:
                #print(i)
                consola.insert(INSERT, "Error lexico - Caracter: " +  elemento[i] + "\n")
                #print("error")
            #print(i)
            i += 1
            #print(i) 

barraMenu = Menu(root)
root.config(menu = barraMenu, width = 1000, height = 600)

archivoMenu = Menu(barraMenu, tearoff=0)
archivoMenu.add_command(label = "Nuevo", command = nuevo)
archivoMenu.add_command(label = "Abrir", command = abrir)
archivoMenu.add_command(label = "Guardar", command = guardarArchivo)
archivoMenu.add_command(label = "Guardar Como...", command = guardarComo)
archivoMenu.add_separator()
archivoMenu.add_command(label = "Salir", command = salir)

reporteMenu = Menu(barraMenu, tearoff=0)
reporteMenu.add_command(label = "AFD JS", command = afdjs)
reporteMenu.add_command(label = "Errores JS", command = erroresjs)
reporteMenu.add_command(label = "Errores CSS", command = errorescss)
reporteMenu.add_command(label = "Errores HTML", command = erroreshtml)
reporteMenu.add_command(label = "Sintactico", command = reportesin)


barraMenu.add_cascade(label = "Archivo", menu = archivoMenu)
barraMenu.add_command(label = "Analizar",  command = ejecutar)
barraMenu.add_cascade(label = "Reportes",  menu = reporteMenu)
barraMenu.add_command(label = "Salir",  command = salir)

frame = Frame(root, bg="gray")
canvas = Canvas(frame, bg="gray")
scrollbar = Scrollbar(frame, orient=VERTICAL, command=canvas.yview)
scroll = Frame(canvas, bg="gray")

scroll.bind("<Configure>",lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

canvas.create_window((0, 0), window=scroll, anchor="nw")

canvas.configure(yscrollcommand=scrollbar.set, width = 800, height = 700)

ttk.Label(scroll, text = "Editor de texto", font = ("Arial", 17), background='gray', foreground = "black").grid(column = 1, row = 0)

editor = scrolledtext.ScrolledText(scroll, undo = True, width = 60, height = 15, font = ("Arial", 12), background = 'white',  foreground = "black")

editor.grid(column = 1, row = 1, pady = 25, padx = 125)

consola = scrolledtext.ScrolledText(scroll, undo = True, width = 60, height = 15, font = ("Arial", 12), background = 'black',  foreground = "white")

consola.grid(column = 1, row = 2, pady = 25, padx = 125)

frame.grid(sticky='news')
canvas.grid(row=0,column=1)
scrollbar.grid(row=0, column=2, sticky='ns')


editor.focus()
root.mainloop()
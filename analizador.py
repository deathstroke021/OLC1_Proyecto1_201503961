from tkinter import Tk, Menu, messagebox, filedialog, ttk, Label, scrolledtext, INSERT, END, Button, Scrollbar, RIGHT, Y, Frame, Canvas, HORIZONTAL, VERTICAL, simpledialog
from Buffer import Buffer
from LexicalAnalyzer import LexicalAnalyzer
from pila import Pila
import os

root = Tk()
root.title("Analizador")
root.configure(background = "gray")

'''FUNCIONES DEL MENU'''

archivo = ""

Buffer = Buffer()
Analyzer = LexicalAnalyzer()

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
    consola.insert(INSERT, "Prueba", "start")

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
 
            # Tokenize and reload of the buffer
            #entrada = 'program.c'
            for i in Buffer.load_buffer(archivo):
                t, lex, lin, col = Analyzer.tokenizejs(i)
                token += t
                lexeme += lex
                row += lin
                column += col

        
            print('\nRecognize Tokens: ', token)
            Analyzer.lin_num = 1

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
 
            # Tokenize and reload of the buffer
            #entrada = 'program.c'
            for i in Buffer.load_buffer(archivo):
                t, lex, lin, col = Analyzer.tokenizecss(i)
                token += t
                lexeme += lex
                row += lin
                column += col

        
            print('\nRecognize Tokens: ', token)
            Analyzer.lin_num = 1

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
 
            # Tokenize and reload of the buffer
            #entrada = 'program.c'
            for i in Buffer.load_buffer(archivo):
                t, lex, lin, col = Analyzer.tokenizehtml(i)
                token += t
                lexeme += lex
                row += lin
                column += col

        
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
            while i < len(token):
                #f.write(token[i] + " " + lexeme[i] + "\n")
                if token[i] == "NEWLINE":
                    print("Nueva expresion")
                    #f.write(lexeme[i])
                    if p.estaVacia() is True and estado == "":
                        #print("pila vacia, correcto")
                        estado = "Correcto"
                    elif p.estaVacia() is False:
                        estado = "Error"


                    f.write("<tr>\n")
                    f.write("<td>"+ expresion + "</td>\n")
                    f.write("<td>"+ estado + "</td>\n")
                    f.write("</tr>\n")
                    expresion = ""
                    estado = ""

                    while p.estaVacia() is False:
                        p.extraer()

                elif token[i] == "SKIP":
                    print("Ignorar")

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
                            estado = "Error"
                        else:
                            #print("pila llena, se ha removido")
                            p.extraer()
                            

                i = i+1

            if p.estaVacia is True and estado == "":
                #print("pila vaica, correcto")
                estado = "Correcto"
            elif p.estaVacia() is False:
                estado = "Error"

            while p.estaVacia() is False:
                p.extraer()

            f.write("<tr>\n")
            f.write("<td>"+ expresion + "</td>\n")
            f.write("<td>"+ estado + "</td>\n")
            f.write("</tr>\n")
            expresion = ""
            estado = ""

            f.write("</table>\n")
            f.write("</body>\n")
            f.write("</html>\n")
            f.close() 
            print('Archivo creado')
            #print(p.inspeccionar())
            #print(p.tamano())

        
        else:
            print("No se ha podido ejecutar el analisis, Archivo no soportado")

barraMenu = Menu(root)
root.config(menu = barraMenu, width = 1000, height = 600)

archivoMenu = Menu(barraMenu, tearoff=0)
archivoMenu.add_command(label = "Nuevo", command = nuevo)
archivoMenu.add_command(label = "Abrir", command = abrir)
archivoMenu.add_command(label = "Guardar", command = guardarArchivo)
archivoMenu.add_command(label = "Guardar Como...", command = guardarComo)
archivoMenu.add_separator()
archivoMenu.add_command(label = "Salir", command = salir)


barraMenu.add_cascade(label = "Archivo", menu = archivoMenu)
barraMenu.add_command(label = "Analizar",  command = ejecutar)
barraMenu.add_command(label = "Reportes",  command = salir)
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
from tkinter import Tk, Menu, messagebox, filedialog, ttk, Label, scrolledtext, INSERT, END, Button, Scrollbar, RIGHT, Y, Frame, Canvas, HORIZONTAL, VERTICAL, simpledialog
from Buffer import Buffer
from LexicalAnalyzer import LexicalAnalyzer

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
    entrada.close()

    consola.insert(INSERT, "Abriendo archivo " + archivo + "\n")

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

    print("Ejecutando Analisis Lexico...")

    if archivo == "":
        print("No hay archivos para analizar, guarde el archivo para continuar")

    else:

        tipoarchivo = archivo.split(".")
        print("Extension archivo: " + tipoarchivo[1])


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

        elif tipoarchivo[1] == "css":
            print("Analizando archivo de CSS")

             # Lists for every list returned list from the function tokenize
            token = []
            lexeme = []
            row = []
            column = []
 
            # Tokenize and reload of the buffer
            #entrada = 'program.c'
            for i in Buffer.load_buffer2(archivo):
                t, lex, lin, col = Analyzer.tokenizecss(i)
                token += t
                lexeme += lex
                row += lin
                column += col

        
            print('\nRecognize Tokens: ', token)
            Analyzer.lin_num = 1

        elif tipoarchivo[1] == "html":
            print("Analizando archivo de HTML")

            # Lists for every list returned list from the function tokenize
            token = []
            lexeme = []
            row = []
            column = []
 
            # Tokenize and reload of the buffer
            #entrada = 'program.c'
            for i in Buffer.load_buffer2(archivo):
                t, lex, lin, col = Analyzer.tokenizehtml(i)
                token += t
                lexeme += lex
                row += lin
                column += col

        
            print('\nRecognize Tokens: ', token)
            Analyzer.lin_num = 1
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
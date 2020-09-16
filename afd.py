# -*- coding: utf-8 -*-

class afd:

    contadornumero = 0
    contadorid = 0
    contadorcadena = 0

    """ AGREGAR ELEMENTOS A LA COLA """
    def abrir_archivo(self, entrada):
        #Abrir .txt con expresiones aritmeticas
        expresiones = open(entrada)
        linea = [" "]
        impresion = ''
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
            
            impresion += "La respuesta para ["+' '.join(linea)+"] es: "'\n'
            impresion += self.describir_lexico(' '.join(linea))
            #print("JOIN" + ' '.join(linea))

        self.afdgraficar()

        return impresion

    """ AGREGAR EL RESULTADO AL ARCHIVO """   
    def escribir_archivo(self,resultado):
        busquedas = open("resultados.txt", "w")
        busquedas.write(resultado)
        busquedas.close()

    """ DETERMINAR EL TIPO DE CARACTER (LEXICO) """
    #El lexico solo acepta numeros, operadores y variables (en minuscula)
    def describir_lexico(self,elementos):
        #Tomar elemento por elemento
        elemento = elementos
        #print(elemento)
        #print(len(elementos))
        #print(elemento[len(elemento) - 1])
        #caracteres = elementos.split(' ')
        i = 0
        impresion = ""
        while i < len(elemento):
            #print(elemento[i])
            #Si es un numero
            if elemento[i].isdigit():
                start = elemento[i]
                end = ""
                j=i+1
                while j < len(elemento):
                    if elemento[j].isdigit():
                        end = end + elemento[j]
                    else:
                        impresion += start + end +" es un numero"'\n'

                        if self.contadornumero == 0:
                            print("Graficar AFD numero")
                            
                            
                            self.contadornumero = 1
                        else:
                            print("AFD numero ya graficado")
                        #print("numero")
                        i = j-1
                        j=len(elemento)
                        
                    j=j+1
                        
            #Si es un operador (+-*/)
            elif elemento[i] == "*" or elemento[i] == "+" or elemento[i] == "-":
                impresion += elemento[i]+" es un operador"'\n'
                #print("operador")
            #Si es una variable (minusculas)
            elif elemento[i].isalpha():
                start = elemento[i]
                end = ""
                j=i+1
                while j < len(elemento):
                    if elemento[j].isalpha() or elemento[j].isdigit() or elemento[j] == "_":
                        end = end + elemento[j]
                    else:
                        impresion += start + end +" es un id"'\n'
                        #print("id")
                        if self.contadorid == 0:
                            print("Graficar AFD id")
                            self.contadorid = 1
                        else:
                            print("AFD id ya graficado")

                        i = j-1
                        j=len(elemento)
                        
                    j=j+1
            elif elemento[i] == "\"":
                start = elemento[i]
                end = ""
                j=i+1
                while j < len(elemento):
                    if elemento[j] == "\"":
                        impresion += start + end + elemento[j] + " es una cadena"'\n'

                        if self.contadorcadena == 0:
                            print("Graficar AFD cadena")
                            self.contadorcadena = 1
                        else:
                            print("AFD cadena ya graficado")
                        
                        i = j
                        j=len(elemento)
                        
                    else:
                        end = end + elemento[j]
                        
                        #print("id")
                        
                        
                    j=j+1

            elif elemento[i] == "'":
                start = elemento[i]
                end = ""
                j=i+1
                while j < len(elemento):
                    if elemento[j] == "'":
                        impresion += start + end + elemento[j] + " es una cadena tipo 2"'\n'
                        i = j
                        j=len(elemento)
                        
                    else:
                        end = end + elemento[j]
                        
                        #print("id")
                        
                        
                    j=j+1
            elif elemento[i] == "/":
                start = elemento[i]
                j=i+1
                while j < len(elemento):
                    if elemento[j] == "/":
                        impresion += start + elemento[j] + " es un comentario"'\n'
                        
                        j=len(elemento)
                        i = j
                        
                    else:
                        impresion += start + "diagonal"'\n'
                        i=j-1
                        j=len(elemento)
                        
                    j=j+1

            elif elemento[i] == " ":
                print("ignorar")
            else:
                #print(i)
                impresion += elemento[i]+" no se reconoce"'\n'
                #print("error")
            #print(i)
            i += 1
            #print(i) 
        return impresion

    def afdgraficar(self):
        f= open("AFD.dot","w+")
        f.write("digraph automata_finito {\n")
        f.write("rankdir=LR;\n")
        f.write("graph [label=\"AFD\", labelloc=t, fontsize=20]; \n")
        f.write("node [shape=doublecircle, style = filled,color = mediumseagreen]; 0;\n")
        f.write("edge [color=red];\n")
        f.write("secret_node [style=invis];\n")
        f.write("secret_node -> 0 [label=\"inicio\"];\n")
        if self.contadornumero == 1:
            f.write("node [shape=circle];\n")
            f.write("node [color=midnightblue,fontcolor=white]; 1;\n")
            f.write("0 -> 1 [label=\"numero\"];\n")
            f.write("1 -> 1 [label=\"numero\"];\n")
        if self.contadorid == 1:
            f.write("node [shape=doublecircle, style = filled,color = mediumseagreen]; 2;\n")
            f.write("node [shape=circle];\n")
            f.write("node [color=midnightblue,fontcolor=white]; 3;\n")
            f.write("0 -> 2 [label=\"letra\"];\n")
            f.write("2 -> 3 [label=\"letra|numero|_\"];\n")
            f.write("3 -> 3 [label=\"letra|numero|_\"];\n")
        if self.contadorcadena == 1:
            f.write("node [shape=doublecircle, style = filled,color = mediumseagreen]; 4,5;\n")
            f.write("node [shape=circle];\n")
            f.write("node [color=midnightblue,fontcolor=white]; 6;\n")
            f.write("0 -> 4 [label=\"\\\"\"];\n")
            f.write("4 -> 5 [label=\"todo\"];\n")
            f.write("5 -> 6 [label=\"\\\"\"];\n")

        f.write("}")
        f.close
        
    
    
"""inicio = afd()
salida = inicio.abrir_archivo("expresiones.txt")
inicio.escribir_archivo(salida)"""

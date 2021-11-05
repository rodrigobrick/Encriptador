from os.path import join
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog as fd
from funciones import *
from time import time
#---------METODOS---------------------------------
from cifrado_cesar import *
from AES import *
from pydes import des
from BLOWFISH import *
from des3 import *
#--------------------INTERFAZ----------------------

raiz=tk.Tk()
raiz.title("Encriptador/Desencriptador de mensajes")
raiz.resizable(0,0)  
#raiz.iconbitmap('C:\Users\Main-user\Desktop\programita\dron.ico')
#raiz.iconphoto(True,tk.PhotoImage(file='icons/icono.png'))
raiz.geometry("800x600+500+300")

def inicio():  #ACA VA LA CONFORMACION DE LA INTERFAZ GRAFICA
    titulo1 = tk.Entry(raiz)
    titulo1 = Label(raiz, text="ENCRIPTADOR/DESENCRIPTADOR DE MENSAJES", font=("OCR A Extended", 18))
    titulo1.grid(row=1, column=1, padx=0, pady=50) 

    labelMensaje = Label(raiz, text="Mensaje: ", font= ("OCR A Extended", 12))
    labelMensaje.grid(row=2, column=0, padx=10, pady=10)
    mensaje = tk.StringVar()
    entradaMensaje = tk.Entry(raiz, width=80, justify=tk.LEFT, textvariable = mensaje)
    entradaMensaje.grid(row=2, column=1)

    labelOpcion = Label(raiz, text="Opcion: ",font=("OCR A Extended",12))
    labelOpcion.grid(row=3,column=0, padx=0, pady=20)
    ComboBoxOpcion= ttk.Combobox(raiz, state = "readonly", values =["ENCRIPTAR","DESENCRIPTAR"])
    ComboBoxOpcion.place(x=143,y=195)
    ComboBoxOpcion.current(0)

    labelMetodo = Label(raiz, text="Metodo: ", font=("OCR A Extended", 12))
    labelMetodo.grid(row=3, column=1,padx=10, pady=20)
    ComboBoxMetodos = ttk.Combobox(raiz, state = "readonly", values=["CIFRADO DEL CESAR","AES","DES","3DES","BLOWFISH"])
    ComboBoxMetodos.place(x=485, y=195)
    ComboBoxMetodos.current(0)

    labelLlave = Label(raiz, text="Llave: ", font = ("OCR A Extended",12))
    labelLlave.grid(row=4,column=0, padx=0, pady=20)
    llave = tk.StringVar()
    entradaLlave = tk.Entry(raiz, width=80, justify=tk.LEFT, textvariable=llave)
    entradaLlave.grid(row=4, column=1)

    BotonFuncion = Button(raiz,text="INICIAR",font=("OCR A Extended",18),
    command = lambda:Iniciar_proceso( mensaje.get(), resultado, ComboBoxOpcion.get(), ComboBoxMetodos.get(), llave.get()) )
    BotonFuncion.grid(row=5, column=1, padx=0, pady=20)

    labelResultado = Label(raiz, text="Resultado: ", font=("OCR A Extended",12))
    labelResultado.grid(row=6, column=0, padx=0, pady=20)
    resultado = tk.StringVar()
    entradaResultado = tk.Entry(raiz, width=80, state="readonly", textvariable=resultado)
    entradaResultado.grid(row=6, column=1, padx=0, pady=20)
    BotonCopiar = Button(raiz, text="Copiar", command= lambda:CopiarDatos(resultado.get()))
    BotonCopiar.place(x=650, y=400)

    BotonHistorial = Button(raiz,text="Mostrar Historial", command=abrir_historial)
    BotonHistorial.grid (row=9, column=1,padx=0, pady=50)

   
    raiz.mainloop()

aux= None

def Iniciar_proceso(mensaje, resultado, ComboBoxOpcion,ComboBoxMetodos, llave):
    if (mensaje!=""): 

        if (ComboBoxMetodos == "CIFRADO DEL CESAR"): #IF NECESARIO PARA QUITAR LA LLAVE DEL PROCEDIMIENTO
            if (ComboBoxOpcion == "ENCRIPTAR"):  #ENCRIPTADO METODO DEL CESAR
                start_time = time()
                auxEntrada = mensaje
                rotaciones = comprobar_rotacion(llave)
                auxResultado = codificar(auxEntrada,rotaciones)
                resultado.set(auxResultado)
                elapsed_time = time() - start_time
                registrar_info_cesar(auxEntrada, auxResultado, ComboBoxOpcion, ComboBoxMetodos, llave, elapsed_time)
                messagebox.showinfo(title= "Resultados finales", 
                message= muestra_msj_cesar(auxEntrada, auxResultado, ComboBoxOpcion, ComboBoxMetodos, llave, elapsed_time))
            else:        #DESENCRIPTADO METODO DEL CESAR
                start_time = time()
                auxEntrada = mensaje
                rotaciones = comprobar_rotacion(llave)
                auxResultado= decodificar(auxEntrada,rotaciones)
                resultado.set(auxResultado)
                elapsed_time = time() - start_time
                registrar_info_cesar(auxEntrada, auxResultado, ComboBoxOpcion, ComboBoxMetodos, llave, elapsed_time)
                messagebox.showinfo(title= "Resultados finales",
                message= muestra_msj_cesar(auxEntrada, auxResultado, ComboBoxOpcion, ComboBoxMetodos, llave, elapsed_time))
        
        if (ComboBoxMetodos == "AES"):
            if (ComboBoxOpcion == "ENCRIPTAR"):  #ENCRIPTADO METODO AES      
                start_time = time()
                auxEntrada = comprobar_mensaje(mensaje)
                auxLlave = AESCipher(comprobar_llave(llave))
                auxResultado = auxLlave.encrypt(auxEntrada)
                resultado.set(auxResultado)
                elapsed_time = time() - start_time
                registrar_info(auxEntrada, auxResultado, ComboBoxOpcion, ComboBoxMetodos, llave, elapsed_time)
                messagebox.showinfo(title= "Resultados finales",
                message= muestra_msj(auxEntrada, auxResultado, ComboBoxOpcion, ComboBoxMetodos,llave, elapsed_time))
                       
            else:
                start_time = time()
                auxEntrada = comprobar_mensaje(mensaje)
                auxLlave = AESCipher(comprobar_llave(llave))
                auxResultado = auxLlave.decrypt(auxEntrada)
                resultado.set(auxResultado)
                elapsed_time = time() - start_time
                registrar_info(auxEntrada, auxResultado, ComboBoxOpcion, ComboBoxMetodos, llave, elapsed_time)
                messagebox.showinfo(title= "Resultados finales",
                message= muestra_msj(auxEntrada, auxResultado, ComboBoxOpcion, ComboBoxMetodos,llave, elapsed_time))

        if (ComboBoxMetodos == "DES"):
            if (ComboBoxOpcion == "ENCRIPTAR"):    #ENCRIPTADO METODO DES
                start_time = time()
                auxEntrada = mensaje
                llave = comprobar_llave_DES(llave)
                d = des()
                auxResultado=d.encrypt(llave, auxEntrada, padding=True).encode("utf-8")
                global aux
                aux= d.encrypt(llave, auxEntrada, padding= True)
                resultado.set(auxResultado)
                elapsed_time = time() - start_time
                registrar_info(auxEntrada, auxResultado, ComboBoxOpcion, ComboBoxMetodos, llave, elapsed_time)
                messagebox.showinfo(title= "Resultados finales",
                message= muestra_msj(auxEntrada, str(auxResultado), ComboBoxOpcion, ComboBoxMetodos,llave, elapsed_time))
            else:                               #DESENCRIPTADO METODO DES
                start_time = time()
                auxEntrada = aux
                auxregistro = aux.encode("utf-8")
                llave = comprobar_llave_DES(llave)
                d = des()
                auxResultado= d.decrypt(llave, auxEntrada, padding=True)
                resultado.set(auxResultado)
                elapsed_time = time() - start_time
                registrar_info(auxEntrada, auxResultado, ComboBoxOpcion, ComboBoxMetodos, llave, elapsed_time)
                messagebox.showinfo(title= "Resultados finales",
                message= muestra_msj(auxregistro, str(auxResultado), ComboBoxOpcion, ComboBoxMetodos,llave, elapsed_time))   

        if (ComboBoxMetodos == "BLOWFISH"):
            if (ComboBoxOpcion == "ENCRIPTAR"):
                start_time = time()
                auxEntrada = comprobar_mensaje(mensaje)
                auxLlave = BlowfishCipher(comprobar_llave(llave))
                auxResultado = auxLlave.encrypt(auxEntrada)
                resultado.set(auxResultado)
                elapsed_time = time() - start_time
                registrar_info(auxEntrada, auxResultado, ComboBoxOpcion, ComboBoxMetodos, llave, elapsed_time)
                messagebox.showinfo(title= " Resultados finales",
                message=muestra_msj(auxEntrada, auxResultado, ComboBoxOpcion, ComboBoxMetodos,llave, elapsed_time))
            else:
                start_time = time()
                auxEntrada = comprobar_mensaje(mensaje)
                auxLlave = BlowfishCipher(comprobar_llave(llave))
                auxResultado = auxLlave.decrypt(auxEntrada)
                resultado.set(auxResultado)
                elapsed_time = time() - start_time
                registrar_info(auxEntrada, auxResultado, ComboBoxOpcion, ComboBoxMetodos, llave, elapsed_time)
                messagebox.showinfo(title= "Resultados finales",
                message= muestra_msj(auxEntrada, auxResultado, ComboBoxOpcion, ComboBoxMetodos,llave, elapsed_time))

        if (ComboBoxMetodos == "3DES"):
            if (ComboBoxOpcion == "ENCRIPTAR"):
                start_time = time()
                auxEntrada = mensaje
                auxLlave = llave
                auxResultado = encrypt3DES(auxLlave,auxEntrada)
                resultado.set(auxResultado)
                elapsed_time = time() - start_time
                registrar_info(auxEntrada, auxResultado, ComboBoxOpcion, ComboBoxMetodos, llave, elapsed_time)
                messagebox.showinfo(title= " Resultados finales",
                message=muestra_msj(auxEntrada, auxResultado, ComboBoxOpcion, ComboBoxMetodos,llave, elapsed_time))
            else:
                start_time = time()
                auxEntrada = mensaje
                auxLlave = llave
                auxResultado = decrypt3DES(auxLlave,auxEntrada)
                resultado.set(auxResultado)
                elapsed_time = time() - start_time
                registrar_info(auxEntrada, auxResultado, ComboBoxOpcion, ComboBoxMetodos, llave, elapsed_time)
                messagebox.showinfo(title= " Resultados finales",
                message=muestra_msj(auxEntrada, auxResultado, ComboBoxOpcion, ComboBoxMetodos,llave, elapsed_time))

    else:
        messagebox.showerror(title= "Error", message="El campo de mensaje esta vacio")
 

def CopiarDatos(resultado):
    raiz.clipboard_clear()
    raiz.clipboard_append(resultado)
    if (raiz.clipboard_get()==""):
        messagebox.showinfo(title= "Aviso:", message= "No hay nada para copiar")
    else:
        messagebox.showinfo(title= "Aviso", message= "Mensaje copiado con exito")

def abrir_historial():
    root = tk.Tk()
    root.title('Mostrando historial')
    root.geometry('650x400')
    root.resizable(0,0)
    texto = tk.Text(root)#, width= 100, height= 100)
    texto.grid(row=0, column=0, sticky='nsew')
    scrolltexto = Scrollbar(root,command=texto.yview)
    scrolltexto.grid(row=0, column=0, pady=10, sticky='nse')
    texto.config(yscrollcommand=scrolltexto.set)
    def abrir_archivo():
        tipos_archivos = ('text files','*.txt'),('All files', '*.*')
        f = fd.askopenfile(filetype=tipos_archivos)
        texto.insert('1.0', f.readlines())
    abrir_archivo()
    root.mainloop()

inicio()




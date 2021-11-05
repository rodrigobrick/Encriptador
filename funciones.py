#archivo para dejar funciones

from tkinter import messagebox

def muestra_msj_cesar(mensaje, resultado, ComboBoxOpcion,ComboBoxMetodos, llave, elapsed_time):
    lista = ["Mensaje original: ",mensaje,"\nOpcion utilizada: ",ComboBoxOpcion,"\nMetodo utilizado: ",
    ComboBoxMetodos,"\nMensaje final: ",resultado, "\nRotaciones: ", llave, "\nTiempo transcurrido: ",str(elapsed_time), " segundos"]
    return (" ".join(lista))

def muestra_msj(mensaje, resultado, ComboBoxOpcion,ComboBoxMetodos, llave, elapsed_time):
    lista = ["Mensaje original: ",mensaje , "\nOpcion utilizada: ",ComboBoxOpcion,"\nMetodo utilizado: ",
    ComboBoxMetodos,"\nMensaje final: ",resultado, "\nLlave utilizada: ", llave, "\nTiempo transcurrido: ",str(elapsed_time), " segundos"]
    return (" ".join(lista))


def registrar_info_cesar(mensaje, resultado, ComboBoxOpcion, ComboBoxMetodos,llave, elapsed_time):
    archivoRegistro = open("historial.txt","a")
    archivoRegistro.write("\n\n\nMensaje original: ")
    archivoRegistro.write(mensaje)
    archivoRegistro.write("\nOpcion utilizada: ")
    archivoRegistro.write(ComboBoxOpcion)
    archivoRegistro.write("\nMetodo utilizado: ")
    archivoRegistro.write(ComboBoxMetodos)
    archivoRegistro.write("\nRotaciones: ")
    archivoRegistro.write(llave)
    archivoRegistro.write("\nMensaje final: ")
    archivoRegistro.write(resultado)
    archivoRegistro.write("\nTiempo transcurrido: ")
    archivoRegistro.write(str(elapsed_time))
    archivoRegistro.write(" segundos")
    archivoRegistro.write("\n\n    ")
    archivoRegistro.close() 

def registrar_info(mensaje, resultado, ComboBoxOpcion, ComboBoxMetodos, llave, elapsed_time):
    archivoRegistro = open("historial.txt","a")
    archivoRegistro.write("\n\n\nMensaje original: ")
    archivoRegistro.write(str(mensaje))
    archivoRegistro.write("\nOpcion utilizada: ")
    archivoRegistro.write(ComboBoxOpcion)
    archivoRegistro.write("\nMetodo utilizado: ")
    archivoRegistro.write(ComboBoxMetodos)
    archivoRegistro.write("\nLlave utilizada: ")
    archivoRegistro.write(llave)
    archivoRegistro.write("\nMensaje final: ")
    archivoRegistro.write(str(resultado))
    archivoRegistro.write("\nTiempo transcurrido: ")
    archivoRegistro.write(str(elapsed_time))
    archivoRegistro.write(" segundos")
    archivoRegistro.write("\n\n     ")
    archivoRegistro.close() 

def comprobar_llave_DES(llave):
    if (len(llave) < 8):
        messagebox.showerror(title = "Error", message= "La clave es demasiado corta, deben ser 8 caracteres")
    else:
        llave = llave[:8]
    return llave

def comprobar_mensaje(mensaje):
    for letra in mensaje:
        if letra == 'ñ' or letra == 'Ñ':
            messagebox.showerror(title= "Error", message= "El mensaje no puede contener la letra ñ")
            break
        else:
            continue
    return mensaje

def comprobar_llave(key):
        if (key == ""):
            messagebox.showerror(title = "Error", message = "Debe ingresar clave")
        elif (len(key) < 4):
            messagebox.showerror(title = "Error", message= "La clave debe poseer mas de 4 caracteres")
        else:
            return key

def comprobar_rotacion(llave):
    aux=""
    if (llave == ""):
        messagebox.showerror(title="Error", message = "Debe ingresar una clave")
    try:
        aux = int(llave)
        if (aux > 0 and aux < 26):
            return aux
        else:
            messagebox.showerror(title = "Error", message = "Ingrese numero entre 1 y 25")
    except ValueError:
        messagebox.showerror(title="Error", message = "Ingrese clave numerica")    

    
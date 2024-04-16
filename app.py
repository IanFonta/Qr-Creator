import tkinter as tk
import os
from PIL import ImageTk, Image
import qrcode

def generar_qr():
    texto = texto_input.get()
    img = qrcode.make(texto)
    file_path = os.path.join(os.path.dirname(__file__), "output.png") # Muestra donde se va a ubicar la imagen generada
    img.save(file_path)
    img_label.config(text="¡QR generado con éxito!")
    mostrar_imagen(file_path)

def mostrar_imagen(file_path):
    img = Image.open(file_path)
    img.thumbnail((200, 200))  # Redimensionar la imagen para que se ajuste al área de visualización
    img_tk = ImageTk.PhotoImage(img)
    imagen_label.config(image=img_tk)
    imagen_label.image = img_tk  # Esto es importante para evitar que la imagen se borre por el recolector de basura

# Configuración de la ventana
ventana = tk.Tk()
ventana.title("Generador de QR Code")
ventana.geometry("500x400")  # Aumentamos un poco la altura para dejar espacio para la imagen

frame = tk.Frame(ventana) # Marco para centrar los elementos verticalmente
frame.pack(expand=True)

texto_input = tk.Entry(frame, width=40) # Campo de texto para ingresar el texto del QR
texto_input.pack(pady=10)

boton_generar = tk.Button(frame, text="Generar QR Code", command=generar_qr) # Botón para generar el QR
boton_generar.pack(pady=5)

img_label = tk.Label(frame, text="") # Etiqueta para mostrar mensajes de éxito
img_label.pack(pady=5)

imagen_label = tk.Label(frame) # Muestra la imagen generada
imagen_label.pack(pady=10)

frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER) # Centrar el marco en la ventana

# Iniciar el bucle de eventos
ventana.mainloop()


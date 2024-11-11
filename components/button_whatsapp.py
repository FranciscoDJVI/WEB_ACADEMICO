import reflex as rx
import os
from dotenv import load_dotenv
from utils.crypto import desencriptar_archivo, clave

desencriptar_archivo(".env", clave)

load_dotenv()

numero = os.environ.get("NUMERO")

def open_whatsapp():
  numero_telefono = numero  # Reemplaza con tu número de teléfono
  mensaje = "Hola! Me gustaría obtener más información."  # Mensaje opcional
  url = f"https://wa.me/{numero_telefono}?text={mensaje}"
  return rx.redirect(url)


def button_whatsapp():
  return rx.center(
    rx.button(
      "WhatsApp",
      on_click=open_whatsapp,
      bg="green",
      color="white",
      border_radius="1em",
      padding="1em",
    )
  )

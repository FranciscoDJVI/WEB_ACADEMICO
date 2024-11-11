from cryptography.fernet import Fernet

def generar_clave():
  clave = Fernet.generate_key()
  with open("clave.key", "wb") as archivo_clave:
    archivo_clave.write(clave)

def cargar_clave():
  return open("clave.key", "rb").read()

def encriptar_archivo(nombre_archivo, clave):
  f = Fernet(clave)
  with open(nombre_archivo, "rb") as archivo:
    datos_originales = archivo.read()
  datos_encriptados = f.encrypt(datos_originales)
  with open(nombre_archivo, "wb") as archivo:
    archivo.write(datos_encriptados)

def desencriptar_archivo(nombre_archivo, clave):
  f = Fernet(clave)
  with open(nombre_archivo, "rb") as archivo:
    datos_encriptados = archivo.read()
  datos_originales = f.decrypt(datos_encriptados)
  with open(nombre_archivo, "wb") as archivo:
    archivo.write(datos_originales)

generar_clave()  

clave = cargar_clave()

nombre_archivo = ".env"
encriptar_archivo(nombre_archivo, clave)

# Importar la clase FastAPI
from fastapi import FastAPI

# Crear una instancia de la clase FastAPI
app = FastAPI()

# Definir una "ruta" (o endpoint) con su "decorador"
@app.get("/")
# Función que se ejecutará cuando se visite la ruta "/"
def read_root():
    return {"Hola": "Mundo"}


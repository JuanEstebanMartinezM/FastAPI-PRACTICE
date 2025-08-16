# FastAPI Documentation

Este documento describe cómo crear un entorno virtual, instalar **FastAPI** y **Uvicorn**, y ejecutar un primer proyecto de ejemplo.

---

## 1. Crear el entorno virtual

**`venv`** es un módulo de Python que crea un entorno virtual.  
El segundo **`venv`** es el nombre que le damos a la carpeta del entorno.

```
python -m venv venv
```
1.1. ¿Cómo desactivar el entorno virtual?
    El entorno virtual se desactiva con el siguiente comando:

    ```
    deactivate
    ```

## 2. Luego se inicializa el entorno con:

```
.\venv\Scripts\activate
```
Activar el entorno virtual asegura que cualquier paquete que instales (como FastAPI) se guarde dentro de la carpeta venv y no globalmente en tu sistema.

## 3. Instalar FastAPI y Uvicorn:
- Instalamos `FastAPI` con todas sus dependencias más comunes:
     ```
     pip install "fastapi[all]"
     ```
     
    **Justificación:**
    Esta es la forma más fácil de instalar FastAPI junto con dependencias opcionales como:
    
    `uvicorn` → servidor para correr la aplicación.
    
    `pydantic` → validación de datos.
    
     Otros módulos útiles.
- También instalamos `Uvicorn` explícitamente:
    ```
    pip install "uvicorn[standard]"
    ```
    **Justificación:**
    Uvicorn es un servidor web asíncrono que ejecuta aplicaciones ASGI (Asynchronous Server Gateway Interface).
    En términos sencillos, es lo que permite que tu aplicación web se ejecute y reciba peticiones.
  
    **RECOMENDACIÓN**
  
    **Para aprender y proyectos pequeños:** instala solo fastapi y luego añade lo que necesites manualmente,
    ya que al usar `[all] o [standard]` Básicamente te instala todo lo que podrías llegar a necesitar, pero muchas de esas librerías puede que no las uses nunca.
  
## 4. Crear el primer proyecto: **Hola Mundo**

Creamos un archivo `main.py`.
Este será el archivo principal donde escribiremos el código de nuestra API.
```
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hola": "Mundo"}
```
**Explicación del código**

`from fastapi import FastAPI` → Importamos la clase principal de la biblioteca, base de nuestra aplicación.

`app = FastAPI()` → Creamos una instancia de la clase FastAPI y la llamamos app.

`@app.get("/")` → Decorador que indica que la función se ejecuta cuando alguien hace una petición GET a la ruta "/" (la raíz del sitio).

`def read_root():` → Función que maneja la ruta.

`return {"Hola": "Mundo"}` → Retorna un diccionario en Python. FastAPI lo convierte automáticamente a JSON.

## 5. Ejecutar el servidor
Para iniciar la aplicación, usa el siguiente comando:

```
uvicorn main:app --reload
```
**Explicación del comando:**

`uvicorn` → servidor web que utilizamos.

`main:app` → le dice a Uvicorn que busque la instancia `app` en el archivo `main.py`.

`--reload` → reinicia el servidor automáticamente cuando detecta cambios (muy útil en desarrollo).

## **Documentación automática de FastAPI**
Una de las mejores características de FastAPI es su documentación automática.

Abre tu navegador web.

**Visita:** `http://127.0.0.1:8000/docs` → Interfaz **Swagger UI** donde puedes probar tus endpoints.

**Alternativamente, visita:** `http://127.0.0.1:8000/redoc` → Documentación en formato ReDoc.


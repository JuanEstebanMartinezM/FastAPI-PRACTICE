# Documentacion FastAPI
## como primer paso se creara el entorno viartual 
    venv es un módulo de Python que crea un entorno virtual. El segundo venv es el nombre que le damos a la carpeta del entorno virtual.

    - codigo: `python -m venv venv`

    seguido a esto se inicializara el entorno con

    - codigo: `.\venv\Scripts\activate`

    Activar el entorno virtual te asegura que cualquier paquete que instales (como FastAPI) se guardará dentro de la carpeta venv y no globalmente en tu sistema.

## como segundo paso se comenzara con la instalacion de fastapi y uvicorn

    - codigo: `pip install "fastapi[all]"`

    ***Justificación:*** Esta es la forma más fácil de instalar FastAPI junto con todas sus dependencias opcionales más comunes, como uvicorn (para correr el servidor), pydantic (para validación de datos) y otros.

    - codigo: `pip install "uvicorn[standard]"`

    ***Justificación:*** uvicorn es un servidor web asíncrono que corre aplicaciones ASGI (Asynchronous Server Gateway Interface), como FastAPI. En términos sencillos, es lo que permite que tu aplicación web se ejecute y reciba peticiones.

# lo siguiente es comprobar que todo este bien y para eso crearemos nuestro primer hola mundo en fastAPI.
para esto crearemos un archivo main.py Este será el archivo principal donde escribiremos el código de nuestra API.

---

## Explicacion del codigo:
    from fastapi import FastAPI: Importamos la clase principal de la biblioteca. Es la base de nuestra aplicación.

    **app = FastAPI():** Creamos una instancia de la clase FastAPI. A esta instancia la llamamos app.

    **@app.get("/"):** Esto es un decorador. Un decorador es una forma de "envolver" una función para modificar su comportamiento. En este caso, le dice a FastAPI que la función que está debajo (read_root) se debe ejecutar cuando alguien hace una petición GET a la ruta **"/"** (la raíz de tu sitio web).

    **def read_root():**: Esta es la función que se ejecuta.

    **return {"Hola": "Mundo"}:** La función devuelve un diccionario de Python. FastAPI automáticamente lo convierte a un formato JSON (JavaScript Object Notation), que es el formato estándar para intercambiar datos en la web. La respuesta será: {"Hola": "Mundo"}.

## Ejecutando tu Servidor

    - codigo: `uvicorn main:app --reload` 

    Explicación del Comando:
    uvicorn: El servidor web que estamos usando.

    main:app: Le estamos diciendo a uvicorn que busque la instancia llamada app dentro del archivo main.py.

    --reload: Esto es muy útil durante el fase de desarrollo. Le dice a uvicorn que reinicie el servidor automáticamente cada vez que guardes un cambio en tu código.

## Documentación Automática de FastAPI
- Una de las mejores cosas de FastAPI es su documentación automática.

    Paso a paso:
    Abre tu navegador web y ve a la siguiente dirección: http://127.0.0.1:8000/docs.

    Verás una interfaz interactiva de Swagger UI . Aquí puedes ver y probar todas las rutas (endpoints) que has creado. FastAPI genera esto por ti automáticamente a partir de tu código.

    También puedes ir a http://127.0.0.1:8000/redoc para ver una documentación alternativa.
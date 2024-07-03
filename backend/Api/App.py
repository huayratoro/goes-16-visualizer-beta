from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import os

app = FastAPI()

# Lista de orígenes permitidos (puedes ajustarla según tus necesidades)
origins = [
    "http://localhost",
    "http://localhost:8000",
    "http://localhost:8000/imagenes",
    "http://0.0.0.0:8000/imagenes",
    "http://127.0.0.1:5501",  # Agrega este origen
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Ruta para obtener imágenes desde un directorio local
@app.get("/imagenes")
async def obtener_imagenes():
    directorio = "backend/assets/goes_images/"  
    imagenes = []

    for archivo in os.listdir(directorio):
        if archivo.lower().endswith((".png")):
            ruta_completa = os.path.join(directorio, archivo)
            imagenes.append(ruta_completa)

    return JSONResponse(content={"imagenes": sorted(imagenes)})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

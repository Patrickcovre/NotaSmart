from fastapi import FastAPI, File, UploadFile, HTTPException
from typing import List

app = FastAPI()

# TODO: ESTOU USANDO CONTENT_TYPE POR MOTIVO QUE É UM APP PESSOAL POR ENQUANTO ENTAO DE PRIMEIRO MOMENTO NAO VAI TER CAMADA DE SEGURANÇA AINDA, MAS DEPOIS VAI TER

@app.post("/upload_file")
async def upload_file(file:UploadFile):
    #Usar UploadFile para se caso a memória estiver quase estourando ele vai passar para o disco e continuar o processo
    if file.content_type != "image/jpeg":
        raise HTTPException(status_code=400, detail="File must be a JPEG image")

    return {"filename": file}
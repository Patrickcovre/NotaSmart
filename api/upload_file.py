from fastapi import FastAPI, File, UploadFile, HTTPException
from typing import List

app = FastAPI()

@app.post("/upload_file")
async def upload_file(file:UploadFile):
    #Usar UploadFile para se caso a memória estiver quase estourando ele vai passar para o disco e continuar o processo
    if file.content_type != "image/jpeg":
        raise HTTPException(status_code=400, detail="File must be a JPEG image")

    return {"filename": file}
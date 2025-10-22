from fastapi import FastAPI, File, UploadFile
from typing import List

app = FastAPI()

@app.post("/upload_file")
async def upload_file(file: List[UploadFile]):
    #Usar UploadFile para se caso a memória estiver quase estourando ele vai passar para o disco e continuar o processo
    return {"filename": file.filename}
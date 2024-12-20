from fastapi import FastAPI, UploadFile, File
from pathlib import Path

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the API!"}

@app.post("/upload-image/")
async def upload_image(file: UploadFile = File(...)):
    save_path = Path("data/raw") / file.filename
    with open(save_path, "wb") as f:
        f.write(await file.read())
    return {"filename": file.filename, "message": "File uploaded successfully"}

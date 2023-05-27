from fastapi import FastAPI,UploadFile, File
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    print("upload----");
    contents = await file.read()
    with open(file.filename, "wb") as f:
        f.write(contents)
    return {"filename": file.filename}

@app.get('/')
async def root():
    return {'hello': 'world'}


if __name__ == "__main__":
    import nest_asyncio
    nest_asyncio.apply()
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

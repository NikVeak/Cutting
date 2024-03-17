import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import service
import model


app = FastAPI()

# Настройка CORS middleware
origins = [
    "http://localhost",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.get("/test_linear")
async def test_linear_cut():
    original_length = 6000
    cuts_length = [1500, 1450, 1300, 1150, 1000]
    cuts_count = [10, 3, 6, 9, 10]
    return service.linear_cut_method(original_length, cuts_length, cuts_count)


@app.post("/linear-cut/", tags=["linear-cut"])
async def linear_cut(options_cut: model.CutOptions):
    original_length = options_cut.original_length
    cuts_length = options_cut.cut_length
    cuts_count = options_cut.cut_count
    return service.linear_cut_method(original_length, cuts_length, cuts_count)

@app.get("/stop")
async def stopserver():
    stop_uvicorn_process()
    return {"message": "Сервер успешно остановлен"}

@app.middleware("http")
async def add_cors_header(request, call_next):
    response = await call_next(request)
    response.headers["Access-Control-Allow-Origin"] = "http://localhost:3000"
    return response



if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)



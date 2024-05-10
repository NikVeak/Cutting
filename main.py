import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import service
import model

app = FastAPI()

# Настройка CORS middleware
origins = [
    "http://localhost",
    "https://localhost:3000",
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


@app.get("/test_bivariate")
async def test_bivariate():
    pass


@app.post("/linear-cut/", tags=["linear-cut"])
async def linear_cut(options_cut: model.LinearCutOptions):
    original_length = options_cut.original_length
    cuts_length = options_cut.cut_length
    cuts_count = options_cut.cut_count
    blade_thickness = options_cut.blade_thickness
    cutting_angle = options_cut.cutting_angle
    original_thickness = options_cut.original_thickness

    service.prepare_cuts(original_length, cuts_length, blade_thickness, cutting_angle, original_thickness)
    maps = service.linear_cut_method(original_length, cuts_length, cuts_count)

    if len(maps) == 0:
        return []
    else:
        new_maps = service.recycle_maps_remains(original_length, cuts_length, maps)
        result_maps = service.reсycle_maps(original_length, cuts_length, maps)
        return result_maps, new_maps

@app.post("/linear-cut-dynamic", tags=["linear-cut-dynamic"])
async def linear_cut(options_cut: model.LinearCutOptions):
    original_length = options_cut.original_length
    cuts_length = options_cut.cut_length
    cuts_count = options_cut.cut_count
    blade_thickness = options_cut.blade_thickness
    cutting_angle = options_cut.cutting_angle
    original_thickness = options_cut.original_thickness

    service.prepare_cuts(original_length, cuts_length, blade_thickness, cutting_angle, original_thickness)
    maps = service.find_optimal_maps(original_length, cuts_length, cuts_count)
    result_maps = service.reсycle_maps(original_length, cuts_length, maps)
    return result_maps, maps

@app.post("/linear-multi-cut-dynamic", tags=["linear-multi-cut-dynamic"])
async def linear_multi_cut(options_cut: model.LinearMultiCutOptions):
    originals_length = options_cut.originals_length
    cut_length = options_cut.cut_length
    cut_count = options_cut.cut_count
    result_maps = service.bivariate_cut(originals_length, cut_length, cut_count)
    return result_maps

@app.post("/bivariate-cut")
async def bivariate_cut(options_cut: model.SquareCutOptions):
    original_square = options_cut.original_square
    cuts_length = options_cut.cut_length
    cuts_count = options_cut.cut_count
    result_maps = service.bivariate_cut(original_square, cuts_length, cuts_count)
    return result_maps


@app.middleware("http")
async def add_cors_header(request, call_next):
    response = await call_next(request)
    response.headers["Access-Control-Allow-Origin"] = "http://localhost:3000"
    return response

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

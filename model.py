from pydantic import BaseModel
from typing import List
class LinearCutOptions(BaseModel):
    # длина исходного материала
    original_length: int
    # массив заготавливаемых длин
    cut_length: List[int]
    # массив заготавливаемых количеств
    cut_count: List[int]
    # толщина лезвия
    blade_thickness: float
    # угол реза
    cutting_angle: float
    # толщина исходной заготовки
    original_thickness: float

class SquareCutOptions(BaseModel):
    pieces: List[tuple]
    material_height: int
    material_width: int

class LinearMultiCutOptions(BaseModel):
    # длина исходного материала
    originals_length: List[int]
    # массив заготавливаемых длин
    cut_length: List[int]
    # массив заготавливаемых количеств
    cut_count: List[int]
    # толщина лезвия
    blade_thickness: float
    # угол реза
    cutting_angle: float
    # толщина исходной заготовки
    original_thickness: float



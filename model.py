from pydantic import BaseModel
from typing import List
class CutOptions(BaseModel):
    original_length: int
    cut_length: List[int]
    cut_count: List[int]


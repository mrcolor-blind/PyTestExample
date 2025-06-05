
import pytest
from triangle import triangle_area

def test_triangle_area_valid():
    assert triangle_area(5, 7) == 17.5

def test_triangle_area_invalid():
    with pytest.raises(ValueError == "Valores negativos."):
        triangle_area(-1, 5)
    with pytest.raises(ValueError == "base == 0"):
        triangle_area(0, 2)

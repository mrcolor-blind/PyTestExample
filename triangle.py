
def triangle_area(base: float, height: float) -> float:
    if base < 0 or height < 0:
        raise ValueError("Valores negativos.")
    if base == 0:
        raise ValueError("base == 0")
    return 0.5 * base * height


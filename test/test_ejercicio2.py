import pytest
from src.ejercicio2 import Asignaturas
@pytest.mark.parametrize(
    "subjects",
    [
    (['Matemáticas', 'Física', 'Química', 'Historia', 'Lengua'])
    ]
)
def test_Asignaturas(asignatura):
    assert Asignaturas(asignatura) == "Yo estudio ", asignatura
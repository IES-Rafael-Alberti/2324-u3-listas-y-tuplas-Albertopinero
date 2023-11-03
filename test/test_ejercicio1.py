import pytest
from src.ejercicio1 import AsignaturasCurso
@pytest.mark.parametrize(
    "subjects",
    [
    (['Matemáticas', 'Física', 'Química', 'Historia', 'Lengua'])
    ]
)
def test_Asignaturas_Curso(subjects):
    assert AsignaturasCurso(subjects) == subjects
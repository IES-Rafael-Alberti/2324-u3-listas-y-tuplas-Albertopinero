import pytest
from src.ejercicio3 import NotasCurso
@pytest.mark.parametrize(
    "subjects",
    [
    (['Matemáticas', 'Física', 'Química', 'Historia', 'Lengua'])
    ]
)
def test_Notas_Curso(subjects):
    assert NotasCurso(subjects) == subjects
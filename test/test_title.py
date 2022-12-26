import unittest
from src.schemas.title import Title
from src.utils.constants import TITULOS, ID_TITULOS
from src.services.title_service import TitleService
from src.connection import get_dal




db = get_dal().get_db()
            
#validar que la funcion get_cantidad_titulos retorne la cantidad de titulos
class TestTitleService(unittest.TestCase):
    def test_get_cantidad_titulos(self):
        # Arrange
        service = TitleService()
        # Act
        cantidad = service.get_cantidad_titulos(db)
        # Assert
        self.assertEqual(cantidad, 3)

    #validar que la funcion create_titulo cree un titulo
    def test_create_titulo(self):
        # Arrange
        service = TitleService()
        # Act
        titulo = service.create_titulo(db, Title(**TITULOS[0]))
        # Assert
        self.assertEqual(titulo, TITULOS[0])

    #validar que la funcion delete_titulo elimine un titulo
    def test_delete_titulo(self):
        # Arrange
        service = TitleService()
        # Act
        titulo = service.delete_titulo(db, ID_TITULOS[0])
        # Assert
        self.assertEqual(titulo, None)

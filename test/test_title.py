import unittest
from src.schemas.title import Title
from src.utils.constants import TITULOS, ID_TITULOS
from src.services.title_service import TitleService
from src.connection import get_dal

db = get_dal().get_db()


class TestTitleService(unittest.TestCase):
    def test_get_cantidad_titulos(self):
        # Arrange
        service = TitleService()
        # Act
        cantidad = service.get_cantidad_titulos(db)
        # Assert
        self.assertEqual(cantidad, 3)

    def test_delete_titulo(self):
        # Arrange
        service = TitleService()
        # Act
        titulo = service.delete_titulo(db, ID_TITULOS[0])
        # Assert
        self.assertEqual(titulo, None)

    def test_create_titulo(self):
        # Arrange
        service = TitleService()
        nuevo_titulo = Title(
            id_titulo='THI',
            titulo='DOLAR',
            clasificacion='C',
            valor=50000,
            fecha_creacion='2021-01-01',
            fecha_vencimiento='2021-01-01',
            pago_cuota='y',
        )
        # Act
        titulo = service.create_titulo(db, nuevo_titulo)
        # Assert
        self.assertEqual(titulo, nuevo_titulo)

    def test_get_titulos(self):
        # Arrange
        service = TitleService()
        # Act
        titulos = service.get_titulos(db)
        # Assert
        self.assertEqual(db, titulos)


if __name__ == '__main__':
    unittest.main()



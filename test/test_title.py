import unittest
from src.schemas.title import Title
from src.utils.constants import TITULOS, ID_TITULOS
from src.services.title_service import TitleService
from src.connection import get_dal

db = get_dal().get_db()


class TestTitleService(unittest.TestCase):
    def test_get_cantidad_titulos(self):
        service = TitleService()
        cantidad = service.get_cantidad_titulos(db)
        self.assertEqual(cantidad, 3)

    def test_delete_titulo(self):
        service = TitleService()
        titulo = service.delete_titulo(db, ID_TITULOS[0])
        self.assertEqual(titulo, None)

    def test_create_titulo(self):
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
        titulo = service.create_titulo(db, nuevo_titulo)
        self.assertEqual(titulo, nuevo_titulo)

    def test_get_titulos(self):
        service = TitleService()
        titulos = service.get_titulos(db)
        self.assertEqual(db, titulos)


if __name__ == '__main__':
    unittest.main()

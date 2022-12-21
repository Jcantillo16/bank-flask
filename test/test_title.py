import unittest
from src.schemas.title import Title


class TestTitle(unittest.TestCase):
    def test_id_titulo(self):
        with self.assertRaises(ValueError):
            Title(
                id_titulo="USD1",
                titulo="DOLAR",
                clasificacion="DIV",
                valor=500000000,
                fecha_creacion="2022-03-14",
                fecha_vencimiento="2023-03-15",
                pago_cuota="y"
            )


if __name__ == '__main__':
    unittest.main()

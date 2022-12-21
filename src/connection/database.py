import datetime
from src.schemas.title import Title


class DataAccessLayer:

    def __init__(self):
        self.db: dict[str, Title] = {
            'USD': Title(
                id_titulo='USD',
                titulo='DOLAR',
                clasificacion='DIV',
                valor=500000000,
                fecha_creacion=datetime.date(2022, 3, 14),
                fecha_vencimiento=datetime.date(2023, 3, 15),
                pago_cuota='y'
            ),
            'TRPV': Title(
                id_titulo='TRPV',
                titulo='TITULO DE PARTICIPACION RENTA VARIABLE',
                clasificacion='DIV',
                valor=256000000,
                fecha_creacion=datetime.date(2022, 8, 25),
                fecha_vencimiento=datetime.date(2023, 8, 16),
                pago_cuota='y'
            ),
            'TP': Title(
                id_titulo='TP',
                titulo='TITULO DE PARTICIPACION',
                clasificacion='DIV',
                valor=360000000,
                fecha_creacion=datetime.date(2022, 2, 16),
                fecha_vencimiento=datetime.date(2023, 2, 17),
                pago_cuota='y'
            )
        }

    def get_db(self) -> dict[str, Title]:
        return self.db

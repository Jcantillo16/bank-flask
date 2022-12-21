import datetime
from typing import Literal
from dataclasses import dataclass
from src.utils.constants import TITULOS, ID_TITULOS


@dataclass
class Title:
    id_titulo: str
    titulo: str
    clasificacion: str
    valor: float
    fecha_creacion: datetime.datetime
    fecha_vencimiento: datetime.datetime
    pago_cuota: Literal['y', 'n']

    def __post_init__(self):
        DATE_FORMAT: str = '%Y-%m-%d'
        if isinstance(self.fecha_creacion, str):
            self.fecha_creacion = datetime.datetime.strptime(
                self.fecha_creacion,
                DATE_FORMAT
            )
        if isinstance(self.fecha_vencimiento, str):
            self.fecha_vencimiento = datetime.datetime.strptime(
                self.fecha_vencimiento,
                DATE_FORMAT
            )

        if self.id_titulo not in ID_TITULOS:
            raise ValueError(f'El idtitulo {self.id_titulo} no es válido.')

        if self.pago_cuota not in ['y', 'n']:
            raise ValueError(f'El pago de la cuota {self.pago_cuota} no es válido.')

        if self.fecha_creacion > self.fecha_vencimiento:
            raise ValueError(f'La fecha de creación {self.fecha_creacion} '
                             f'no puede ser mayor a la fecha de vencimiento {self.fecha_vencimiento}.')

        if self.id_titulo == 'USD':
            self.titulo = 'DOLAR'

        elif self.id_titulo == 'TRPV':
            self.titulo = 'TITULO DE PARTICIPACION RENTA VARIABLE'

        elif self.id_titulo == 'TP':
            self.titulo = 'TITULO DE PARTICIPACION'

        elif self.id_titulo == 'TID':
            self.titulo = 'TIDIS'

        elif self.id_titulo == 'THI':
            self.titulo = 'TITULOS HIPOTECARIOS'

        elif self.id_titulo == 'TESU':
            self.titulo = 'TES UVR'

        elif self.id_titulo == 'TEST':
            self.titulo = 'TES TRM'

        elif self.id_titulo == 'TESP':
            self.titulo = 'TES PESOS'

        elif self.id_titulo == 'TESOROS':
            self.titulo = 'BONOS DEL TESORO EEUU'

        elif self.id_titulo == 'TESI':
            self.titulo = 'TES IPC'

    def __str__(self) -> str:
        return (
            f'Titulo n° {self.id_titulo}, {self.titulo}, {self.clasificacion}'
            f', {self.valor}, {self.fecha_creacion}, {self.fecha_vencimiento}'
            f', {self.pago_cuota}'
        )

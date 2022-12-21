import datetime
from typing import Literal
from dataclasses import dataclass


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

    def __str__(self) -> str:
        return (
            f'Titulo n° {self.id_titulo}, {self.titulo}, {self.clasificacion}'
            f', {self.valor}, {self.fecha_creacion}, {self.fecha_vencimiento}'
            f', {self.pago_cuota}'
        )

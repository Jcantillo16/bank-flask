import datetime

from src.connection import get_dal
from src.schemas.title import Title
from src.repositories.title_repository import TitleRepository
from src.errors.titulo import TituloInvalido, TituloNoExiste


class TitleService:

    def __init__(self):
        self._repo = TitleRepository()

    def get_cantidad_titulos(self, db: dict[str, Title]) -> int:
        return self._repo.get_cantidad_titulos(db)

    def create_titulo(
            self,
            db: dict[str, Title],
            nuevo_titulo: Title
    ) -> dict:
        titulo = self._repo.get_titulo_por_id(db, nuevo_titulo.id_titulo)
        if titulo:
            raise TituloInvalido('Ya existe un titulo con este id_titulo')
        new_record = self._repo.create_titulo(db, nuevo_titulo)
        return new_record

    def delete_titulo(
            self,
            db: dict[str, Title],
            id_titulo: str
    ):
        return self._repo.delete_titulo(db, id_titulo)

    def get_titulos(self, db: dict[str, Title]) -> dict[str, Title]:
        return self._repo.get_titulos(db)

    def modificar_fecha_creacion(self, db: dict[str, Title], fecha: str) -> dict[str, Title]:
        titulo_modificado = {}
        for titulo in db.values():
            if titulo.fecha_creacion == datetime.date.fromisoformat(fecha):
                titulo.fecha_creacion = datetime.date.fromisoformat('2021-01-01')
                titulo_modificado[titulo.id_titulo] = titulo
        return titulo_modificado

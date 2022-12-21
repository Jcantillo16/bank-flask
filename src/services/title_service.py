from src.schemas.title import Title
from src.repositories.title_repository import TitleRepository

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
            raise Exception('Ya existe un titulo con este id')
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

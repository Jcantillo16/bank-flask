from src.schemas.title import Title


class TitleRepository:

    def get_cantidad_titulos(self, db: dict[str, Title]) -> int:
        return len(db.keys())

    def get_titulo_por_id(self, db: dict[str, Title], id_titulo: str) -> str:
        return db.get(id_titulo, None)

    def create_titulo(
        self,
        db: dict[str, Title],
        nuevo_titulo: Title
    ) -> Title:
        db[nuevo_titulo.id_titulo] = nuevo_titulo
        return nuevo_titulo

    def delete_titulo(self, db: dict[str, Title], id_titulo: str):
        db.pop(id_titulo, None)

    def get_titulos(self, db) -> dict[str, Title]:
        return db

from src.connection import get_dal
from src.services.title_service import TitleService
from src.schemas.title import Title
from flask import Blueprint, request, abort

title_api = Blueprint('titles', __name__)
title_service = TitleService()


@title_api.get('/cantidad')
def get_cantidad():
    db = get_dal().get_db()
    return {
        'cantidad_titulo': title_service.get_cantidad_titulos(db)
    }


@title_api.post('/crear')
def create_titulo():
    db = get_dal().get_db()
    data: dict = request.get_json()

    try:
        new_titulo = title_service.create_titulo(
            db=db,
            nuevo_titulo=Title(**data)
        )
    except Exception as e:
        abort(404, str(e))

    return {
        'titulo': new_titulo
    }


@title_api.delete('/delete/<id_titulo>')
def delete_titulo(id_titulo: str):
    db = get_dal().get_db()
    title_service.delete_titulo(db, id_titulo)
    return '', 204


@title_api.get('/list')
def get_titulos():
    db = get_dal().get_db()
    return title_service.get_titulos(db)


@title_api.get('/modificar_fecha_creacion/<fecha>')
def modificar_fecha_creacion(fecha: str):
    db = get_dal().get_db()
    return title_service.modificar_fecha_creacion(db, fecha)

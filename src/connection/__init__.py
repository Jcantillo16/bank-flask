from src.connection.database import DataAccessLayer

dal: DataAccessLayer = None


def get_dal() -> DataAccessLayer:
    """TODO: Agregar comentario
    """

    global dal

    if dal is None:
        dal = DataAccessLayer()

    return dal

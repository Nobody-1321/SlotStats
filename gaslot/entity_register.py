
class EntityRegistry:
    """Clase para registrar y acceder a entidades de manera centralizada."""
    _registry = {}

    @classmethod
    def register(cls, name, entity):
        """Registra una entidad con un nombre único."""
        cls._registry[name] = entity

    @classmethod
    def get(cls, name):
        """Obtiene una entidad registrada por su nombre."""
        return cls._registry.get(name)

    @classmethod
    def unregister(cls, name):
        """Elimina una entidad registrada."""
        if name in cls._registry:
            del cls._registry[name]

    @classmethod
    def list_entities(cls):
        """Devuelve una lista de todas las entidades registradas."""
        return list(cls._registry.keys())

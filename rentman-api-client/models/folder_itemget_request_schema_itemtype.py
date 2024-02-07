from enum import Enum


class FolderItemgetRequestSchemaItemtype(str, Enum):
    EQUIPMENT = "equipment"
    CONTACT = "contact"
    VEHICLE = "vehicle"
    USER = "user"
    CONTAINER = "container"

    def __str__(self) -> str:
        return str(self.value)

from enum import Enum


class MateriaalItemputResponseSchemaDataIsPhysical(str, Enum):
    VIRTUAL_PACKAGE = "Virtual package"
    PHYSICAL_EQUIPMENT = "Physical equipment"

    def __str__(self) -> str:
        return str(self.value)

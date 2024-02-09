from enum import Enum


class ProjectTypeCollectionpostResponseSchemaDataItemType(str, Enum):
    REGULAR = "regular"
    SUPPLIER = "supplier"
    TRANSFER = "transfer"
    SHIFTS = "shifts"

    def __str__(self) -> str:
        return str(self.value)

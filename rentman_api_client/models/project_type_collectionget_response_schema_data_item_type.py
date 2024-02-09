from enum import Enum


class ProjectTypeCollectiongetResponseSchemaDataItemType(str, Enum):
    REGULAR = "regular"
    SUPPLIER = "supplier"
    TRANSFER = "transfer"
    SHIFTS = "shifts"

    def __str__(self) -> str:
        return str(self.value)

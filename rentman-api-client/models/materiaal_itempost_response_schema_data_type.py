from enum import Enum


class MateriaalItempostResponseSchemaDataType(str, Enum):
    SET = "set"
    CASE = "case"
    ITEM = "item"

    def __str__(self) -> str:
        return str(self.value)

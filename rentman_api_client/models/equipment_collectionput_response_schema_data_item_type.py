from enum import Enum


class EquipmentCollectionputResponseSchemaDataItemType(str, Enum):
    SET = "set"
    CASE = "case"
    ITEM = "item"

    def __str__(self) -> str:
        return str(self.value)

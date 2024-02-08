from enum import Enum


class AssetLocationItemputResponseSchemaDataType(str, Enum):
    PLANNABLE = "plannable"
    NONPLANNABLE = "nonplannable"

    def __str__(self) -> str:
        return str(self.value)

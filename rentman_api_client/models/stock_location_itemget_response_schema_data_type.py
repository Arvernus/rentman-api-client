from enum import Enum


class StockLocationItemgetResponseSchemaDataType(str, Enum):
    PLANNABLE = "plannable"
    NONPLANNABLE = "nonplannable"

    def __str__(self) -> str:
        return str(self.value)

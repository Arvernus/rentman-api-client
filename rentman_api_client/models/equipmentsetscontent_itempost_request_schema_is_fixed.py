from enum import Enum


class EquipmentsetscontentItempostRequestSchemaIsFixed(str, Enum):
    AVAILABLE_OUTSIDE_THIS_COMBINATION = "Available outside this combination"
    RESERVED_FROM_STOCK = "Reserved from stock"

    def __str__(self) -> str:
        return str(self.value)

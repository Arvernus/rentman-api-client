from enum import Enum


class EquipmentItempostRequestSchemaStockManagement(str, Enum):
    EXCLUDE_FROM_STOCK_TRACKING = "Exclude from stock tracking"
    TRACK_STOCK = "Track stock"

    def __str__(self) -> str:
        return str(self.value)

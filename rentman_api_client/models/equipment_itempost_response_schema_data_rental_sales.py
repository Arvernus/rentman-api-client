from enum import Enum


class EquipmentItempostResponseSchemaDataRentalSales(str, Enum):
    SALE = "Sale"
    RENTAL = "Rental"

    def __str__(self) -> str:
        return str(self.value)

from enum import Enum


class MateriaalItemgetResponseSchemaDataRentalSales(str, Enum):
    SALE = "Sale"
    RENTAL = "Rental"

    def __str__(self) -> str:
        return str(self.value)

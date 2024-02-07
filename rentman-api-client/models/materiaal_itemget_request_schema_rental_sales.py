from enum import Enum


class MateriaalItemgetRequestSchemaRentalSales(str, Enum):
    SALE = "Sale"
    RENTAL = "Rental"

    def __str__(self) -> str:
        return str(self.value)

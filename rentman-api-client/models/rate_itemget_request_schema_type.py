from enum import Enum


class RateItemgetRequestSchemaType(str, Enum):
    PRICE = "price"
    COST = "cost"

    def __str__(self) -> str:
        return str(self.value)

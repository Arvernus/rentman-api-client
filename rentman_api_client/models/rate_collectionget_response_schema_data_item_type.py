from enum import Enum


class RateCollectiongetResponseSchemaDataItemType(str, Enum):
    PRICE = "price"
    COST = "cost"

    def __str__(self) -> str:
        return str(self.value)

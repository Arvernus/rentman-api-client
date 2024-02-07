from enum import Enum


class TaxClassItemputRequestSchemaType(str, Enum):
    VAT = "vat"
    TAX = "tax"
    NOTAX = "notax"

    def __str__(self) -> str:
        return str(self.value)

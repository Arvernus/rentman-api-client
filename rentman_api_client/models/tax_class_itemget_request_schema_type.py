from enum import Enum


class TaxClassItemgetRequestSchemaType(str, Enum):
    VAT = "vat"
    TAX = "tax"
    NOTAX = "notax"

    def __str__(self) -> str:
        return str(self.value)

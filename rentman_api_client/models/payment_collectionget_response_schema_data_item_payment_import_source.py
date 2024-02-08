from enum import Enum


class PaymentCollectiongetResponseSchemaDataItemPaymentImportSource(str, Enum):
    NONE = "none"
    EXACTONLINE = "exactonline"
    QUICKBOOKS = "quickbooks"
    XERO = "xero"
    PUBLICAPI = "publicapi"

    def __str__(self) -> str:
        return str(self.value)

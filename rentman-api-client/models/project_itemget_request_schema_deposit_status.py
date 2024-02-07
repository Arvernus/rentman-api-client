from enum import Enum


class ProjectItemgetRequestSchemaDepositStatus(str, Enum):
    NO_DEPOSIT_PAID = "no_deposit_paid"
    DEPOSIT_PAID = "deposit_paid"
    DEPOSIT_RETURNED = "deposit_returned"

    def __str__(self) -> str:
        return str(self.value)

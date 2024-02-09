from enum import Enum


class StocklocationItempostRequestSchemaType(str, Enum):
    PLANNABLE = "plannable"
    NONPLANNABLE = "nonplannable"

    def __str__(self) -> str:
        return str(self.value)

from enum import Enum


class ContactItemgetRequestSchemaType(str, Enum):
    PRIVATE = "private"
    COMPANY = "company"

    def __str__(self) -> str:
        return str(self.value)

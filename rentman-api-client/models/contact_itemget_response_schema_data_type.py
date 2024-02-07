from enum import Enum


class ContactItemgetResponseSchemaDataType(str, Enum):
    PRIVATE = "private"
    COMPANY = "company"

    def __str__(self) -> str:
        return str(self.value)

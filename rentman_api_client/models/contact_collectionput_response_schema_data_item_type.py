from enum import Enum


class ContactCollectionputResponseSchemaDataItemType(str, Enum):
    PRIVATE = "private"
    COMPANY = "company"

    def __str__(self) -> str:
        return str(self.value)

from enum import Enum


class ProjectRequestCollectiongetResponseSchemaDataItemStatus(str, Enum):
    ACCEPTED = "accepted"
    DECLINED = "declined"
    OPEN = "open"

    def __str__(self) -> str:
        return str(self.value)

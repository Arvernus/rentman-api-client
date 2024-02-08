from enum import Enum


class FilesCollectionpostResponseSchemaDataItemPreviewstatus(str, Enum):
    VALUE_False = "False"
    VALUE_True = "True"
    FAILED = "failed"

    def __str__(self) -> str:
        return str(self.value)

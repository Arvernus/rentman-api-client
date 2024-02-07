from enum import Enum


class FunctieCollectiongetResponseSchemaDataItemType(str, Enum):
    CREW_FUNCTION = "crew_function"
    TRANSPORT_FUNCTION = "transport_function"
    REMARK = "remark"
    SHIFT = "shift"

    def __str__(self) -> str:
        return str(self.value)

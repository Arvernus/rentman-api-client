from enum import Enum


class RateItemgetResponseSchemaDataSubtype(str, Enum):
    GLOBAL_ = "global"
    FLAT = "flat"
    TEMP = "temp"

    def __str__(self) -> str:
        return str(self.value)

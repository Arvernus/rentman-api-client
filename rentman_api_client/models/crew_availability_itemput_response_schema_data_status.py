from enum import Enum


class CrewAvailabilityItemputResponseSchemaDataStatus(str, Enum):
    B = "B"
    N = "N"
    O = "O"

    def __str__(self) -> str:
        return str(self.value)

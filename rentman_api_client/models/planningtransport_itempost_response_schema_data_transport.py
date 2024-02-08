from enum import Enum


class PlanningtransportItempostResponseSchemaDataTransport(str, Enum):
    NO_TRANSPORT = "No transport"
    ROUND_TRIP = "Round trip"
    ONLY_WAY_THERE = "Only way there"
    ONLY_WAY_BACK = "Only way back"

    def __str__(self) -> str:
        return str(self.value)

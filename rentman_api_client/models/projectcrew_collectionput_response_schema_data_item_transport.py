from enum import Enum


class ProjectcrewCollectionputResponseSchemaDataItemTransport(str, Enum):
    NO_TRANSPORT = "no_transport"
    ROUND_TRIP = "round_trip"
    ONLY_WAY_THERE = "only_way_there"
    ONLY_WAY_BACK = "only_way_back"

    def __str__(self) -> str:
        return str(self.value)

from enum import Enum


class TimeRegistrationCollectiongetResponseSchemaDataItemType(str, Enum):
    WORKED = "worked"
    HOLIDAY = "holiday"
    CORRECTION = "correction"
    SICK_LEAVE = "sick_leave"
    COMPENSATION = "compensation"

    def __str__(self) -> str:
        return str(self.value)

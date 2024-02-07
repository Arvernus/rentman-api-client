from enum import Enum


class AfspraakCollectiongetResponseSchemaDataItemRecurrenceIntervalUnit(str, Enum):
    ONCE = "once"
    DAYS = "days"
    WEEKS = "weeks"
    MONTHS = "months"
    YEARS = "years"

    def __str__(self) -> str:
        return str(self.value)

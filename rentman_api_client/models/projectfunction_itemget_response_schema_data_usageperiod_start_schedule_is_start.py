from enum import Enum


class ProjectfunctionItemgetResponseSchemaDataUsageperiodStartScheduleIsStart(str, Enum):
    END_TIME = "End time"
    START_TIME = "Start time"

    def __str__(self) -> str:
        return str(self.value)

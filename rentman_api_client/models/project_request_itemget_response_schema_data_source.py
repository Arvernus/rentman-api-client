from enum import Enum


class ProjectRequestItemgetResponseSchemaDataSource(str, Enum):
    RENTAROUND = "rentaround"
    RENTMAN = "rentman"
    ZOEF = "zoef"
    API = "api"

    def __str__(self) -> str:
        return str(self.value)

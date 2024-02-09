from enum import Enum


class EquipmentCollectionGetFilterStatus(str, Enum):
    OFFEN = "offen"
    GESCHLOSSEN = "geschlossen"
    INBEARBEITUNG = "inBearbeitung"

    def __str__(self) -> str:
        return str(self.value)

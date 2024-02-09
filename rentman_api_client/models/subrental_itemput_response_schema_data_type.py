from enum import Enum


class SubrentalItemputResponseSchemaDataType(str, Enum):
    PICK_UP = "Pick up"
    DELIVERY_AT_WAREHOUSE = "Delivery at warehouse"
    DELIVERY_AT_LOCATION = "Delivery at location"

    def __str__(self) -> str:
        return str(self.value)

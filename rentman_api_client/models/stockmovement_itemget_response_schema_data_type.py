from enum import Enum


class StockmovementItemgetResponseSchemaDataType(str, Enum):
    MANUAL = "manual"
    EQUIPMENT_LOST = "equipment_lost"
    EQUIPMENT_FOUND = "equipment_found"
    SERIAL_CREATED = "serial_created"
    SERIAL_DELETED = "serial_deleted"
    SERIAL_DEACTIVATED = "serial_deactivated"
    SERIAL_ACTIVATED_OR_FOUND = "serial_activated_or_found"
    SERIAL_LOST = "serial_lost"
    STOCK_CORRECTED_COUNTING_SERIALS = "stock_corrected_counting_serials"
    EQUIPMENT_IMPORTED = "equipment_imported"
    INITIAL_MUTATION = "initial_mutation"
    COUNTJOB_CORRECTION = "countjob_correction"
    SERIAL_TRANSFERRED = "serial_transferred"
    CASE_TRANSFER = "case_transfer"
    BULK_TRANSFER = "bulk_transfer"

    def __str__(self) -> str:
        return str(self.value)

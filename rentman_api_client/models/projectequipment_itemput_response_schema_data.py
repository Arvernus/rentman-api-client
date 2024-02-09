import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.projectequipment_itemput_response_schema_data_custom import (
    ProjectequipmentItemputResponseSchemaDataCustom,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="ProjectequipmentItemputResponseSchemaData")


@attr.s(auto_attribs=True)
class ProjectequipmentItemputResponseSchemaData:
    """All the data about the requested items"""

    id: Union[Unset, int] = UNSET
    created: Union[Unset, None, datetime.datetime] = UNSET
    modified: Union[Unset, None, datetime.datetime] = UNSET
    creator: Union[Unset, None, str] = UNSET
    displayname: Union[Unset, str] = UNSET
    equipment: Union[Unset, None, str] = UNSET
    parent: Union[Unset, None, str] = UNSET
    ledger: Union[Unset, None, str] = UNSET
    quantity: Union[Unset, str] = UNSET
    quantity_total: Union[Unset, int] = UNSET
    equipment_group: Union[Unset, str] = UNSET
    discount: Union[Unset, float] = UNSET
    is_option: Union[Unset, bool] = UNSET
    factor: Union[Unset, str] = UNSET
    order: Union[Unset, str] = UNSET
    unit_price: Union[Unset, float] = UNSET
    name: Union[Unset, str] = UNSET
    external_remark: Union[Unset, str] = UNSET
    internal_remark: Union[Unset, str] = UNSET
    delay_notified: Union[Unset, bool] = UNSET
    planperiod_start: Union[Unset, None, datetime.datetime] = UNSET
    planperiod_end: Union[Unset, None, datetime.datetime] = UNSET
    has_missings: Union[Unset, bool] = UNSET
    warehouse_reservations: Union[Unset, int] = UNSET
    subrent_reservations: Union[Unset, int] = UNSET
    serial_number_ids: Union[Unset, str] = UNSET
    custom: Union[Unset, ProjectequipmentItemputResponseSchemaDataCustom] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        created: Union[Unset, None, str] = UNSET
        if not isinstance(self.created, Unset):
            created = self.created.isoformat() if self.created else None

        modified: Union[Unset, None, str] = UNSET
        if not isinstance(self.modified, Unset):
            modified = self.modified.isoformat() if self.modified else None

        creator = self.creator
        displayname = self.displayname
        equipment = self.equipment
        parent = self.parent
        ledger = self.ledger
        quantity = self.quantity
        quantity_total = self.quantity_total
        equipment_group = self.equipment_group
        discount = self.discount
        is_option = self.is_option
        factor = self.factor
        order = self.order
        unit_price = self.unit_price
        name = self.name
        external_remark = self.external_remark
        internal_remark = self.internal_remark
        delay_notified = self.delay_notified
        planperiod_start: Union[Unset, None, str] = UNSET
        if not isinstance(self.planperiod_start, Unset):
            planperiod_start = self.planperiod_start.isoformat() if self.planperiod_start else None

        planperiod_end: Union[Unset, None, str] = UNSET
        if not isinstance(self.planperiod_end, Unset):
            planperiod_end = self.planperiod_end.isoformat() if self.planperiod_end else None

        has_missings = self.has_missings
        warehouse_reservations = self.warehouse_reservations
        subrent_reservations = self.subrent_reservations
        serial_number_ids = self.serial_number_ids
        custom: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.custom, Unset):
            custom = self.custom.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if created is not UNSET:
            field_dict["created"] = created
        if modified is not UNSET:
            field_dict["modified"] = modified
        if creator is not UNSET:
            field_dict["creator"] = creator
        if displayname is not UNSET:
            field_dict["displayname"] = displayname
        if equipment is not UNSET:
            field_dict["equipment"] = equipment
        if parent is not UNSET:
            field_dict["parent"] = parent
        if ledger is not UNSET:
            field_dict["ledger"] = ledger
        if quantity is not UNSET:
            field_dict["quantity"] = quantity
        if quantity_total is not UNSET:
            field_dict["quantity_total"] = quantity_total
        if equipment_group is not UNSET:
            field_dict["equipment_group"] = equipment_group
        if discount is not UNSET:
            field_dict["discount"] = discount
        if is_option is not UNSET:
            field_dict["is_option"] = is_option
        if factor is not UNSET:
            field_dict["factor"] = factor
        if order is not UNSET:
            field_dict["order"] = order
        if unit_price is not UNSET:
            field_dict["unit_price"] = unit_price
        if name is not UNSET:
            field_dict["name"] = name
        if external_remark is not UNSET:
            field_dict["external_remark"] = external_remark
        if internal_remark is not UNSET:
            field_dict["internal_remark"] = internal_remark
        if delay_notified is not UNSET:
            field_dict["delay_notified"] = delay_notified
        if planperiod_start is not UNSET:
            field_dict["planperiod_start"] = planperiod_start
        if planperiod_end is not UNSET:
            field_dict["planperiod_end"] = planperiod_end
        if has_missings is not UNSET:
            field_dict["has_missings"] = has_missings
        if warehouse_reservations is not UNSET:
            field_dict["warehouse_reservations"] = warehouse_reservations
        if subrent_reservations is not UNSET:
            field_dict["subrent_reservations"] = subrent_reservations
        if serial_number_ids is not UNSET:
            field_dict["serial_number_ids"] = serial_number_ids
        if custom is not UNSET:
            field_dict["custom"] = custom

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        created = None
        _created = d.pop("created", UNSET)
        if _created is not None and not isinstance(_created, Unset):
            created = isoparse(_created)

        modified = None
        _modified = d.pop("modified", UNSET)
        if _modified is not None and not isinstance(_modified, Unset):
            modified = isoparse(_modified)

        creator = d.pop("creator", UNSET)

        displayname = d.pop("displayname", UNSET)

        equipment = d.pop("equipment", UNSET)

        parent = d.pop("parent", UNSET)

        ledger = d.pop("ledger", UNSET)

        quantity = d.pop("quantity", UNSET)

        quantity_total = d.pop("quantity_total", UNSET)

        equipment_group = d.pop("equipment_group", UNSET)

        discount = d.pop("discount", UNSET)

        is_option = d.pop("is_option", UNSET)

        factor = d.pop("factor", UNSET)

        order = d.pop("order", UNSET)

        unit_price = d.pop("unit_price", UNSET)

        name = d.pop("name", UNSET)

        external_remark = d.pop("external_remark", UNSET)

        internal_remark = d.pop("internal_remark", UNSET)

        delay_notified = d.pop("delay_notified", UNSET)

        planperiod_start = None
        _planperiod_start = d.pop("planperiod_start", UNSET)
        if _planperiod_start is not None and not isinstance(_planperiod_start, Unset):
            planperiod_start = isoparse(_planperiod_start)

        planperiod_end = None
        _planperiod_end = d.pop("planperiod_end", UNSET)
        if _planperiod_end is not None and not isinstance(_planperiod_end, Unset):
            planperiod_end = isoparse(_planperiod_end)

        has_missings = d.pop("has_missings", UNSET)

        warehouse_reservations = d.pop("warehouse_reservations", UNSET)

        subrent_reservations = d.pop("subrent_reservations", UNSET)

        serial_number_ids = d.pop("serial_number_ids", UNSET)

        custom: Union[Unset, ProjectequipmentItemputResponseSchemaDataCustom] = UNSET
        _custom = d.pop("custom", UNSET)
        if not isinstance(_custom, Unset):
            custom = ProjectequipmentItemputResponseSchemaDataCustom.from_dict(_custom)

        projectequipment_itemput_response_schema_data = cls(
            id=id,
            created=created,
            modified=modified,
            creator=creator,
            displayname=displayname,
            equipment=equipment,
            parent=parent,
            ledger=ledger,
            quantity=quantity,
            quantity_total=quantity_total,
            equipment_group=equipment_group,
            discount=discount,
            is_option=is_option,
            factor=factor,
            order=order,
            unit_price=unit_price,
            name=name,
            external_remark=external_remark,
            internal_remark=internal_remark,
            delay_notified=delay_notified,
            planperiod_start=planperiod_start,
            planperiod_end=planperiod_end,
            has_missings=has_missings,
            warehouse_reservations=warehouse_reservations,
            subrent_reservations=subrent_reservations,
            serial_number_ids=serial_number_ids,
            custom=custom,
        )

        projectequipment_itemput_response_schema_data.additional_properties = d
        return projectequipment_itemput_response_schema_data

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties

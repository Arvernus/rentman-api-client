import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.project_equipment_collectionget_response_schema_data_item_custom import (
    ProjectEquipmentCollectiongetResponseSchemaDataItemCustom,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="ProjectEquipmentCollectiongetResponseSchemaDataItem")


@attr.s(auto_attribs=True)
class ProjectEquipmentCollectiongetResponseSchemaDataItem:
    """ """

    created: Union[Unset, None, datetime.datetime] = UNSET
    creator: Union[Unset, None, str] = UNSET
    custom: Union[Unset, ProjectEquipmentCollectiongetResponseSchemaDataItemCustom] = UNSET
    delay_notified: Union[Unset, bool] = UNSET
    discount: Union[Unset, float] = UNSET
    displayname: Union[Unset, str] = UNSET
    equipment: Union[Unset, None, str] = UNSET
    equipment_group: Union[Unset, str] = UNSET
    external_remark: Union[Unset, str] = UNSET
    factor: Union[Unset, str] = UNSET
    has_missings: Union[Unset, bool] = UNSET
    id: Union[Unset, int] = UNSET
    internal_remark: Union[Unset, str] = UNSET
    is_option: Union[Unset, bool] = UNSET
    ledger: Union[Unset, None, str] = UNSET
    modified: Union[Unset, None, datetime.datetime] = UNSET
    name: Union[Unset, str] = UNSET
    order: Union[Unset, str] = UNSET
    parent: Union[Unset, None, str] = UNSET
    planperiod_end: Union[Unset, None, datetime.datetime] = UNSET
    planperiod_start: Union[Unset, None, datetime.datetime] = UNSET
    quantity: Union[Unset, str] = UNSET
    quantity_total: Union[Unset, int] = UNSET
    serial_number_ids: Union[Unset, str] = UNSET
    subrent_reservations: Union[Unset, int] = UNSET
    unit_price: Union[Unset, float] = UNSET
    warehouse_reservations: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        created: Union[Unset, None, str] = UNSET
        if not isinstance(self.created, Unset):
            created = self.created.isoformat() if self.created else None

        creator = self.creator
        custom: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.custom, Unset):
            custom = self.custom.to_dict()

        delay_notified = self.delay_notified
        discount = self.discount
        displayname = self.displayname
        equipment = self.equipment
        equipment_group = self.equipment_group
        external_remark = self.external_remark
        factor = self.factor
        has_missings = self.has_missings
        id = self.id
        internal_remark = self.internal_remark
        is_option = self.is_option
        ledger = self.ledger
        modified: Union[Unset, None, str] = UNSET
        if not isinstance(self.modified, Unset):
            modified = self.modified.isoformat() if self.modified else None

        name = self.name
        order = self.order
        parent = self.parent
        planperiod_end: Union[Unset, None, str] = UNSET
        if not isinstance(self.planperiod_end, Unset):
            planperiod_end = self.planperiod_end.isoformat() if self.planperiod_end else None

        planperiod_start: Union[Unset, None, str] = UNSET
        if not isinstance(self.planperiod_start, Unset):
            planperiod_start = self.planperiod_start.isoformat() if self.planperiod_start else None

        quantity = self.quantity
        quantity_total = self.quantity_total
        serial_number_ids = self.serial_number_ids
        subrent_reservations = self.subrent_reservations
        unit_price = self.unit_price
        warehouse_reservations = self.warehouse_reservations

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if created is not UNSET:
            field_dict["created"] = created
        if creator is not UNSET:
            field_dict["creator"] = creator
        if custom is not UNSET:
            field_dict["custom"] = custom
        if delay_notified is not UNSET:
            field_dict["delay_notified"] = delay_notified
        if discount is not UNSET:
            field_dict["discount"] = discount
        if displayname is not UNSET:
            field_dict["displayname"] = displayname
        if equipment is not UNSET:
            field_dict["equipment"] = equipment
        if equipment_group is not UNSET:
            field_dict["equipment_group"] = equipment_group
        if external_remark is not UNSET:
            field_dict["external_remark"] = external_remark
        if factor is not UNSET:
            field_dict["factor"] = factor
        if has_missings is not UNSET:
            field_dict["has_missings"] = has_missings
        if id is not UNSET:
            field_dict["id"] = id
        if internal_remark is not UNSET:
            field_dict["internal_remark"] = internal_remark
        if is_option is not UNSET:
            field_dict["is_option"] = is_option
        if ledger is not UNSET:
            field_dict["ledger"] = ledger
        if modified is not UNSET:
            field_dict["modified"] = modified
        if name is not UNSET:
            field_dict["name"] = name
        if order is not UNSET:
            field_dict["order"] = order
        if parent is not UNSET:
            field_dict["parent"] = parent
        if planperiod_end is not UNSET:
            field_dict["planperiod_end"] = planperiod_end
        if planperiod_start is not UNSET:
            field_dict["planperiod_start"] = planperiod_start
        if quantity is not UNSET:
            field_dict["quantity"] = quantity
        if quantity_total is not UNSET:
            field_dict["quantity_total"] = quantity_total
        if serial_number_ids is not UNSET:
            field_dict["serial_number_ids"] = serial_number_ids
        if subrent_reservations is not UNSET:
            field_dict["subrent_reservations"] = subrent_reservations
        if unit_price is not UNSET:
            field_dict["unit_price"] = unit_price
        if warehouse_reservations is not UNSET:
            field_dict["warehouse_reservations"] = warehouse_reservations

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        created = None
        _created = d.pop("created", UNSET)
        if _created is not None and not isinstance(_created, Unset):
            created = isoparse(_created)

        creator = d.pop("creator", UNSET)

        custom: Union[Unset, ProjectEquipmentCollectiongetResponseSchemaDataItemCustom] = UNSET
        _custom = d.pop("custom", UNSET)
        if not isinstance(_custom, Unset):
            custom = ProjectEquipmentCollectiongetResponseSchemaDataItemCustom.from_dict(_custom)

        delay_notified = d.pop("delay_notified", UNSET)

        discount = d.pop("discount", UNSET)

        displayname = d.pop("displayname", UNSET)

        equipment = d.pop("equipment", UNSET)

        equipment_group = d.pop("equipment_group", UNSET)

        external_remark = d.pop("external_remark", UNSET)

        factor = d.pop("factor", UNSET)

        has_missings = d.pop("has_missings", UNSET)

        id = d.pop("id", UNSET)

        internal_remark = d.pop("internal_remark", UNSET)

        is_option = d.pop("is_option", UNSET)

        ledger = d.pop("ledger", UNSET)

        modified = None
        _modified = d.pop("modified", UNSET)
        if _modified is not None and not isinstance(_modified, Unset):
            modified = isoparse(_modified)

        name = d.pop("name", UNSET)

        order = d.pop("order", UNSET)

        parent = d.pop("parent", UNSET)

        planperiod_end = None
        _planperiod_end = d.pop("planperiod_end", UNSET)
        if _planperiod_end is not None and not isinstance(_planperiod_end, Unset):
            planperiod_end = isoparse(_planperiod_end)

        planperiod_start = None
        _planperiod_start = d.pop("planperiod_start", UNSET)
        if _planperiod_start is not None and not isinstance(_planperiod_start, Unset):
            planperiod_start = isoparse(_planperiod_start)

        quantity = d.pop("quantity", UNSET)

        quantity_total = d.pop("quantity_total", UNSET)

        serial_number_ids = d.pop("serial_number_ids", UNSET)

        subrent_reservations = d.pop("subrent_reservations", UNSET)

        unit_price = d.pop("unit_price", UNSET)

        warehouse_reservations = d.pop("warehouse_reservations", UNSET)

        project_equipment_collectionget_response_schema_data_item = cls(
            created=created,
            creator=creator,
            custom=custom,
            delay_notified=delay_notified,
            discount=discount,
            displayname=displayname,
            equipment=equipment,
            equipment_group=equipment_group,
            external_remark=external_remark,
            factor=factor,
            has_missings=has_missings,
            id=id,
            internal_remark=internal_remark,
            is_option=is_option,
            ledger=ledger,
            modified=modified,
            name=name,
            order=order,
            parent=parent,
            planperiod_end=planperiod_end,
            planperiod_start=planperiod_start,
            quantity=quantity,
            quantity_total=quantity_total,
            serial_number_ids=serial_number_ids,
            subrent_reservations=subrent_reservations,
            unit_price=unit_price,
            warehouse_reservations=warehouse_reservations,
        )

        project_equipment_collectionget_response_schema_data_item.additional_properties = d
        return project_equipment_collectionget_response_schema_data_item

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

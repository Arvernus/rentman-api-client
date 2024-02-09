import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="SubrentalEquipmentItemgetResponseSchemaData")


@attr.s(auto_attribs=True)
class SubrentalEquipmentItemgetResponseSchemaData:
    """All the data about the requested items"""

    created: Union[Unset, None, datetime.datetime] = UNSET
    creator: Union[Unset, None, str] = UNSET
    discount: Union[Unset, float] = UNSET
    displayname: Union[Unset, str] = UNSET
    equipment: Union[Unset, None, str] = UNSET
    factor: Union[Unset, str] = UNSET
    id: Union[Unset, int] = UNSET
    lineprice: Union[Unset, float] = UNSET
    modified: Union[Unset, None, datetime.datetime] = UNSET
    name: Union[Unset, str] = UNSET
    order: Union[Unset, str] = UNSET
    parent: Union[Unset, None, str] = UNSET
    planperiod_end: Union[Unset, None, datetime.datetime] = UNSET
    planperiod_start: Union[Unset, None, datetime.datetime] = UNSET
    quantity: Union[Unset, int] = UNSET
    quantity_total: Union[Unset, int] = UNSET
    remark: Union[Unset, str] = UNSET
    subrental_group: Union[Unset, str] = UNSET
    supplier_planningmateriaal: Union[Unset, None, str] = UNSET
    unit_price: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        created: Union[Unset, None, str] = UNSET
        if not isinstance(self.created, Unset):
            created = self.created.isoformat() if self.created else None

        creator = self.creator
        discount = self.discount
        displayname = self.displayname
        equipment = self.equipment
        factor = self.factor
        id = self.id
        lineprice = self.lineprice
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
        remark = self.remark
        subrental_group = self.subrental_group
        supplier_planningmateriaal = self.supplier_planningmateriaal
        unit_price = self.unit_price

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if created is not UNSET:
            field_dict["created"] = created
        if creator is not UNSET:
            field_dict["creator"] = creator
        if discount is not UNSET:
            field_dict["discount"] = discount
        if displayname is not UNSET:
            field_dict["displayname"] = displayname
        if equipment is not UNSET:
            field_dict["equipment"] = equipment
        if factor is not UNSET:
            field_dict["factor"] = factor
        if id is not UNSET:
            field_dict["id"] = id
        if lineprice is not UNSET:
            field_dict["lineprice"] = lineprice
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
        if remark is not UNSET:
            field_dict["remark"] = remark
        if subrental_group is not UNSET:
            field_dict["subrental_group"] = subrental_group
        if supplier_planningmateriaal is not UNSET:
            field_dict["supplier_planningmateriaal"] = supplier_planningmateriaal
        if unit_price is not UNSET:
            field_dict["unit_price"] = unit_price

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        created = None
        _created = d.pop("created", UNSET)
        if _created is not None and not isinstance(_created, Unset):
            created = isoparse(_created)

        creator = d.pop("creator", UNSET)

        discount = d.pop("discount", UNSET)

        displayname = d.pop("displayname", UNSET)

        equipment = d.pop("equipment", UNSET)

        factor = d.pop("factor", UNSET)

        id = d.pop("id", UNSET)

        lineprice = d.pop("lineprice", UNSET)

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

        remark = d.pop("remark", UNSET)

        subrental_group = d.pop("subrental_group", UNSET)

        supplier_planningmateriaal = d.pop("supplier_planningmateriaal", UNSET)

        unit_price = d.pop("unit_price", UNSET)

        subrental_equipment_itemget_response_schema_data = cls(
            created=created,
            creator=creator,
            discount=discount,
            displayname=displayname,
            equipment=equipment,
            factor=factor,
            id=id,
            lineprice=lineprice,
            modified=modified,
            name=name,
            order=order,
            parent=parent,
            planperiod_end=planperiod_end,
            planperiod_start=planperiod_start,
            quantity=quantity,
            quantity_total=quantity_total,
            remark=remark,
            subrental_group=subrental_group,
            supplier_planningmateriaal=supplier_planningmateriaal,
            unit_price=unit_price,
        )

        subrental_equipment_itemget_response_schema_data.additional_properties = d
        return subrental_equipment_itemget_response_schema_data

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

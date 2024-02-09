import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="SubrentalequipmentItemgetResponseSchemaData")


@attr.s(auto_attribs=True)
class SubrentalequipmentItemgetResponseSchemaData:
    """All the data about the requested items"""

    id: Union[Unset, int] = UNSET
    created: Union[Unset, None, datetime.datetime] = UNSET
    modified: Union[Unset, None, datetime.datetime] = UNSET
    creator: Union[Unset, None, str] = UNSET
    displayname: Union[Unset, str] = UNSET
    subrental_group: Union[Unset, str] = UNSET
    equipment: Union[Unset, None, str] = UNSET
    parent: Union[Unset, None, str] = UNSET
    planperiod_start: Union[Unset, None, datetime.datetime] = UNSET
    planperiod_end: Union[Unset, None, datetime.datetime] = UNSET
    name: Union[Unset, str] = UNSET
    quantity: Union[Unset, int] = UNSET
    quantity_total: Union[Unset, int] = UNSET
    unit_price: Union[Unset, float] = UNSET
    discount: Union[Unset, float] = UNSET
    factor: Union[Unset, str] = UNSET
    order: Union[Unset, str] = UNSET
    remark: Union[Unset, str] = UNSET
    lineprice: Union[Unset, float] = UNSET
    supplier_planningmateriaal: Union[Unset, None, str] = UNSET
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
        subrental_group = self.subrental_group
        equipment = self.equipment
        parent = self.parent
        planperiod_start: Union[Unset, None, str] = UNSET
        if not isinstance(self.planperiod_start, Unset):
            planperiod_start = self.planperiod_start.isoformat() if self.planperiod_start else None

        planperiod_end: Union[Unset, None, str] = UNSET
        if not isinstance(self.planperiod_end, Unset):
            planperiod_end = self.planperiod_end.isoformat() if self.planperiod_end else None

        name = self.name
        quantity = self.quantity
        quantity_total = self.quantity_total
        unit_price = self.unit_price
        discount = self.discount
        factor = self.factor
        order = self.order
        remark = self.remark
        lineprice = self.lineprice
        supplier_planningmateriaal = self.supplier_planningmateriaal

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
        if subrental_group is not UNSET:
            field_dict["subrental_group"] = subrental_group
        if equipment is not UNSET:
            field_dict["equipment"] = equipment
        if parent is not UNSET:
            field_dict["parent"] = parent
        if planperiod_start is not UNSET:
            field_dict["planperiod_start"] = planperiod_start
        if planperiod_end is not UNSET:
            field_dict["planperiod_end"] = planperiod_end
        if name is not UNSET:
            field_dict["name"] = name
        if quantity is not UNSET:
            field_dict["quantity"] = quantity
        if quantity_total is not UNSET:
            field_dict["quantity_total"] = quantity_total
        if unit_price is not UNSET:
            field_dict["unit_price"] = unit_price
        if discount is not UNSET:
            field_dict["discount"] = discount
        if factor is not UNSET:
            field_dict["factor"] = factor
        if order is not UNSET:
            field_dict["order"] = order
        if remark is not UNSET:
            field_dict["remark"] = remark
        if lineprice is not UNSET:
            field_dict["lineprice"] = lineprice
        if supplier_planningmateriaal is not UNSET:
            field_dict["supplier_planningmateriaal"] = supplier_planningmateriaal

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

        subrental_group = d.pop("subrental_group", UNSET)

        equipment = d.pop("equipment", UNSET)

        parent = d.pop("parent", UNSET)

        planperiod_start = None
        _planperiod_start = d.pop("planperiod_start", UNSET)
        if _planperiod_start is not None and not isinstance(_planperiod_start, Unset):
            planperiod_start = isoparse(_planperiod_start)

        planperiod_end = None
        _planperiod_end = d.pop("planperiod_end", UNSET)
        if _planperiod_end is not None and not isinstance(_planperiod_end, Unset):
            planperiod_end = isoparse(_planperiod_end)

        name = d.pop("name", UNSET)

        quantity = d.pop("quantity", UNSET)

        quantity_total = d.pop("quantity_total", UNSET)

        unit_price = d.pop("unit_price", UNSET)

        discount = d.pop("discount", UNSET)

        factor = d.pop("factor", UNSET)

        order = d.pop("order", UNSET)

        remark = d.pop("remark", UNSET)

        lineprice = d.pop("lineprice", UNSET)

        supplier_planningmateriaal = d.pop("supplier_planningmateriaal", UNSET)

        subrentalequipment_itemget_response_schema_data = cls(
            id=id,
            created=created,
            modified=modified,
            creator=creator,
            displayname=displayname,
            subrental_group=subrental_group,
            equipment=equipment,
            parent=parent,
            planperiod_start=planperiod_start,
            planperiod_end=planperiod_end,
            name=name,
            quantity=quantity,
            quantity_total=quantity_total,
            unit_price=unit_price,
            discount=discount,
            factor=factor,
            order=order,
            remark=remark,
            lineprice=lineprice,
            supplier_planningmateriaal=supplier_planningmateriaal,
        )

        subrentalequipment_itemget_response_schema_data.additional_properties = d
        return subrentalequipment_itemget_response_schema_data

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

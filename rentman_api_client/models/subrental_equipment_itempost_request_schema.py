import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="SubrentalEquipmentItempostRequestSchema")


@attr.s(auto_attribs=True)
class SubrentalEquipmentItempostRequestSchema:
    """ """

    discount: Union[Unset, float] = UNSET
    equipment: Union[Unset, None, str] = UNSET
    factor: Union[Unset, str] = UNSET
    lineprice: Union[Unset, float] = UNSET
    name: Union[Unset, str] = UNSET
    order: Union[Unset, str] = UNSET
    parent: Union[Unset, None, str] = UNSET
    planperiod_end: Union[Unset, None, datetime.datetime] = UNSET
    planperiod_start: Union[Unset, None, datetime.datetime] = UNSET
    quantity: Union[Unset, int] = UNSET
    quantity_total: Union[Unset, int] = UNSET
    remark: Union[Unset, str] = UNSET
    supplier_planningmateriaal: Union[Unset, None, str] = UNSET
    unit_price: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        discount = self.discount
        equipment = self.equipment
        factor = self.factor
        lineprice = self.lineprice
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
        supplier_planningmateriaal = self.supplier_planningmateriaal
        unit_price = self.unit_price

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if discount is not UNSET:
            field_dict["discount"] = discount
        if equipment is not UNSET:
            field_dict["equipment"] = equipment
        if factor is not UNSET:
            field_dict["factor"] = factor
        if lineprice is not UNSET:
            field_dict["lineprice"] = lineprice
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
        if supplier_planningmateriaal is not UNSET:
            field_dict["supplier_planningmateriaal"] = supplier_planningmateriaal
        if unit_price is not UNSET:
            field_dict["unit_price"] = unit_price

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        discount = d.pop("discount", UNSET)

        equipment = d.pop("equipment", UNSET)

        factor = d.pop("factor", UNSET)

        lineprice = d.pop("lineprice", UNSET)

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

        supplier_planningmateriaal = d.pop("supplier_planningmateriaal", UNSET)

        unit_price = d.pop("unit_price", UNSET)

        subrental_equipment_itempost_request_schema = cls(
            discount=discount,
            equipment=equipment,
            factor=factor,
            lineprice=lineprice,
            name=name,
            order=order,
            parent=parent,
            planperiod_end=planperiod_end,
            planperiod_start=planperiod_start,
            quantity=quantity,
            quantity_total=quantity_total,
            remark=remark,
            supplier_planningmateriaal=supplier_planningmateriaal,
            unit_price=unit_price,
        )

        subrental_equipment_itempost_request_schema.additional_properties = d
        return subrental_equipment_itempost_request_schema

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

from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.planningmateriaal_itemput_request_schema_custom import PlanningmateriaalItemputRequestSchemaCustom
from ..types import UNSET, Unset

T = TypeVar("T", bound="PlanningmateriaalItemputRequestSchema")


@attr.s(auto_attribs=True)
class PlanningmateriaalItemputRequestSchema:
    """ """

    equipment: Union[Unset, None, str] = UNSET
    parent: Union[Unset, None, str] = UNSET
    ledger: Union[Unset, None, str] = UNSET
    quantity: Union[Unset, str] = UNSET
    quantity_total: Union[Unset, int] = UNSET
    discount: Union[Unset, float] = UNSET
    is_option: Union[Unset, bool] = UNSET
    factor: Union[Unset, str] = UNSET
    order: Union[Unset, str] = UNSET
    unit_price: Union[Unset, float] = UNSET
    name: Union[Unset, str] = UNSET
    external_remark: Union[Unset, str] = UNSET
    internal_remark: Union[Unset, str] = UNSET
    delay_notified: Union[Unset, bool] = UNSET
    custom: Union[Unset, PlanningmateriaalItemputRequestSchemaCustom] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        equipment = self.equipment
        parent = self.parent
        ledger = self.ledger
        quantity = self.quantity
        quantity_total = self.quantity_total
        discount = self.discount
        is_option = self.is_option
        factor = self.factor
        order = self.order
        unit_price = self.unit_price
        name = self.name
        external_remark = self.external_remark
        internal_remark = self.internal_remark
        delay_notified = self.delay_notified
        custom: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.custom, Unset):
            custom = self.custom.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
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
        if custom is not UNSET:
            field_dict["custom"] = custom

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        equipment = d.pop("equipment", UNSET)

        parent = d.pop("parent", UNSET)

        ledger = d.pop("ledger", UNSET)

        quantity = d.pop("quantity", UNSET)

        quantity_total = d.pop("quantity_total", UNSET)

        discount = d.pop("discount", UNSET)

        is_option = d.pop("is_option", UNSET)

        factor = d.pop("factor", UNSET)

        order = d.pop("order", UNSET)

        unit_price = d.pop("unit_price", UNSET)

        name = d.pop("name", UNSET)

        external_remark = d.pop("external_remark", UNSET)

        internal_remark = d.pop("internal_remark", UNSET)

        delay_notified = d.pop("delay_notified", UNSET)

        custom: Union[Unset, PlanningmateriaalItemputRequestSchemaCustom] = UNSET
        _custom = d.pop("custom", UNSET)
        if not isinstance(_custom, Unset):
            custom = PlanningmateriaalItemputRequestSchemaCustom.from_dict(_custom)

        planningmateriaal_itemput_request_schema = cls(
            equipment=equipment,
            parent=parent,
            ledger=ledger,
            quantity=quantity,
            quantity_total=quantity_total,
            discount=discount,
            is_option=is_option,
            factor=factor,
            order=order,
            unit_price=unit_price,
            name=name,
            external_remark=external_remark,
            internal_remark=internal_remark,
            delay_notified=delay_notified,
            custom=custom,
        )

        planningmateriaal_itemput_request_schema.additional_properties = d
        return planningmateriaal_itemput_request_schema

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

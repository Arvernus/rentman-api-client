from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.project_equipment_itemput_request_schema_custom import ProjectEquipmentItemputRequestSchemaCustom
from ..types import UNSET, Unset

T = TypeVar("T", bound="ProjectEquipmentItemputRequestSchema")


@attr.s(auto_attribs=True)
class ProjectEquipmentItemputRequestSchema:
    """ """

    custom: Union[Unset, ProjectEquipmentItemputRequestSchemaCustom] = UNSET
    delay_notified: Union[Unset, bool] = UNSET
    discount: Union[Unset, float] = UNSET
    equipment: Union[Unset, None, str] = UNSET
    external_remark: Union[Unset, str] = UNSET
    factor: Union[Unset, str] = UNSET
    internal_remark: Union[Unset, str] = UNSET
    is_option: Union[Unset, bool] = UNSET
    ledger: Union[Unset, None, str] = UNSET
    name: Union[Unset, str] = UNSET
    order: Union[Unset, str] = UNSET
    parent: Union[Unset, None, str] = UNSET
    quantity: Union[Unset, str] = UNSET
    quantity_total: Union[Unset, int] = UNSET
    unit_price: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        custom: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.custom, Unset):
            custom = self.custom.to_dict()

        delay_notified = self.delay_notified
        discount = self.discount
        equipment = self.equipment
        external_remark = self.external_remark
        factor = self.factor
        internal_remark = self.internal_remark
        is_option = self.is_option
        ledger = self.ledger
        name = self.name
        order = self.order
        parent = self.parent
        quantity = self.quantity
        quantity_total = self.quantity_total
        unit_price = self.unit_price

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if custom is not UNSET:
            field_dict["custom"] = custom
        if delay_notified is not UNSET:
            field_dict["delay_notified"] = delay_notified
        if discount is not UNSET:
            field_dict["discount"] = discount
        if equipment is not UNSET:
            field_dict["equipment"] = equipment
        if external_remark is not UNSET:
            field_dict["external_remark"] = external_remark
        if factor is not UNSET:
            field_dict["factor"] = factor
        if internal_remark is not UNSET:
            field_dict["internal_remark"] = internal_remark
        if is_option is not UNSET:
            field_dict["is_option"] = is_option
        if ledger is not UNSET:
            field_dict["ledger"] = ledger
        if name is not UNSET:
            field_dict["name"] = name
        if order is not UNSET:
            field_dict["order"] = order
        if parent is not UNSET:
            field_dict["parent"] = parent
        if quantity is not UNSET:
            field_dict["quantity"] = quantity
        if quantity_total is not UNSET:
            field_dict["quantity_total"] = quantity_total
        if unit_price is not UNSET:
            field_dict["unit_price"] = unit_price

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        custom: Union[Unset, ProjectEquipmentItemputRequestSchemaCustom] = UNSET
        _custom = d.pop("custom", UNSET)
        if not isinstance(_custom, Unset):
            custom = ProjectEquipmentItemputRequestSchemaCustom.from_dict(_custom)

        delay_notified = d.pop("delay_notified", UNSET)

        discount = d.pop("discount", UNSET)

        equipment = d.pop("equipment", UNSET)

        external_remark = d.pop("external_remark", UNSET)

        factor = d.pop("factor", UNSET)

        internal_remark = d.pop("internal_remark", UNSET)

        is_option = d.pop("is_option", UNSET)

        ledger = d.pop("ledger", UNSET)

        name = d.pop("name", UNSET)

        order = d.pop("order", UNSET)

        parent = d.pop("parent", UNSET)

        quantity = d.pop("quantity", UNSET)

        quantity_total = d.pop("quantity_total", UNSET)

        unit_price = d.pop("unit_price", UNSET)

        project_equipment_itemput_request_schema = cls(
            custom=custom,
            delay_notified=delay_notified,
            discount=discount,
            equipment=equipment,
            external_remark=external_remark,
            factor=factor,
            internal_remark=internal_remark,
            is_option=is_option,
            ledger=ledger,
            name=name,
            order=order,
            parent=parent,
            quantity=quantity,
            quantity_total=quantity_total,
            unit_price=unit_price,
        )

        project_equipment_itemput_request_schema.additional_properties = d
        return project_equipment_itemput_request_schema

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

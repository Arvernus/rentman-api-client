from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ProjectRequestEquipmentItempostRequestSchema")


@attr.s(auto_attribs=True)
class ProjectRequestEquipmentItempostRequestSchema:
    """ """

    discount: Union[Unset, float] = UNSET
    external_remark: Union[Unset, str] = UNSET
    factor: Union[Unset, str] = UNSET
    is_comment: Union[Unset, bool] = UNSET
    is_kit: Union[Unset, bool] = UNSET
    linked_equipment: Union[Unset, None, str] = UNSET
    name: Union[Unset, str] = UNSET
    order: Union[Unset, str] = UNSET
    parent: Union[Unset, None, str] = UNSET
    quantity: Union[Unset, int] = UNSET
    quantity_total: Union[Unset, int] = UNSET
    unit_price: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        discount = self.discount
        external_remark = self.external_remark
        factor = self.factor
        is_comment = self.is_comment
        is_kit = self.is_kit
        linked_equipment = self.linked_equipment
        name = self.name
        order = self.order
        parent = self.parent
        quantity = self.quantity
        quantity_total = self.quantity_total
        unit_price = self.unit_price

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if discount is not UNSET:
            field_dict["discount"] = discount
        if external_remark is not UNSET:
            field_dict["external_remark"] = external_remark
        if factor is not UNSET:
            field_dict["factor"] = factor
        if is_comment is not UNSET:
            field_dict["is_comment"] = is_comment
        if is_kit is not UNSET:
            field_dict["is_kit"] = is_kit
        if linked_equipment is not UNSET:
            field_dict["linked_equipment"] = linked_equipment
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
        discount = d.pop("discount", UNSET)

        external_remark = d.pop("external_remark", UNSET)

        factor = d.pop("factor", UNSET)

        is_comment = d.pop("is_comment", UNSET)

        is_kit = d.pop("is_kit", UNSET)

        linked_equipment = d.pop("linked_equipment", UNSET)

        name = d.pop("name", UNSET)

        order = d.pop("order", UNSET)

        parent = d.pop("parent", UNSET)

        quantity = d.pop("quantity", UNSET)

        quantity_total = d.pop("quantity_total", UNSET)

        unit_price = d.pop("unit_price", UNSET)

        project_request_equipment_itempost_request_schema = cls(
            discount=discount,
            external_remark=external_remark,
            factor=factor,
            is_comment=is_comment,
            is_kit=is_kit,
            linked_equipment=linked_equipment,
            name=name,
            order=order,
            parent=parent,
            quantity=quantity,
            quantity_total=quantity_total,
            unit_price=unit_price,
        )

        project_request_equipment_itempost_request_schema.additional_properties = d
        return project_request_equipment_itempost_request_schema

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

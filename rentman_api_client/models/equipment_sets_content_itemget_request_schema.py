from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.equipment_sets_content_itemget_request_schema_is_fixed import (
    EquipmentSetsContentItemgetRequestSchemaIsFixed,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="EquipmentSetsContentItemgetRequestSchema")


@attr.s(auto_attribs=True)
class EquipmentSetsContentItemgetRequestSchema:
    """ """

    equipment: str
    is_fixed: Union[Unset, EquipmentSetsContentItemgetRequestSchemaIsFixed] = UNSET
    order: Union[Unset, str] = UNSET
    quantity: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        equipment = self.equipment
        is_fixed: Union[Unset, str] = UNSET
        if not isinstance(self.is_fixed, Unset):
            is_fixed = self.is_fixed.value

        order = self.order
        quantity = self.quantity

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "equipment": equipment,
            }
        )
        if is_fixed is not UNSET:
            field_dict["is_fixed"] = is_fixed
        if order is not UNSET:
            field_dict["order"] = order
        if quantity is not UNSET:
            field_dict["quantity"] = quantity

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        equipment = d.pop("equipment")

        is_fixed: Union[Unset, EquipmentSetsContentItemgetRequestSchemaIsFixed] = UNSET
        _is_fixed = d.pop("is_fixed", UNSET)
        if not isinstance(_is_fixed, Unset):
            is_fixed = EquipmentSetsContentItemgetRequestSchemaIsFixed(_is_fixed)

        order = d.pop("order", UNSET)

        quantity = d.pop("quantity", UNSET)

        equipment_sets_content_itemget_request_schema = cls(
            equipment=equipment,
            is_fixed=is_fixed,
            order=order,
            quantity=quantity,
        )

        equipment_sets_content_itemget_request_schema.additional_properties = d
        return equipment_sets_content_itemget_request_schema

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

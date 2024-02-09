from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.equipmentsetscontent_itemget_request_schema_is_fixed import (
    EquipmentsetscontentItemgetRequestSchemaIsFixed,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="EquipmentsetscontentItemgetRequestSchema")


@attr.s(auto_attribs=True)
class EquipmentsetscontentItemgetRequestSchema:
    """ """

    equipment: str
    quantity: Union[Unset, str] = UNSET
    order: Union[Unset, str] = UNSET
    is_fixed: Union[Unset, EquipmentsetscontentItemgetRequestSchemaIsFixed] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        equipment = self.equipment
        quantity = self.quantity
        order = self.order
        is_fixed: Union[Unset, str] = UNSET
        if not isinstance(self.is_fixed, Unset):
            is_fixed = self.is_fixed.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "equipment": equipment,
            }
        )
        if quantity is not UNSET:
            field_dict["quantity"] = quantity
        if order is not UNSET:
            field_dict["order"] = order
        if is_fixed is not UNSET:
            field_dict["is_fixed"] = is_fixed

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        equipment = d.pop("equipment")

        quantity = d.pop("quantity", UNSET)

        order = d.pop("order", UNSET)

        is_fixed: Union[Unset, EquipmentsetscontentItemgetRequestSchemaIsFixed] = UNSET
        _is_fixed = d.pop("is_fixed", UNSET)
        if not isinstance(_is_fixed, Unset):
            is_fixed = EquipmentsetscontentItemgetRequestSchemaIsFixed(_is_fixed)

        equipmentsetscontent_itemget_request_schema = cls(
            equipment=equipment,
            quantity=quantity,
            order=order,
            is_fixed=is_fixed,
        )

        equipmentsetscontent_itemget_request_schema.additional_properties = d
        return equipmentsetscontent_itemget_request_schema

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

from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="SubrentalEquipmentGroupItemputRequestSchema")


@attr.s(auto_attribs=True)
class SubrentalEquipmentGroupItemputRequestSchema:
    """ """

    name: Union[Unset, str] = UNSET
    order: Union[Unset, str] = UNSET
    supplier_category: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        order = self.order
        supplier_category = self.supplier_category

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if order is not UNSET:
            field_dict["order"] = order
        if supplier_category is not UNSET:
            field_dict["supplier_category"] = supplier_category

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name", UNSET)

        order = d.pop("order", UNSET)

        supplier_category = d.pop("supplier_category", UNSET)

        subrental_equipment_group_itemput_request_schema = cls(
            name=name,
            order=order,
            supplier_category=supplier_category,
        )

        subrental_equipment_group_itemput_request_schema.additional_properties = d
        return subrental_equipment_group_itemput_request_schema

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

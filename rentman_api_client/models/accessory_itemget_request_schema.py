from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="AccessoryItemgetRequestSchema")


@attr.s(auto_attribs=True)
class AccessoryItemgetRequestSchema:
    """ """

    equipment: Union[Unset, None, str] = UNSET
    quantity: Union[Unset, int] = UNSET
    automatic: Union[Unset, bool] = UNSET
    skip: Union[Unset, bool] = UNSET
    is_free: Union[Unset, bool] = UNSET
    order: Union[Unset, str] = UNSET
    add_as_new_line: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        equipment = self.equipment
        quantity = self.quantity
        automatic = self.automatic
        skip = self.skip
        is_free = self.is_free
        order = self.order
        add_as_new_line = self.add_as_new_line

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if equipment is not UNSET:
            field_dict["equipment"] = equipment
        if quantity is not UNSET:
            field_dict["quantity"] = quantity
        if automatic is not UNSET:
            field_dict["automatic"] = automatic
        if skip is not UNSET:
            field_dict["skip"] = skip
        if is_free is not UNSET:
            field_dict["is_free"] = is_free
        if order is not UNSET:
            field_dict["order"] = order
        if add_as_new_line is not UNSET:
            field_dict["add_as_new_line"] = add_as_new_line

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        equipment = d.pop("equipment", UNSET)

        quantity = d.pop("quantity", UNSET)

        automatic = d.pop("automatic", UNSET)

        skip = d.pop("skip", UNSET)

        is_free = d.pop("is_free", UNSET)

        order = d.pop("order", UNSET)

        add_as_new_line = d.pop("add_as_new_line", UNSET)

        accessory_itemget_request_schema = cls(
            equipment=equipment,
            quantity=quantity,
            automatic=automatic,
            skip=skip,
            is_free=is_free,
            order=order,
            add_as_new_line=add_as_new_line,
        )

        accessory_itemget_request_schema.additional_properties = d
        return accessory_itemget_request_schema

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

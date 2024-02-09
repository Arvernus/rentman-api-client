from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="AccessoryItempostRequestSchema")


@attr.s(auto_attribs=True)
class AccessoryItempostRequestSchema:
    """ """

    add_as_new_line: Union[Unset, bool] = UNSET
    automatic: Union[Unset, bool] = UNSET
    equipment: Union[Unset, None, str] = UNSET
    is_free: Union[Unset, bool] = UNSET
    order: Union[Unset, str] = UNSET
    quantity: Union[Unset, int] = UNSET
    skip: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        add_as_new_line = self.add_as_new_line
        automatic = self.automatic
        equipment = self.equipment
        is_free = self.is_free
        order = self.order
        quantity = self.quantity
        skip = self.skip

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if add_as_new_line is not UNSET:
            field_dict["add_as_new_line"] = add_as_new_line
        if automatic is not UNSET:
            field_dict["automatic"] = automatic
        if equipment is not UNSET:
            field_dict["equipment"] = equipment
        if is_free is not UNSET:
            field_dict["is_free"] = is_free
        if order is not UNSET:
            field_dict["order"] = order
        if quantity is not UNSET:
            field_dict["quantity"] = quantity
        if skip is not UNSET:
            field_dict["skip"] = skip

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        add_as_new_line = d.pop("add_as_new_line", UNSET)

        automatic = d.pop("automatic", UNSET)

        equipment = d.pop("equipment", UNSET)

        is_free = d.pop("is_free", UNSET)

        order = d.pop("order", UNSET)

        quantity = d.pop("quantity", UNSET)

        skip = d.pop("skip", UNSET)

        accessory_itempost_request_schema = cls(
            add_as_new_line=add_as_new_line,
            automatic=automatic,
            equipment=equipment,
            is_free=is_free,
            order=order,
            quantity=quantity,
            skip=skip,
        )

        accessory_itempost_request_schema.additional_properties = d
        return accessory_itempost_request_schema

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

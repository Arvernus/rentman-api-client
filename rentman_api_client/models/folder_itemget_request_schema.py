from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.folder_itemget_request_schema_itemtype import FolderItemgetRequestSchemaItemtype
from ..types import UNSET, Unset

T = TypeVar("T", bound="FolderItemgetRequestSchema")


@attr.s(auto_attribs=True)
class FolderItemgetRequestSchema:
    """ """

    parent: Union[Unset, None, str] = UNSET
    name: Union[Unset, str] = UNSET
    order: Union[Unset, str] = UNSET
    itemtype: Union[Unset, FolderItemgetRequestSchemaItemtype] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        parent = self.parent
        name = self.name
        order = self.order
        itemtype: Union[Unset, str] = UNSET
        if not isinstance(self.itemtype, Unset):
            itemtype = self.itemtype.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if parent is not UNSET:
            field_dict["parent"] = parent
        if name is not UNSET:
            field_dict["name"] = name
        if order is not UNSET:
            field_dict["order"] = order
        if itemtype is not UNSET:
            field_dict["itemtype"] = itemtype

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        parent = d.pop("parent", UNSET)

        name = d.pop("name", UNSET)

        order = d.pop("order", UNSET)

        itemtype: Union[Unset, FolderItemgetRequestSchemaItemtype] = UNSET
        _itemtype = d.pop("itemtype", UNSET)
        if not isinstance(_itemtype, Unset):
            itemtype = FolderItemgetRequestSchemaItemtype(_itemtype)

        folder_itemget_request_schema = cls(
            parent=parent,
            name=name,
            order=order,
            itemtype=itemtype,
        )

        folder_itemget_request_schema.additional_properties = d
        return folder_itemget_request_schema

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

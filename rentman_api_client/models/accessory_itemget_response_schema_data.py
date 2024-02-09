import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="AccessoryItemgetResponseSchemaData")


@attr.s(auto_attribs=True)
class AccessoryItemgetResponseSchemaData:
    """All the data about the requested items"""

    add_as_new_line: Union[Unset, bool] = UNSET
    automatic: Union[Unset, bool] = UNSET
    created: Union[Unset, None, datetime.datetime] = UNSET
    creator: Union[Unset, None, str] = UNSET
    displayname: Union[Unset, str] = UNSET
    equipment: Union[Unset, None, str] = UNSET
    id: Union[Unset, int] = UNSET
    is_free: Union[Unset, bool] = UNSET
    modified: Union[Unset, None, datetime.datetime] = UNSET
    order: Union[Unset, str] = UNSET
    parent_equipment: Union[Unset, str] = UNSET
    quantity: Union[Unset, int] = UNSET
    skip: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        add_as_new_line = self.add_as_new_line
        automatic = self.automatic
        created: Union[Unset, None, str] = UNSET
        if not isinstance(self.created, Unset):
            created = self.created.isoformat() if self.created else None

        creator = self.creator
        displayname = self.displayname
        equipment = self.equipment
        id = self.id
        is_free = self.is_free
        modified: Union[Unset, None, str] = UNSET
        if not isinstance(self.modified, Unset):
            modified = self.modified.isoformat() if self.modified else None

        order = self.order
        parent_equipment = self.parent_equipment
        quantity = self.quantity
        skip = self.skip

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if add_as_new_line is not UNSET:
            field_dict["add_as_new_line"] = add_as_new_line
        if automatic is not UNSET:
            field_dict["automatic"] = automatic
        if created is not UNSET:
            field_dict["created"] = created
        if creator is not UNSET:
            field_dict["creator"] = creator
        if displayname is not UNSET:
            field_dict["displayname"] = displayname
        if equipment is not UNSET:
            field_dict["equipment"] = equipment
        if id is not UNSET:
            field_dict["id"] = id
        if is_free is not UNSET:
            field_dict["is_free"] = is_free
        if modified is not UNSET:
            field_dict["modified"] = modified
        if order is not UNSET:
            field_dict["order"] = order
        if parent_equipment is not UNSET:
            field_dict["parent_equipment"] = parent_equipment
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

        created = None
        _created = d.pop("created", UNSET)
        if _created is not None and not isinstance(_created, Unset):
            created = isoparse(_created)

        creator = d.pop("creator", UNSET)

        displayname = d.pop("displayname", UNSET)

        equipment = d.pop("equipment", UNSET)

        id = d.pop("id", UNSET)

        is_free = d.pop("is_free", UNSET)

        modified = None
        _modified = d.pop("modified", UNSET)
        if _modified is not None and not isinstance(_modified, Unset):
            modified = isoparse(_modified)

        order = d.pop("order", UNSET)

        parent_equipment = d.pop("parent_equipment", UNSET)

        quantity = d.pop("quantity", UNSET)

        skip = d.pop("skip", UNSET)

        accessory_itemget_response_schema_data = cls(
            add_as_new_line=add_as_new_line,
            automatic=automatic,
            created=created,
            creator=creator,
            displayname=displayname,
            equipment=equipment,
            id=id,
            is_free=is_free,
            modified=modified,
            order=order,
            parent_equipment=parent_equipment,
            quantity=quantity,
            skip=skip,
        )

        accessory_itemget_response_schema_data.additional_properties = d
        return accessory_itemget_response_schema_data

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

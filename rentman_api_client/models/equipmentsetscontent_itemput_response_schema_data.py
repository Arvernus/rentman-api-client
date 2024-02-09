import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.equipmentsetscontent_itemput_response_schema_data_is_fixed import (
    EquipmentsetscontentItemputResponseSchemaDataIsFixed,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="EquipmentsetscontentItemputResponseSchemaData")


@attr.s(auto_attribs=True)
class EquipmentsetscontentItemputResponseSchemaData:
    """All the data about the requested items"""

    id: Union[Unset, int] = UNSET
    created: Union[Unset, None, datetime.datetime] = UNSET
    modified: Union[Unset, None, datetime.datetime] = UNSET
    creator: Union[Unset, None, str] = UNSET
    displayname: Union[Unset, str] = UNSET
    quantity: Union[Unset, str] = UNSET
    parent_equipment: Union[Unset, str] = UNSET
    order: Union[Unset, str] = UNSET
    equipment: Union[Unset, str] = UNSET
    is_fixed: Union[Unset, EquipmentsetscontentItemputResponseSchemaDataIsFixed] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        created: Union[Unset, None, str] = UNSET
        if not isinstance(self.created, Unset):
            created = self.created.isoformat() if self.created else None

        modified: Union[Unset, None, str] = UNSET
        if not isinstance(self.modified, Unset):
            modified = self.modified.isoformat() if self.modified else None

        creator = self.creator
        displayname = self.displayname
        quantity = self.quantity
        parent_equipment = self.parent_equipment
        order = self.order
        equipment = self.equipment
        is_fixed: Union[Unset, str] = UNSET
        if not isinstance(self.is_fixed, Unset):
            is_fixed = self.is_fixed.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if created is not UNSET:
            field_dict["created"] = created
        if modified is not UNSET:
            field_dict["modified"] = modified
        if creator is not UNSET:
            field_dict["creator"] = creator
        if displayname is not UNSET:
            field_dict["displayname"] = displayname
        if quantity is not UNSET:
            field_dict["quantity"] = quantity
        if parent_equipment is not UNSET:
            field_dict["parent_equipment"] = parent_equipment
        if order is not UNSET:
            field_dict["order"] = order
        if equipment is not UNSET:
            field_dict["equipment"] = equipment
        if is_fixed is not UNSET:
            field_dict["is_fixed"] = is_fixed

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        created = None
        _created = d.pop("created", UNSET)
        if _created is not None and not isinstance(_created, Unset):
            created = isoparse(_created)

        modified = None
        _modified = d.pop("modified", UNSET)
        if _modified is not None and not isinstance(_modified, Unset):
            modified = isoparse(_modified)

        creator = d.pop("creator", UNSET)

        displayname = d.pop("displayname", UNSET)

        quantity = d.pop("quantity", UNSET)

        parent_equipment = d.pop("parent_equipment", UNSET)

        order = d.pop("order", UNSET)

        equipment = d.pop("equipment", UNSET)

        is_fixed: Union[Unset, EquipmentsetscontentItemputResponseSchemaDataIsFixed] = UNSET
        _is_fixed = d.pop("is_fixed", UNSET)
        if not isinstance(_is_fixed, Unset):
            is_fixed = EquipmentsetscontentItemputResponseSchemaDataIsFixed(_is_fixed)

        equipmentsetscontent_itemput_response_schema_data = cls(
            id=id,
            created=created,
            modified=modified,
            creator=creator,
            displayname=displayname,
            quantity=quantity,
            parent_equipment=parent_equipment,
            order=order,
            equipment=equipment,
            is_fixed=is_fixed,
        )

        equipmentsetscontent_itemput_response_schema_data.additional_properties = d
        return equipmentsetscontent_itemput_response_schema_data

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

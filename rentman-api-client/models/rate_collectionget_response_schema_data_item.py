import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.rate_collectionget_response_schema_data_item_subtype import RateCollectiongetResponseSchemaDataItemSubtype
from ..models.rate_collectionget_response_schema_data_item_type import RateCollectiongetResponseSchemaDataItemType
from ..types import UNSET, Unset

T = TypeVar("T", bound="RateCollectiongetResponseSchemaDataItem")


@attr.s(auto_attribs=True)
class RateCollectiongetResponseSchemaDataItem:
    """ """

    id: Union[Unset, int] = UNSET
    created: Union[Unset, None, datetime.datetime] = UNSET
    modified: Union[Unset, None, datetime.datetime] = UNSET
    creator: Union[Unset, None, str] = UNSET
    displayname: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    archived: Union[Unset, bool] = UNSET
    type: Union[Unset, RateCollectiongetResponseSchemaDataItemType] = UNSET
    subtype: Union[Unset, RateCollectiongetResponseSchemaDataItemSubtype] = UNSET
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
        name = self.name
        archived = self.archived
        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        subtype: Union[Unset, str] = UNSET
        if not isinstance(self.subtype, Unset):
            subtype = self.subtype.value

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
        if name is not UNSET:
            field_dict["name"] = name
        if archived is not UNSET:
            field_dict["archived"] = archived
        if type is not UNSET:
            field_dict["type"] = type
        if subtype is not UNSET:
            field_dict["subtype"] = subtype

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

        name = d.pop("name", UNSET)

        archived = d.pop("archived", UNSET)

        type: Union[Unset, RateCollectiongetResponseSchemaDataItemType] = UNSET
        _type = d.pop("type", UNSET)
        if not isinstance(_type, Unset):
            type = RateCollectiongetResponseSchemaDataItemType(_type)

        subtype: Union[Unset, RateCollectiongetResponseSchemaDataItemSubtype] = UNSET
        _subtype = d.pop("subtype", UNSET)
        if not isinstance(_subtype, Unset):
            subtype = RateCollectiongetResponseSchemaDataItemSubtype(_subtype)

        rate_collectionget_response_schema_data_item = cls(
            id=id,
            created=created,
            modified=modified,
            creator=creator,
            displayname=displayname,
            name=name,
            archived=archived,
            type=type,
            subtype=subtype,
        )

        rate_collectionget_response_schema_data_item.additional_properties = d
        return rate_collectionget_response_schema_data_item

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

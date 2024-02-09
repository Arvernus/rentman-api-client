import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="AppointmentCollectionpostResponseSchemaDataItem")


@attr.s(auto_attribs=True)
class AppointmentCollectionpostResponseSchemaDataItem:
    """ """

    color: Union[Unset, str] = UNSET
    created: Union[Unset, None, datetime.datetime] = UNSET
    creator: Union[Unset, None, str] = UNSET
    displayname: Union[Unset, str] = UNSET
    end: Union[Unset, datetime.datetime] = UNSET
    id: Union[Unset, int] = UNSET
    is_plannable: Union[Unset, bool] = UNSET
    is_public: Union[Unset, bool] = UNSET
    location: Union[Unset, str] = UNSET
    modified: Union[Unset, None, datetime.datetime] = UNSET
    name: Union[Unset, str] = UNSET
    remark: Union[Unset, str] = UNSET
    start: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        color = self.color
        created: Union[Unset, None, str] = UNSET
        if not isinstance(self.created, Unset):
            created = self.created.isoformat() if self.created else None

        creator = self.creator
        displayname = self.displayname
        end: Union[Unset, str] = UNSET
        if not isinstance(self.end, Unset):
            end = self.end.isoformat()

        id = self.id
        is_plannable = self.is_plannable
        is_public = self.is_public
        location = self.location
        modified: Union[Unset, None, str] = UNSET
        if not isinstance(self.modified, Unset):
            modified = self.modified.isoformat() if self.modified else None

        name = self.name
        remark = self.remark
        start: Union[Unset, str] = UNSET
        if not isinstance(self.start, Unset):
            start = self.start.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if color is not UNSET:
            field_dict["color"] = color
        if created is not UNSET:
            field_dict["created"] = created
        if creator is not UNSET:
            field_dict["creator"] = creator
        if displayname is not UNSET:
            field_dict["displayname"] = displayname
        if end is not UNSET:
            field_dict["end"] = end
        if id is not UNSET:
            field_dict["id"] = id
        if is_plannable is not UNSET:
            field_dict["is_plannable"] = is_plannable
        if is_public is not UNSET:
            field_dict["is_public"] = is_public
        if location is not UNSET:
            field_dict["location"] = location
        if modified is not UNSET:
            field_dict["modified"] = modified
        if name is not UNSET:
            field_dict["name"] = name
        if remark is not UNSET:
            field_dict["remark"] = remark
        if start is not UNSET:
            field_dict["start"] = start

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        color = d.pop("color", UNSET)

        created = None
        _created = d.pop("created", UNSET)
        if _created is not None and not isinstance(_created, Unset):
            created = isoparse(_created)

        creator = d.pop("creator", UNSET)

        displayname = d.pop("displayname", UNSET)

        end: Union[Unset, datetime.datetime] = UNSET
        _end = d.pop("end", UNSET)
        if not isinstance(_end, Unset):
            end = isoparse(_end)

        id = d.pop("id", UNSET)

        is_plannable = d.pop("is_plannable", UNSET)

        is_public = d.pop("is_public", UNSET)

        location = d.pop("location", UNSET)

        modified = None
        _modified = d.pop("modified", UNSET)
        if _modified is not None and not isinstance(_modified, Unset):
            modified = isoparse(_modified)

        name = d.pop("name", UNSET)

        remark = d.pop("remark", UNSET)

        start: Union[Unset, datetime.datetime] = UNSET
        _start = d.pop("start", UNSET)
        if not isinstance(_start, Unset):
            start = isoparse(_start)

        appointment_collectionpost_response_schema_data_item = cls(
            color=color,
            created=created,
            creator=creator,
            displayname=displayname,
            end=end,
            id=id,
            is_plannable=is_plannable,
            is_public=is_public,
            location=location,
            modified=modified,
            name=name,
            remark=remark,
            start=start,
        )

        appointment_collectionpost_response_schema_data_item.additional_properties = d
        return appointment_collectionpost_response_schema_data_item

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

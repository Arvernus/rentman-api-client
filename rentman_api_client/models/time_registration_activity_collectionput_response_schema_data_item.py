import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="TimeRegistrationActivityCollectionputResponseSchemaDataItem")


@attr.s(auto_attribs=True)
class TimeRegistrationActivityCollectionputResponseSchemaDataItem:
    """ """

    created: Union[Unset, None, datetime.datetime] = UNSET
    creator: Union[Unset, None, str] = UNSET
    description: Union[Unset, str] = UNSET
    displayname: Union[Unset, str] = UNSET
    duration: Union[Unset, None, float] = UNSET
    id: Union[Unset, int] = UNSET
    modified: Union[Unset, None, datetime.datetime] = UNSET
    project_function: Union[Unset, None, str] = UNSET
    time_registration: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        created: Union[Unset, None, str] = UNSET
        if not isinstance(self.created, Unset):
            created = self.created.isoformat() if self.created else None

        creator = self.creator
        description = self.description
        displayname = self.displayname
        duration = self.duration
        id = self.id
        modified: Union[Unset, None, str] = UNSET
        if not isinstance(self.modified, Unset):
            modified = self.modified.isoformat() if self.modified else None

        project_function = self.project_function
        time_registration = self.time_registration

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if created is not UNSET:
            field_dict["created"] = created
        if creator is not UNSET:
            field_dict["creator"] = creator
        if description is not UNSET:
            field_dict["description"] = description
        if displayname is not UNSET:
            field_dict["displayname"] = displayname
        if duration is not UNSET:
            field_dict["duration"] = duration
        if id is not UNSET:
            field_dict["id"] = id
        if modified is not UNSET:
            field_dict["modified"] = modified
        if project_function is not UNSET:
            field_dict["project_function"] = project_function
        if time_registration is not UNSET:
            field_dict["time_registration"] = time_registration

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        created = None
        _created = d.pop("created", UNSET)
        if _created is not None and not isinstance(_created, Unset):
            created = isoparse(_created)

        creator = d.pop("creator", UNSET)

        description = d.pop("description", UNSET)

        displayname = d.pop("displayname", UNSET)

        duration = d.pop("duration", UNSET)

        id = d.pop("id", UNSET)

        modified = None
        _modified = d.pop("modified", UNSET)
        if _modified is not None and not isinstance(_modified, Unset):
            modified = isoparse(_modified)

        project_function = d.pop("project_function", UNSET)

        time_registration = d.pop("time_registration", UNSET)

        time_registration_activity_collectionput_response_schema_data_item = cls(
            created=created,
            creator=creator,
            description=description,
            displayname=displayname,
            duration=duration,
            id=id,
            modified=modified,
            project_function=project_function,
            time_registration=time_registration,
        )

        time_registration_activity_collectionput_response_schema_data_item.additional_properties = d
        return time_registration_activity_collectionput_response_schema_data_item

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

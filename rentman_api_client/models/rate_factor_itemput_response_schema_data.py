import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="RateFactorItemputResponseSchemaData")


@attr.s(auto_attribs=True)
class RateFactorItemputResponseSchemaData:
    """All the data about the requested items"""

    created: Union[Unset, None, datetime.datetime] = UNSET
    creator: Union[Unset, None, str] = UNSET
    displayname: Union[Unset, str] = UNSET
    fixed: Union[Unset, float] = UNSET
    from_: Union[Unset, None, float] = UNSET
    id: Union[Unset, int] = UNSET
    modified: Union[Unset, None, datetime.datetime] = UNSET
    rate_id: Union[Unset, str] = UNSET
    to: Union[Unset, None, float] = UNSET
    variable: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        created: Union[Unset, None, str] = UNSET
        if not isinstance(self.created, Unset):
            created = self.created.isoformat() if self.created else None

        creator = self.creator
        displayname = self.displayname
        fixed = self.fixed
        from_ = self.from_
        id = self.id
        modified: Union[Unset, None, str] = UNSET
        if not isinstance(self.modified, Unset):
            modified = self.modified.isoformat() if self.modified else None

        rate_id = self.rate_id
        to = self.to
        variable = self.variable

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if created is not UNSET:
            field_dict["created"] = created
        if creator is not UNSET:
            field_dict["creator"] = creator
        if displayname is not UNSET:
            field_dict["displayname"] = displayname
        if fixed is not UNSET:
            field_dict["fixed"] = fixed
        if from_ is not UNSET:
            field_dict["from"] = from_
        if id is not UNSET:
            field_dict["id"] = id
        if modified is not UNSET:
            field_dict["modified"] = modified
        if rate_id is not UNSET:
            field_dict["rate_id"] = rate_id
        if to is not UNSET:
            field_dict["to"] = to
        if variable is not UNSET:
            field_dict["variable"] = variable

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        created = None
        _created = d.pop("created", UNSET)
        if _created is not None and not isinstance(_created, Unset):
            created = isoparse(_created)

        creator = d.pop("creator", UNSET)

        displayname = d.pop("displayname", UNSET)

        fixed = d.pop("fixed", UNSET)

        from_ = d.pop("from", UNSET)

        id = d.pop("id", UNSET)

        modified = None
        _modified = d.pop("modified", UNSET)
        if _modified is not None and not isinstance(_modified, Unset):
            modified = isoparse(_modified)

        rate_id = d.pop("rate_id", UNSET)

        to = d.pop("to", UNSET)

        variable = d.pop("variable", UNSET)

        rate_factor_itemput_response_schema_data = cls(
            created=created,
            creator=creator,
            displayname=displayname,
            fixed=fixed,
            from_=from_,
            id=id,
            modified=modified,
            rate_id=rate_id,
            to=to,
            variable=variable,
        )

        rate_factor_itemput_response_schema_data.additional_properties = d
        return rate_factor_itemput_response_schema_data

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

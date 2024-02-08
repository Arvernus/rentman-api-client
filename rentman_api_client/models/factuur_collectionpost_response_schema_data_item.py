import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="FactuurCollectionpostResponseSchemaDataItem")


@attr.s(auto_attribs=True)
class FactuurCollectionpostResponseSchemaDataItem:
    """ """

    id: Union[Unset, int] = UNSET
    created: Union[Unset, None, datetime.datetime] = UNSET
    modified: Union[Unset, None, datetime.datetime] = UNSET
    creator: Union[Unset, None, str] = UNSET
    displayname: Union[Unset, str] = UNSET
    customer: Union[Unset, None, str] = UNSET
    account_manager: Union[Unset, None, str] = UNSET
    contact: Union[Unset, None, str] = UNSET
    expiration: Union[Unset, None, str] = UNSET
    date: Union[Unset, None, str] = UNSET
    number: Union[Unset, str] = UNSET
    procent: Union[Unset, float] = UNSET
    from_project: Union[Unset, bool] = UNSET
    subject: Union[Unset, str] = UNSET
    project: Union[Unset, None, str] = UNSET
    filename: Union[Unset, str] = UNSET
    tags: Union[Unset, str] = UNSET
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
        customer = self.customer
        account_manager = self.account_manager
        contact = self.contact
        expiration = self.expiration
        date = self.date
        number = self.number
        procent = self.procent
        from_project = self.from_project
        subject = self.subject
        project = self.project
        filename = self.filename
        tags = self.tags

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
        if customer is not UNSET:
            field_dict["customer"] = customer
        if account_manager is not UNSET:
            field_dict["account_manager"] = account_manager
        if contact is not UNSET:
            field_dict["contact"] = contact
        if expiration is not UNSET:
            field_dict["expiration"] = expiration
        if date is not UNSET:
            field_dict["date"] = date
        if number is not UNSET:
            field_dict["number"] = number
        if procent is not UNSET:
            field_dict["procent"] = procent
        if from_project is not UNSET:
            field_dict["from_project"] = from_project
        if subject is not UNSET:
            field_dict["subject"] = subject
        if project is not UNSET:
            field_dict["project"] = project
        if filename is not UNSET:
            field_dict["filename"] = filename
        if tags is not UNSET:
            field_dict["tags"] = tags

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

        customer = d.pop("customer", UNSET)

        account_manager = d.pop("account_manager", UNSET)

        contact = d.pop("contact", UNSET)

        expiration = d.pop("expiration", UNSET)

        date = d.pop("date", UNSET)

        number = d.pop("number", UNSET)

        procent = d.pop("procent", UNSET)

        from_project = d.pop("from_project", UNSET)

        subject = d.pop("subject", UNSET)

        project = d.pop("project", UNSET)

        filename = d.pop("filename", UNSET)

        tags = d.pop("tags", UNSET)

        factuur_collectionpost_response_schema_data_item = cls(
            id=id,
            created=created,
            modified=modified,
            creator=creator,
            displayname=displayname,
            customer=customer,
            account_manager=account_manager,
            contact=contact,
            expiration=expiration,
            date=date,
            number=number,
            procent=procent,
            from_project=from_project,
            subject=subject,
            project=project,
            filename=filename,
            tags=tags,
        )

        factuur_collectionpost_response_schema_data_item.additional_properties = d
        return factuur_collectionpost_response_schema_data_item

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

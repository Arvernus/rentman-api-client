import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="InvoiceItemputResponseSchemaData")


@attr.s(auto_attribs=True)
class InvoiceItemputResponseSchemaData:
    """All the data about the requested items"""

    account_manager: Union[Unset, None, str] = UNSET
    contact: Union[Unset, None, str] = UNSET
    created: Union[Unset, None, datetime.datetime] = UNSET
    creator: Union[Unset, None, str] = UNSET
    customer: Union[Unset, None, str] = UNSET
    date: Union[Unset, None, str] = UNSET
    displayname: Union[Unset, str] = UNSET
    expiration: Union[Unset, None, str] = UNSET
    filename: Union[Unset, str] = UNSET
    from_project: Union[Unset, bool] = UNSET
    id: Union[Unset, int] = UNSET
    modified: Union[Unset, None, datetime.datetime] = UNSET
    number: Union[Unset, str] = UNSET
    procent: Union[Unset, float] = UNSET
    project: Union[Unset, None, str] = UNSET
    project_crew_price: Union[Unset, float] = UNSET
    project_insurance_price: Union[Unset, float] = UNSET
    project_other_price: Union[Unset, float] = UNSET
    project_rental_price: Union[Unset, float] = UNSET
    project_sale_price: Union[Unset, float] = UNSET
    project_total_price: Union[Unset, float] = UNSET
    project_transport_price: Union[Unset, float] = UNSET
    subject: Union[Unset, str] = UNSET
    tags: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        account_manager = self.account_manager
        contact = self.contact
        created: Union[Unset, None, str] = UNSET
        if not isinstance(self.created, Unset):
            created = self.created.isoformat() if self.created else None

        creator = self.creator
        customer = self.customer
        date = self.date
        displayname = self.displayname
        expiration = self.expiration
        filename = self.filename
        from_project = self.from_project
        id = self.id
        modified: Union[Unset, None, str] = UNSET
        if not isinstance(self.modified, Unset):
            modified = self.modified.isoformat() if self.modified else None

        number = self.number
        procent = self.procent
        project = self.project
        project_crew_price = self.project_crew_price
        project_insurance_price = self.project_insurance_price
        project_other_price = self.project_other_price
        project_rental_price = self.project_rental_price
        project_sale_price = self.project_sale_price
        project_total_price = self.project_total_price
        project_transport_price = self.project_transport_price
        subject = self.subject
        tags = self.tags

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if account_manager is not UNSET:
            field_dict["account_manager"] = account_manager
        if contact is not UNSET:
            field_dict["contact"] = contact
        if created is not UNSET:
            field_dict["created"] = created
        if creator is not UNSET:
            field_dict["creator"] = creator
        if customer is not UNSET:
            field_dict["customer"] = customer
        if date is not UNSET:
            field_dict["date"] = date
        if displayname is not UNSET:
            field_dict["displayname"] = displayname
        if expiration is not UNSET:
            field_dict["expiration"] = expiration
        if filename is not UNSET:
            field_dict["filename"] = filename
        if from_project is not UNSET:
            field_dict["from_project"] = from_project
        if id is not UNSET:
            field_dict["id"] = id
        if modified is not UNSET:
            field_dict["modified"] = modified
        if number is not UNSET:
            field_dict["number"] = number
        if procent is not UNSET:
            field_dict["procent"] = procent
        if project is not UNSET:
            field_dict["project"] = project
        if project_crew_price is not UNSET:
            field_dict["project_crew_price"] = project_crew_price
        if project_insurance_price is not UNSET:
            field_dict["project_insurance_price"] = project_insurance_price
        if project_other_price is not UNSET:
            field_dict["project_other_price"] = project_other_price
        if project_rental_price is not UNSET:
            field_dict["project_rental_price"] = project_rental_price
        if project_sale_price is not UNSET:
            field_dict["project_sale_price"] = project_sale_price
        if project_total_price is not UNSET:
            field_dict["project_total_price"] = project_total_price
        if project_transport_price is not UNSET:
            field_dict["project_transport_price"] = project_transport_price
        if subject is not UNSET:
            field_dict["subject"] = subject
        if tags is not UNSET:
            field_dict["tags"] = tags

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        account_manager = d.pop("account_manager", UNSET)

        contact = d.pop("contact", UNSET)

        created = None
        _created = d.pop("created", UNSET)
        if _created is not None and not isinstance(_created, Unset):
            created = isoparse(_created)

        creator = d.pop("creator", UNSET)

        customer = d.pop("customer", UNSET)

        date = d.pop("date", UNSET)

        displayname = d.pop("displayname", UNSET)

        expiration = d.pop("expiration", UNSET)

        filename = d.pop("filename", UNSET)

        from_project = d.pop("from_project", UNSET)

        id = d.pop("id", UNSET)

        modified = None
        _modified = d.pop("modified", UNSET)
        if _modified is not None and not isinstance(_modified, Unset):
            modified = isoparse(_modified)

        number = d.pop("number", UNSET)

        procent = d.pop("procent", UNSET)

        project = d.pop("project", UNSET)

        project_crew_price = d.pop("project_crew_price", UNSET)

        project_insurance_price = d.pop("project_insurance_price", UNSET)

        project_other_price = d.pop("project_other_price", UNSET)

        project_rental_price = d.pop("project_rental_price", UNSET)

        project_sale_price = d.pop("project_sale_price", UNSET)

        project_total_price = d.pop("project_total_price", UNSET)

        project_transport_price = d.pop("project_transport_price", UNSET)

        subject = d.pop("subject", UNSET)

        tags = d.pop("tags", UNSET)

        invoice_itemput_response_schema_data = cls(
            account_manager=account_manager,
            contact=contact,
            created=created,
            creator=creator,
            customer=customer,
            date=date,
            displayname=displayname,
            expiration=expiration,
            filename=filename,
            from_project=from_project,
            id=id,
            modified=modified,
            number=number,
            procent=procent,
            project=project,
            project_crew_price=project_crew_price,
            project_insurance_price=project_insurance_price,
            project_other_price=project_other_price,
            project_rental_price=project_rental_price,
            project_sale_price=project_sale_price,
            project_total_price=project_total_price,
            project_transport_price=project_transport_price,
            subject=subject,
            tags=tags,
        )

        invoice_itemput_response_schema_data.additional_properties = d
        return invoice_itemput_response_schema_data

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

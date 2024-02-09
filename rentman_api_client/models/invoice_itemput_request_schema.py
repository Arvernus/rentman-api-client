from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="InvoiceItemputRequestSchema")


@attr.s(auto_attribs=True)
class InvoiceItemputRequestSchema:
    """ """

    account_manager: Union[Unset, None, str] = UNSET
    contact: Union[Unset, None, str] = UNSET
    customer: Union[Unset, None, str] = UNSET
    date: Union[Unset, None, str] = UNSET
    expiration: Union[Unset, None, str] = UNSET
    filename: Union[Unset, str] = UNSET
    from_project: Union[Unset, bool] = UNSET
    number: Union[Unset, str] = UNSET
    procent: Union[Unset, float] = UNSET
    project: Union[Unset, None, str] = UNSET
    subject: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        account_manager = self.account_manager
        contact = self.contact
        customer = self.customer
        date = self.date
        expiration = self.expiration
        filename = self.filename
        from_project = self.from_project
        number = self.number
        procent = self.procent
        project = self.project
        subject = self.subject

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if account_manager is not UNSET:
            field_dict["account_manager"] = account_manager
        if contact is not UNSET:
            field_dict["contact"] = contact
        if customer is not UNSET:
            field_dict["customer"] = customer
        if date is not UNSET:
            field_dict["date"] = date
        if expiration is not UNSET:
            field_dict["expiration"] = expiration
        if filename is not UNSET:
            field_dict["filename"] = filename
        if from_project is not UNSET:
            field_dict["from_project"] = from_project
        if number is not UNSET:
            field_dict["number"] = number
        if procent is not UNSET:
            field_dict["procent"] = procent
        if project is not UNSET:
            field_dict["project"] = project
        if subject is not UNSET:
            field_dict["subject"] = subject

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        account_manager = d.pop("account_manager", UNSET)

        contact = d.pop("contact", UNSET)

        customer = d.pop("customer", UNSET)

        date = d.pop("date", UNSET)

        expiration = d.pop("expiration", UNSET)

        filename = d.pop("filename", UNSET)

        from_project = d.pop("from_project", UNSET)

        number = d.pop("number", UNSET)

        procent = d.pop("procent", UNSET)

        project = d.pop("project", UNSET)

        subject = d.pop("subject", UNSET)

        invoice_itemput_request_schema = cls(
            account_manager=account_manager,
            contact=contact,
            customer=customer,
            date=date,
            expiration=expiration,
            filename=filename,
            from_project=from_project,
            number=number,
            procent=procent,
            project=project,
            subject=subject,
        )

        invoice_itemput_request_schema.additional_properties = d
        return invoice_itemput_request_schema

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

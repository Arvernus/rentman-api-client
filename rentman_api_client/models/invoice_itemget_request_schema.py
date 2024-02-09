from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="InvoiceItemgetRequestSchema")


@attr.s(auto_attribs=True)
class InvoiceItemgetRequestSchema:
    """ """

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
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
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

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
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

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
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

        invoice_itemget_request_schema = cls(
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
        )

        invoice_itemget_request_schema.additional_properties = d
        return invoice_itemget_request_schema

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

import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.payment_itemput_request_schema_payment_import_source import PaymentItemputRequestSchemaPaymentImportSource
from ..types import UNSET, Unset

T = TypeVar("T", bound="PaymentItemputRequestSchema")


@attr.s(auto_attribs=True)
class PaymentItemputRequestSchema:
    """ """

    moment: datetime.datetime
    amount: Union[Unset, float] = UNSET
    description: Union[Unset, str] = UNSET
    payment_import_source: Union[Unset, PaymentItemputRequestSchemaPaymentImportSource] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        moment = self.moment.isoformat()

        amount = self.amount
        description = self.description
        payment_import_source: Union[Unset, str] = UNSET
        if not isinstance(self.payment_import_source, Unset):
            payment_import_source = self.payment_import_source.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "moment": moment,
            }
        )
        if amount is not UNSET:
            field_dict["amount"] = amount
        if description is not UNSET:
            field_dict["description"] = description
        if payment_import_source is not UNSET:
            field_dict["payment_import_source"] = payment_import_source

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        moment = isoparse(d.pop("moment"))

        amount = d.pop("amount", UNSET)

        description = d.pop("description", UNSET)

        payment_import_source: Union[Unset, PaymentItemputRequestSchemaPaymentImportSource] = UNSET
        _payment_import_source = d.pop("payment_import_source", UNSET)
        if not isinstance(_payment_import_source, Unset):
            payment_import_source = PaymentItemputRequestSchemaPaymentImportSource(_payment_import_source)

        payment_itemput_request_schema = cls(
            moment=moment,
            amount=amount,
            description=description,
            payment_import_source=payment_import_source,
        )

        payment_itemput_request_schema.additional_properties = d
        return payment_itemput_request_schema

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

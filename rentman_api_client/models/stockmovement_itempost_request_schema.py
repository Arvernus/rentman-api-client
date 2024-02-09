import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="StockmovementItempostRequestSchema")


@attr.s(auto_attribs=True)
class StockmovementItempostRequestSchema:
    """ """

    amount: Union[Unset, int] = UNSET
    projectequipment: Union[Unset, None, str] = UNSET
    description: Union[Unset, str] = UNSET
    details: Union[Unset, str] = UNSET
    date: Union[Unset, None, datetime.datetime] = UNSET
    stock_location: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        amount = self.amount
        projectequipment = self.projectequipment
        description = self.description
        details = self.details
        date: Union[Unset, None, str] = UNSET
        if not isinstance(self.date, Unset):
            date = self.date.isoformat() if self.date else None

        stock_location = self.stock_location

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if amount is not UNSET:
            field_dict["amount"] = amount
        if projectequipment is not UNSET:
            field_dict["projectequipment"] = projectequipment
        if description is not UNSET:
            field_dict["description"] = description
        if details is not UNSET:
            field_dict["details"] = details
        if date is not UNSET:
            field_dict["date"] = date
        if stock_location is not UNSET:
            field_dict["stock_location"] = stock_location

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        amount = d.pop("amount", UNSET)

        projectequipment = d.pop("projectequipment", UNSET)

        description = d.pop("description", UNSET)

        details = d.pop("details", UNSET)

        date = None
        _date = d.pop("date", UNSET)
        if _date is not None and not isinstance(_date, Unset):
            date = isoparse(_date)

        stock_location = d.pop("stock_location", UNSET)

        stockmovement_itempost_request_schema = cls(
            amount=amount,
            projectequipment=projectequipment,
            description=description,
            details=details,
            date=date,
            stock_location=stock_location,
        )

        stockmovement_itempost_request_schema.additional_properties = d
        return stockmovement_itempost_request_schema

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
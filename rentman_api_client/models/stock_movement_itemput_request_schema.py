import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="StockMovementItemputRequestSchema")


@attr.s(auto_attribs=True)
class StockMovementItemputRequestSchema:
    """ """

    amount: Union[Unset, int] = UNSET
    date: Union[Unset, None, datetime.datetime] = UNSET
    description: Union[Unset, str] = UNSET
    details: Union[Unset, str] = UNSET
    projectequipment: Union[Unset, None, str] = UNSET
    stock_location: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        amount = self.amount
        date: Union[Unset, None, str] = UNSET
        if not isinstance(self.date, Unset):
            date = self.date.isoformat() if self.date else None

        description = self.description
        details = self.details
        projectequipment = self.projectequipment
        stock_location = self.stock_location

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if amount is not UNSET:
            field_dict["amount"] = amount
        if date is not UNSET:
            field_dict["date"] = date
        if description is not UNSET:
            field_dict["description"] = description
        if details is not UNSET:
            field_dict["details"] = details
        if projectequipment is not UNSET:
            field_dict["projectequipment"] = projectequipment
        if stock_location is not UNSET:
            field_dict["stock_location"] = stock_location

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        amount = d.pop("amount", UNSET)

        date = None
        _date = d.pop("date", UNSET)
        if _date is not None and not isinstance(_date, Unset):
            date = isoparse(_date)

        description = d.pop("description", UNSET)

        details = d.pop("details", UNSET)

        projectequipment = d.pop("projectequipment", UNSET)

        stock_location = d.pop("stock_location", UNSET)

        stock_movement_itemput_request_schema = cls(
            amount=amount,
            date=date,
            description=description,
            details=details,
            projectequipment=projectequipment,
            stock_location=stock_location,
        )

        stock_movement_itemput_request_schema.additional_properties = d
        return stock_movement_itemput_request_schema

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

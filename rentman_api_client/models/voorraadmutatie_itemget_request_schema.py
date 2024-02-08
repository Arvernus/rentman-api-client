import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.voorraadmutatie_itemget_request_schema_type import VoorraadmutatieItemgetRequestSchemaType
from ..types import UNSET, Unset

T = TypeVar("T", bound="VoorraadmutatieItemgetRequestSchema")


@attr.s(auto_attribs=True)
class VoorraadmutatieItemgetRequestSchema:
    """ """

    amount: Union[Unset, int] = UNSET
    projectequipment: Union[Unset, None, str] = UNSET
    description: Union[Unset, str] = UNSET
    details: Union[Unset, str] = UNSET
    date: Union[Unset, None, datetime.datetime] = UNSET
    type: Union[Unset, VoorraadmutatieItemgetRequestSchemaType] = UNSET
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

        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

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
        if type is not UNSET:
            field_dict["type"] = type
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

        type: Union[Unset, VoorraadmutatieItemgetRequestSchemaType] = UNSET
        _type = d.pop("type", UNSET)
        if not isinstance(_type, Unset):
            type = VoorraadmutatieItemgetRequestSchemaType(_type)

        stock_location = d.pop("stock_location", UNSET)

        voorraadmutatie_itemget_request_schema = cls(
            amount=amount,
            projectequipment=projectequipment,
            description=description,
            details=details,
            date=date,
            type=type,
            stock_location=stock_location,
        )

        voorraadmutatie_itemget_request_schema.additional_properties = d
        return voorraadmutatie_itemget_request_schema

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

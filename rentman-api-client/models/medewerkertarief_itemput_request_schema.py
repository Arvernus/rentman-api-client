from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="MedewerkertariefItemputRequestSchema")


@attr.s(auto_attribs=True)
class MedewerkertariefItemputRequestSchema:
    """ """

    naam: Union[Unset, str] = UNSET
    cost_rate: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        naam = self.naam
        cost_rate = self.cost_rate

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if naam is not UNSET:
            field_dict["naam"] = naam
        if cost_rate is not UNSET:
            field_dict["cost_rate"] = cost_rate

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        naam = d.pop("naam", UNSET)

        cost_rate = d.pop("cost_rate", UNSET)

        medewerkertarief_itemput_request_schema = cls(
            naam=naam,
            cost_rate=cost_rate,
        )

        medewerkertarief_itemput_request_schema.additional_properties = d
        return medewerkertarief_itemput_request_schema

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

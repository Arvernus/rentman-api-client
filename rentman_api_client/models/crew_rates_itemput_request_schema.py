from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="CrewRatesItemputRequestSchema")


@attr.s(auto_attribs=True)
class CrewRatesItemputRequestSchema:
    """ """

    cost_rate: Union[Unset, None, str] = UNSET
    naam: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        cost_rate = self.cost_rate
        naam = self.naam

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cost_rate is not UNSET:
            field_dict["cost_rate"] = cost_rate
        if naam is not UNSET:
            field_dict["naam"] = naam

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        cost_rate = d.pop("cost_rate", UNSET)

        naam = d.pop("naam", UNSET)

        crew_rates_itemput_request_schema = cls(
            cost_rate=cost_rate,
            naam=naam,
        )

        crew_rates_itemput_request_schema.additional_properties = d
        return crew_rates_itemput_request_schema

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

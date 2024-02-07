from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="RateFactorItempostRequestSchema")


@attr.s(auto_attribs=True)
class RateFactorItempostRequestSchema:
    """ """

    from_: Union[Unset, None, float] = UNSET
    to: Union[Unset, None, float] = UNSET
    variable: Union[Unset, float] = UNSET
    fixed: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from_ = self.from_
        to = self.to
        variable = self.variable
        fixed = self.fixed

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if from_ is not UNSET:
            field_dict["from"] = from_
        if to is not UNSET:
            field_dict["to"] = to
        if variable is not UNSET:
            field_dict["variable"] = variable
        if fixed is not UNSET:
            field_dict["fixed"] = fixed

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        from_ = d.pop("from", UNSET)

        to = d.pop("to", UNSET)

        variable = d.pop("variable", UNSET)

        fixed = d.pop("fixed", UNSET)

        rate_factor_itempost_request_schema = cls(
            from_=from_,
            to=to,
            variable=variable,
            fixed=fixed,
        )

        rate_factor_itempost_request_schema.additional_properties = d
        return rate_factor_itempost_request_schema

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
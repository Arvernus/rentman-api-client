from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.rate_factor_itempost_response_schema_data import RateFactorItempostResponseSchemaData
from ..types import UNSET, Unset

T = TypeVar("T", bound="RateFactorItempostResponseSchema")


@attr.s(auto_attribs=True)
class RateFactorItempostResponseSchema:
    """ """

    data: Union[Unset, RateFactorItempostResponseSchemaData] = UNSET
    item_count: Union[Unset, float] = UNSET
    limit: Union[Unset, float] = UNSET
    offset: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        data: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.data, Unset):
            data = self.data.to_dict()

        item_count = self.item_count
        limit = self.limit
        offset = self.offset

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if data is not UNSET:
            field_dict["data"] = data
        if item_count is not UNSET:
            field_dict["itemCount"] = item_count
        if limit is not UNSET:
            field_dict["limit"] = limit
        if offset is not UNSET:
            field_dict["offset"] = offset

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        data: Union[Unset, RateFactorItempostResponseSchemaData] = UNSET
        _data = d.pop("data", UNSET)
        if not isinstance(_data, Unset):
            data = RateFactorItempostResponseSchemaData.from_dict(_data)

        item_count = d.pop("itemCount", UNSET)

        limit = d.pop("limit", UNSET)

        offset = d.pop("offset", UNSET)

        rate_factor_itempost_response_schema = cls(
            data=data,
            item_count=item_count,
            limit=limit,
            offset=offset,
        )

        rate_factor_itempost_response_schema.additional_properties = d
        return rate_factor_itempost_response_schema

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

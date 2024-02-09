from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.equipment_collection_get_filter_status import EquipmentCollectionGetFilterStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="EquipmentCollectionGetFilter")


@attr.s(auto_attribs=True)
class EquipmentCollectionGetFilter:
    """ """

    status: Union[Unset, EquipmentCollectionGetFilterStatus] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        status: Union[Unset, EquipmentCollectionGetFilterStatus] = UNSET
        _status = d.pop("status", UNSET)
        if not isinstance(_status, Unset):
            status = EquipmentCollectionGetFilterStatus(_status)

        equipment_collection_get_filter = cls(
            status=status,
        )

        equipment_collection_get_filter.additional_properties = d
        return equipment_collection_get_filter

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

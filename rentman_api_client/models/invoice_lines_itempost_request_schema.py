from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="InvoiceLinesItempostRequestSchema")


@attr.s(auto_attribs=True)
class InvoiceLinesItempostRequestSchema:
    """ """

    base: Union[Unset, float] = UNSET
    ledger: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        base = self.base
        ledger = self.ledger

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if base is not UNSET:
            field_dict["base"] = base
        if ledger is not UNSET:
            field_dict["ledger"] = ledger

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        base = d.pop("base", UNSET)

        ledger = d.pop("ledger", UNSET)

        invoice_lines_itempost_request_schema = cls(
            base=base,
            ledger=ledger,
        )

        invoice_lines_itempost_request_schema.additional_properties = d
        return invoice_lines_itempost_request_schema

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

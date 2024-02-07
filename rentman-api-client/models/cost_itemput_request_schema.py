from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.cost_itemput_request_schema_custom import CostItemputRequestSchemaCustom
from ..types import UNSET, Unset

T = TypeVar("T", bound="CostItemputRequestSchema")


@attr.s(auto_attribs=True)
class CostItemputRequestSchema:
    """ """

    subproject: str
    name: Union[Unset, str] = UNSET
    remark: Union[Unset, str] = UNSET
    is_template: Union[Unset, bool] = UNSET
    taxclass: Union[Unset, None, str] = UNSET
    ledger: Union[Unset, None, str] = UNSET
    verkoopprijs: Union[Unset, float] = UNSET
    inkoopprijs: Union[Unset, float] = UNSET
    custom: Union[Unset, CostItemputRequestSchemaCustom] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        subproject = self.subproject
        name = self.name
        remark = self.remark
        is_template = self.is_template
        taxclass = self.taxclass
        ledger = self.ledger
        verkoopprijs = self.verkoopprijs
        inkoopprijs = self.inkoopprijs
        custom: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.custom, Unset):
            custom = self.custom.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "subproject": subproject,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if remark is not UNSET:
            field_dict["remark"] = remark
        if is_template is not UNSET:
            field_dict["is_template"] = is_template
        if taxclass is not UNSET:
            field_dict["taxclass"] = taxclass
        if ledger is not UNSET:
            field_dict["ledger"] = ledger
        if verkoopprijs is not UNSET:
            field_dict["verkoopprijs"] = verkoopprijs
        if inkoopprijs is not UNSET:
            field_dict["inkoopprijs"] = inkoopprijs
        if custom is not UNSET:
            field_dict["custom"] = custom

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        subproject = d.pop("subproject")

        name = d.pop("name", UNSET)

        remark = d.pop("remark", UNSET)

        is_template = d.pop("is_template", UNSET)

        taxclass = d.pop("taxclass", UNSET)

        ledger = d.pop("ledger", UNSET)

        verkoopprijs = d.pop("verkoopprijs", UNSET)

        inkoopprijs = d.pop("inkoopprijs", UNSET)

        custom: Union[Unset, CostItemputRequestSchemaCustom] = UNSET
        _custom = d.pop("custom", UNSET)
        if not isinstance(_custom, Unset):
            custom = CostItemputRequestSchemaCustom.from_dict(_custom)

        cost_itemput_request_schema = cls(
            subproject=subproject,
            name=name,
            remark=remark,
            is_template=is_template,
            taxclass=taxclass,
            ledger=ledger,
            verkoopprijs=verkoopprijs,
            inkoopprijs=inkoopprijs,
            custom=custom,
        )

        cost_itemput_request_schema.additional_properties = d
        return cost_itemput_request_schema

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

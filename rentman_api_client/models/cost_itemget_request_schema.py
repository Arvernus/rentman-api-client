from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.cost_itemget_request_schema_custom import CostItemgetRequestSchemaCustom
from ..types import UNSET, Unset

T = TypeVar("T", bound="CostItemgetRequestSchema")


@attr.s(auto_attribs=True)
class CostItemgetRequestSchema:
    """ """

    subproject: str
    custom: Union[Unset, CostItemgetRequestSchemaCustom] = UNSET
    inkoopprijs: Union[Unset, float] = UNSET
    is_template: Union[Unset, bool] = UNSET
    ledger: Union[Unset, None, str] = UNSET
    name: Union[Unset, str] = UNSET
    remark: Union[Unset, str] = UNSET
    taxclass: Union[Unset, None, str] = UNSET
    verkoopprijs: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        subproject = self.subproject
        custom: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.custom, Unset):
            custom = self.custom.to_dict()

        inkoopprijs = self.inkoopprijs
        is_template = self.is_template
        ledger = self.ledger
        name = self.name
        remark = self.remark
        taxclass = self.taxclass
        verkoopprijs = self.verkoopprijs

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "subproject": subproject,
            }
        )
        if custom is not UNSET:
            field_dict["custom"] = custom
        if inkoopprijs is not UNSET:
            field_dict["inkoopprijs"] = inkoopprijs
        if is_template is not UNSET:
            field_dict["is_template"] = is_template
        if ledger is not UNSET:
            field_dict["ledger"] = ledger
        if name is not UNSET:
            field_dict["name"] = name
        if remark is not UNSET:
            field_dict["remark"] = remark
        if taxclass is not UNSET:
            field_dict["taxclass"] = taxclass
        if verkoopprijs is not UNSET:
            field_dict["verkoopprijs"] = verkoopprijs

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        subproject = d.pop("subproject")

        custom: Union[Unset, CostItemgetRequestSchemaCustom] = UNSET
        _custom = d.pop("custom", UNSET)
        if not isinstance(_custom, Unset):
            custom = CostItemgetRequestSchemaCustom.from_dict(_custom)

        inkoopprijs = d.pop("inkoopprijs", UNSET)

        is_template = d.pop("is_template", UNSET)

        ledger = d.pop("ledger", UNSET)

        name = d.pop("name", UNSET)

        remark = d.pop("remark", UNSET)

        taxclass = d.pop("taxclass", UNSET)

        verkoopprijs = d.pop("verkoopprijs", UNSET)

        cost_itemget_request_schema = cls(
            subproject=subproject,
            custom=custom,
            inkoopprijs=inkoopprijs,
            is_template=is_template,
            ledger=ledger,
            name=name,
            remark=remark,
            taxclass=taxclass,
            verkoopprijs=verkoopprijs,
        )

        cost_itemget_request_schema.additional_properties = d
        return cost_itemget_request_schema

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

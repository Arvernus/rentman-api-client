from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.serialnumber_itemget_request_schema_custom import SerialnumberItemgetRequestSchemaCustom
from ..types import UNSET, Unset

T = TypeVar("T", bound="SerialnumberItemgetRequestSchema")


@attr.s(auto_attribs=True)
class SerialnumberItemgetRequestSchema:
    """ """

    serial: Union[Unset, str] = UNSET
    purchasedate: Union[Unset, None, str] = UNSET
    depreciation_monthly: Union[Unset, float] = UNSET
    book_value: Union[Unset, float] = UNSET
    purchase_costs: Union[Unset, float] = UNSET
    active: Union[Unset, bool] = UNSET
    remark: Union[Unset, str] = UNSET
    ref: Union[Unset, str] = UNSET
    asset_location: Union[Unset, None, str] = UNSET
    custom: Union[Unset, SerialnumberItemgetRequestSchemaCustom] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        serial = self.serial
        purchasedate = self.purchasedate
        depreciation_monthly = self.depreciation_monthly
        book_value = self.book_value
        purchase_costs = self.purchase_costs
        active = self.active
        remark = self.remark
        ref = self.ref
        asset_location = self.asset_location
        custom: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.custom, Unset):
            custom = self.custom.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if serial is not UNSET:
            field_dict["serial"] = serial
        if purchasedate is not UNSET:
            field_dict["purchasedate"] = purchasedate
        if depreciation_monthly is not UNSET:
            field_dict["depreciation_monthly"] = depreciation_monthly
        if book_value is not UNSET:
            field_dict["book_value"] = book_value
        if purchase_costs is not UNSET:
            field_dict["purchase_costs"] = purchase_costs
        if active is not UNSET:
            field_dict["active"] = active
        if remark is not UNSET:
            field_dict["remark"] = remark
        if ref is not UNSET:
            field_dict["ref"] = ref
        if asset_location is not UNSET:
            field_dict["asset_location"] = asset_location
        if custom is not UNSET:
            field_dict["custom"] = custom

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        serial = d.pop("serial", UNSET)

        purchasedate = d.pop("purchasedate", UNSET)

        depreciation_monthly = d.pop("depreciation_monthly", UNSET)

        book_value = d.pop("book_value", UNSET)

        purchase_costs = d.pop("purchase_costs", UNSET)

        active = d.pop("active", UNSET)

        remark = d.pop("remark", UNSET)

        ref = d.pop("ref", UNSET)

        asset_location = d.pop("asset_location", UNSET)

        custom: Union[Unset, SerialnumberItemgetRequestSchemaCustom] = UNSET
        _custom = d.pop("custom", UNSET)
        if not isinstance(_custom, Unset):
            custom = SerialnumberItemgetRequestSchemaCustom.from_dict(_custom)

        serialnumber_itemget_request_schema = cls(
            serial=serial,
            purchasedate=purchasedate,
            depreciation_monthly=depreciation_monthly,
            book_value=book_value,
            purchase_costs=purchase_costs,
            active=active,
            remark=remark,
            ref=ref,
            asset_location=asset_location,
            custom=custom,
        )

        serialnumber_itemget_request_schema.additional_properties = d
        return serialnumber_itemget_request_schema

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

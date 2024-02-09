from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.serial_number_itemget_request_schema_custom import SerialNumberItemgetRequestSchemaCustom
from ..types import UNSET, Unset

T = TypeVar("T", bound="SerialNumberItemgetRequestSchema")


@attr.s(auto_attribs=True)
class SerialNumberItemgetRequestSchema:
    """ """

    active: Union[Unset, bool] = UNSET
    asset_location: Union[Unset, None, str] = UNSET
    book_value: Union[Unset, float] = UNSET
    custom: Union[Unset, SerialNumberItemgetRequestSchemaCustom] = UNSET
    depreciation_monthly: Union[Unset, float] = UNSET
    purchase_costs: Union[Unset, float] = UNSET
    purchasedate: Union[Unset, None, str] = UNSET
    ref: Union[Unset, str] = UNSET
    remark: Union[Unset, str] = UNSET
    serial: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        active = self.active
        asset_location = self.asset_location
        book_value = self.book_value
        custom: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.custom, Unset):
            custom = self.custom.to_dict()

        depreciation_monthly = self.depreciation_monthly
        purchase_costs = self.purchase_costs
        purchasedate = self.purchasedate
        ref = self.ref
        remark = self.remark
        serial = self.serial

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if active is not UNSET:
            field_dict["active"] = active
        if asset_location is not UNSET:
            field_dict["asset_location"] = asset_location
        if book_value is not UNSET:
            field_dict["book_value"] = book_value
        if custom is not UNSET:
            field_dict["custom"] = custom
        if depreciation_monthly is not UNSET:
            field_dict["depreciation_monthly"] = depreciation_monthly
        if purchase_costs is not UNSET:
            field_dict["purchase_costs"] = purchase_costs
        if purchasedate is not UNSET:
            field_dict["purchasedate"] = purchasedate
        if ref is not UNSET:
            field_dict["ref"] = ref
        if remark is not UNSET:
            field_dict["remark"] = remark
        if serial is not UNSET:
            field_dict["serial"] = serial

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        active = d.pop("active", UNSET)

        asset_location = d.pop("asset_location", UNSET)

        book_value = d.pop("book_value", UNSET)

        custom: Union[Unset, SerialNumberItemgetRequestSchemaCustom] = UNSET
        _custom = d.pop("custom", UNSET)
        if not isinstance(_custom, Unset):
            custom = SerialNumberItemgetRequestSchemaCustom.from_dict(_custom)

        depreciation_monthly = d.pop("depreciation_monthly", UNSET)

        purchase_costs = d.pop("purchase_costs", UNSET)

        purchasedate = d.pop("purchasedate", UNSET)

        ref = d.pop("ref", UNSET)

        remark = d.pop("remark", UNSET)

        serial = d.pop("serial", UNSET)

        serial_number_itemget_request_schema = cls(
            active=active,
            asset_location=asset_location,
            book_value=book_value,
            custom=custom,
            depreciation_monthly=depreciation_monthly,
            purchase_costs=purchase_costs,
            purchasedate=purchasedate,
            ref=ref,
            remark=remark,
            serial=serial,
        )

        serial_number_itemget_request_schema.additional_properties = d
        return serial_number_itemget_request_schema

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

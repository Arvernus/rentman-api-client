import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.repair_itemget_request_schema_custom import RepairItemgetRequestSchemaCustom
from ..models.repair_itemget_request_schema_is_usable import RepairItemgetRequestSchemaIsUsable
from ..types import UNSET, Unset

T = TypeVar("T", bound="RepairItemgetRequestSchema")


@attr.s(auto_attribs=True)
class RepairItemgetRequestSchema:
    """ """

    serialnumber: Union[Unset, None, str] = UNSET
    reporter: Union[Unset, None, str] = UNSET
    assignee: Union[Unset, None, str] = UNSET
    external_repairer: Union[Unset, None, str] = UNSET
    number: Union[Unset, str] = UNSET
    repairperiod_start: Union[Unset, None, datetime.datetime] = UNSET
    repairperiod_end: Union[Unset, None, datetime.datetime] = UNSET
    amount: Union[Unset, int] = UNSET
    remark: Union[Unset, str] = UNSET
    repair_costs: Union[Unset, float] = UNSET
    is_usable: Union[Unset, RepairItemgetRequestSchemaIsUsable] = UNSET
    costs_charged_to_customer: Union[Unset, None, str] = UNSET
    subproject: Union[Unset, None, str] = UNSET
    stock_location: Union[Unset, None, str] = UNSET
    custom: Union[Unset, RepairItemgetRequestSchemaCustom] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        serialnumber = self.serialnumber
        reporter = self.reporter
        assignee = self.assignee
        external_repairer = self.external_repairer
        number = self.number
        repairperiod_start: Union[Unset, None, str] = UNSET
        if not isinstance(self.repairperiod_start, Unset):
            repairperiod_start = self.repairperiod_start.isoformat() if self.repairperiod_start else None

        repairperiod_end: Union[Unset, None, str] = UNSET
        if not isinstance(self.repairperiod_end, Unset):
            repairperiod_end = self.repairperiod_end.isoformat() if self.repairperiod_end else None

        amount = self.amount
        remark = self.remark
        repair_costs = self.repair_costs
        is_usable: Union[Unset, int] = UNSET
        if not isinstance(self.is_usable, Unset):
            is_usable = self.is_usable.value

        costs_charged_to_customer = self.costs_charged_to_customer
        subproject = self.subproject
        stock_location = self.stock_location
        custom: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.custom, Unset):
            custom = self.custom.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if serialnumber is not UNSET:
            field_dict["serialnumber"] = serialnumber
        if reporter is not UNSET:
            field_dict["reporter"] = reporter
        if assignee is not UNSET:
            field_dict["assignee"] = assignee
        if external_repairer is not UNSET:
            field_dict["external_repairer"] = external_repairer
        if number is not UNSET:
            field_dict["number"] = number
        if repairperiod_start is not UNSET:
            field_dict["repairperiod_start"] = repairperiod_start
        if repairperiod_end is not UNSET:
            field_dict["repairperiod_end"] = repairperiod_end
        if amount is not UNSET:
            field_dict["amount"] = amount
        if remark is not UNSET:
            field_dict["remark"] = remark
        if repair_costs is not UNSET:
            field_dict["repair_costs"] = repair_costs
        if is_usable is not UNSET:
            field_dict["is_usable"] = is_usable
        if costs_charged_to_customer is not UNSET:
            field_dict["costs_charged_to_customer"] = costs_charged_to_customer
        if subproject is not UNSET:
            field_dict["subproject"] = subproject
        if stock_location is not UNSET:
            field_dict["stock_location"] = stock_location
        if custom is not UNSET:
            field_dict["custom"] = custom

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        serialnumber = d.pop("serialnumber", UNSET)

        reporter = d.pop("reporter", UNSET)

        assignee = d.pop("assignee", UNSET)

        external_repairer = d.pop("external_repairer", UNSET)

        number = d.pop("number", UNSET)

        repairperiod_start = None
        _repairperiod_start = d.pop("repairperiod_start", UNSET)
        if _repairperiod_start is not None and not isinstance(_repairperiod_start, Unset):
            repairperiod_start = isoparse(_repairperiod_start)

        repairperiod_end = None
        _repairperiod_end = d.pop("repairperiod_end", UNSET)
        if _repairperiod_end is not None and not isinstance(_repairperiod_end, Unset):
            repairperiod_end = isoparse(_repairperiod_end)

        amount = d.pop("amount", UNSET)

        remark = d.pop("remark", UNSET)

        repair_costs = d.pop("repair_costs", UNSET)

        is_usable: Union[Unset, RepairItemgetRequestSchemaIsUsable] = UNSET
        _is_usable = d.pop("is_usable", UNSET)
        if not isinstance(_is_usable, Unset):
            is_usable = RepairItemgetRequestSchemaIsUsable(_is_usable)

        costs_charged_to_customer = d.pop("costs_charged_to_customer", UNSET)

        subproject = d.pop("subproject", UNSET)

        stock_location = d.pop("stock_location", UNSET)

        custom: Union[Unset, RepairItemgetRequestSchemaCustom] = UNSET
        _custom = d.pop("custom", UNSET)
        if not isinstance(_custom, Unset):
            custom = RepairItemgetRequestSchemaCustom.from_dict(_custom)

        repair_itemget_request_schema = cls(
            serialnumber=serialnumber,
            reporter=reporter,
            assignee=assignee,
            external_repairer=external_repairer,
            number=number,
            repairperiod_start=repairperiod_start,
            repairperiod_end=repairperiod_end,
            amount=amount,
            remark=remark,
            repair_costs=repair_costs,
            is_usable=is_usable,
            costs_charged_to_customer=costs_charged_to_customer,
            subproject=subproject,
            stock_location=stock_location,
            custom=custom,
        )

        repair_itemget_request_schema.additional_properties = d
        return repair_itemget_request_schema

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

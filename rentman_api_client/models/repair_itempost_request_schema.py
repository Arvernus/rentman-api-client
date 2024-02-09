import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.repair_itempost_request_schema_custom import RepairItempostRequestSchemaCustom
from ..models.repair_itempost_request_schema_is_usable import RepairItempostRequestSchemaIsUsable
from ..types import UNSET, Unset

T = TypeVar("T", bound="RepairItempostRequestSchema")


@attr.s(auto_attribs=True)
class RepairItempostRequestSchema:
    """ """

    amount: Union[Unset, int] = UNSET
    assignee: Union[Unset, None, str] = UNSET
    costs_charged_to_customer: Union[Unset, None, str] = UNSET
    custom: Union[Unset, RepairItempostRequestSchemaCustom] = UNSET
    external_repairer: Union[Unset, None, str] = UNSET
    is_usable: Union[Unset, RepairItempostRequestSchemaIsUsable] = UNSET
    number: Union[Unset, str] = UNSET
    remark: Union[Unset, str] = UNSET
    repair_costs: Union[Unset, float] = UNSET
    repairperiod_end: Union[Unset, None, datetime.datetime] = UNSET
    repairperiod_start: Union[Unset, None, datetime.datetime] = UNSET
    reporter: Union[Unset, None, str] = UNSET
    serialnumber: Union[Unset, None, str] = UNSET
    stock_location: Union[Unset, None, str] = UNSET
    subproject: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        amount = self.amount
        assignee = self.assignee
        costs_charged_to_customer = self.costs_charged_to_customer
        custom: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.custom, Unset):
            custom = self.custom.to_dict()

        external_repairer = self.external_repairer
        is_usable: Union[Unset, int] = UNSET
        if not isinstance(self.is_usable, Unset):
            is_usable = self.is_usable.value

        number = self.number
        remark = self.remark
        repair_costs = self.repair_costs
        repairperiod_end: Union[Unset, None, str] = UNSET
        if not isinstance(self.repairperiod_end, Unset):
            repairperiod_end = self.repairperiod_end.isoformat() if self.repairperiod_end else None

        repairperiod_start: Union[Unset, None, str] = UNSET
        if not isinstance(self.repairperiod_start, Unset):
            repairperiod_start = self.repairperiod_start.isoformat() if self.repairperiod_start else None

        reporter = self.reporter
        serialnumber = self.serialnumber
        stock_location = self.stock_location
        subproject = self.subproject

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if amount is not UNSET:
            field_dict["amount"] = amount
        if assignee is not UNSET:
            field_dict["assignee"] = assignee
        if costs_charged_to_customer is not UNSET:
            field_dict["costs_charged_to_customer"] = costs_charged_to_customer
        if custom is not UNSET:
            field_dict["custom"] = custom
        if external_repairer is not UNSET:
            field_dict["external_repairer"] = external_repairer
        if is_usable is not UNSET:
            field_dict["is_usable"] = is_usable
        if number is not UNSET:
            field_dict["number"] = number
        if remark is not UNSET:
            field_dict["remark"] = remark
        if repair_costs is not UNSET:
            field_dict["repair_costs"] = repair_costs
        if repairperiod_end is not UNSET:
            field_dict["repairperiod_end"] = repairperiod_end
        if repairperiod_start is not UNSET:
            field_dict["repairperiod_start"] = repairperiod_start
        if reporter is not UNSET:
            field_dict["reporter"] = reporter
        if serialnumber is not UNSET:
            field_dict["serialnumber"] = serialnumber
        if stock_location is not UNSET:
            field_dict["stock_location"] = stock_location
        if subproject is not UNSET:
            field_dict["subproject"] = subproject

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        amount = d.pop("amount", UNSET)

        assignee = d.pop("assignee", UNSET)

        costs_charged_to_customer = d.pop("costs_charged_to_customer", UNSET)

        custom: Union[Unset, RepairItempostRequestSchemaCustom] = UNSET
        _custom = d.pop("custom", UNSET)
        if not isinstance(_custom, Unset):
            custom = RepairItempostRequestSchemaCustom.from_dict(_custom)

        external_repairer = d.pop("external_repairer", UNSET)

        is_usable: Union[Unset, RepairItempostRequestSchemaIsUsable] = UNSET
        _is_usable = d.pop("is_usable", UNSET)
        if not isinstance(_is_usable, Unset):
            is_usable = RepairItempostRequestSchemaIsUsable(_is_usable)

        number = d.pop("number", UNSET)

        remark = d.pop("remark", UNSET)

        repair_costs = d.pop("repair_costs", UNSET)

        repairperiod_end = None
        _repairperiod_end = d.pop("repairperiod_end", UNSET)
        if _repairperiod_end is not None and not isinstance(_repairperiod_end, Unset):
            repairperiod_end = isoparse(_repairperiod_end)

        repairperiod_start = None
        _repairperiod_start = d.pop("repairperiod_start", UNSET)
        if _repairperiod_start is not None and not isinstance(_repairperiod_start, Unset):
            repairperiod_start = isoparse(_repairperiod_start)

        reporter = d.pop("reporter", UNSET)

        serialnumber = d.pop("serialnumber", UNSET)

        stock_location = d.pop("stock_location", UNSET)

        subproject = d.pop("subproject", UNSET)

        repair_itempost_request_schema = cls(
            amount=amount,
            assignee=assignee,
            costs_charged_to_customer=costs_charged_to_customer,
            custom=custom,
            external_repairer=external_repairer,
            is_usable=is_usable,
            number=number,
            remark=remark,
            repair_costs=repair_costs,
            repairperiod_end=repairperiod_end,
            repairperiod_start=repairperiod_start,
            reporter=reporter,
            serialnumber=serialnumber,
            stock_location=stock_location,
            subproject=subproject,
        )

        repair_itempost_request_schema.additional_properties = d
        return repair_itempost_request_schema

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

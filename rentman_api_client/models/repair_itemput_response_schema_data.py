import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.repair_itemput_response_schema_data_custom import RepairItemputResponseSchemaDataCustom
from ..models.repair_itemput_response_schema_data_is_usable import RepairItemputResponseSchemaDataIsUsable
from ..types import UNSET, Unset

T = TypeVar("T", bound="RepairItemputResponseSchemaData")


@attr.s(auto_attribs=True)
class RepairItemputResponseSchemaData:
    """All the data about the requested items"""

    amount: Union[Unset, int] = UNSET
    assignee: Union[Unset, None, str] = UNSET
    costs_charged_to_customer: Union[Unset, None, str] = UNSET
    created: Union[Unset, None, datetime.datetime] = UNSET
    creator: Union[Unset, None, str] = UNSET
    custom: Union[Unset, RepairItemputResponseSchemaDataCustom] = UNSET
    displayname: Union[Unset, str] = UNSET
    equipment: Union[Unset, str] = UNSET
    external_repairer: Union[Unset, None, str] = UNSET
    id: Union[Unset, int] = UNSET
    is_usable: Union[Unset, RepairItemputResponseSchemaDataIsUsable] = UNSET
    modified: Union[Unset, None, datetime.datetime] = UNSET
    number: Union[Unset, str] = UNSET
    remark: Union[Unset, str] = UNSET
    repair_costs: Union[Unset, float] = UNSET
    repairperiod_end: Union[Unset, None, datetime.datetime] = UNSET
    repairperiod_start: Union[Unset, None, datetime.datetime] = UNSET
    reporter: Union[Unset, None, str] = UNSET
    serialnumber: Union[Unset, None, str] = UNSET
    stock_location: Union[Unset, None, str] = UNSET
    subproject: Union[Unset, None, str] = UNSET
    tags: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        amount = self.amount
        assignee = self.assignee
        costs_charged_to_customer = self.costs_charged_to_customer
        created: Union[Unset, None, str] = UNSET
        if not isinstance(self.created, Unset):
            created = self.created.isoformat() if self.created else None

        creator = self.creator
        custom: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.custom, Unset):
            custom = self.custom.to_dict()

        displayname = self.displayname
        equipment = self.equipment
        external_repairer = self.external_repairer
        id = self.id
        is_usable: Union[Unset, int] = UNSET
        if not isinstance(self.is_usable, Unset):
            is_usable = self.is_usable.value

        modified: Union[Unset, None, str] = UNSET
        if not isinstance(self.modified, Unset):
            modified = self.modified.isoformat() if self.modified else None

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
        tags = self.tags

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if amount is not UNSET:
            field_dict["amount"] = amount
        if assignee is not UNSET:
            field_dict["assignee"] = assignee
        if costs_charged_to_customer is not UNSET:
            field_dict["costs_charged_to_customer"] = costs_charged_to_customer
        if created is not UNSET:
            field_dict["created"] = created
        if creator is not UNSET:
            field_dict["creator"] = creator
        if custom is not UNSET:
            field_dict["custom"] = custom
        if displayname is not UNSET:
            field_dict["displayname"] = displayname
        if equipment is not UNSET:
            field_dict["equipment"] = equipment
        if external_repairer is not UNSET:
            field_dict["external_repairer"] = external_repairer
        if id is not UNSET:
            field_dict["id"] = id
        if is_usable is not UNSET:
            field_dict["is_usable"] = is_usable
        if modified is not UNSET:
            field_dict["modified"] = modified
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
        if tags is not UNSET:
            field_dict["tags"] = tags

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        amount = d.pop("amount", UNSET)

        assignee = d.pop("assignee", UNSET)

        costs_charged_to_customer = d.pop("costs_charged_to_customer", UNSET)

        created = None
        _created = d.pop("created", UNSET)
        if _created is not None and not isinstance(_created, Unset):
            created = isoparse(_created)

        creator = d.pop("creator", UNSET)

        custom: Union[Unset, RepairItemputResponseSchemaDataCustom] = UNSET
        _custom = d.pop("custom", UNSET)
        if not isinstance(_custom, Unset):
            custom = RepairItemputResponseSchemaDataCustom.from_dict(_custom)

        displayname = d.pop("displayname", UNSET)

        equipment = d.pop("equipment", UNSET)

        external_repairer = d.pop("external_repairer", UNSET)

        id = d.pop("id", UNSET)

        is_usable: Union[Unset, RepairItemputResponseSchemaDataIsUsable] = UNSET
        _is_usable = d.pop("is_usable", UNSET)
        if not isinstance(_is_usable, Unset):
            is_usable = RepairItemputResponseSchemaDataIsUsable(_is_usable)

        modified = None
        _modified = d.pop("modified", UNSET)
        if _modified is not None and not isinstance(_modified, Unset):
            modified = isoparse(_modified)

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

        tags = d.pop("tags", UNSET)

        repair_itemput_response_schema_data = cls(
            amount=amount,
            assignee=assignee,
            costs_charged_to_customer=costs_charged_to_customer,
            created=created,
            creator=creator,
            custom=custom,
            displayname=displayname,
            equipment=equipment,
            external_repairer=external_repairer,
            id=id,
            is_usable=is_usable,
            modified=modified,
            number=number,
            remark=remark,
            repair_costs=repair_costs,
            repairperiod_end=repairperiod_end,
            repairperiod_start=repairperiod_start,
            reporter=reporter,
            serialnumber=serialnumber,
            stock_location=stock_location,
            subproject=subproject,
            tags=tags,
        )

        repair_itemput_response_schema_data.additional_properties = d
        return repair_itemput_response_schema_data

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

import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.reparatie_itemget_response_schema_data_custom import ReparatieItemgetResponseSchemaDataCustom
from ..models.reparatie_itemget_response_schema_data_is_usable import ReparatieItemgetResponseSchemaDataIsUsable
from ..types import UNSET, Unset

T = TypeVar("T", bound="ReparatieItemgetResponseSchemaData")


@attr.s(auto_attribs=True)
class ReparatieItemgetResponseSchemaData:
    """All the data about the requested items"""

    id: Union[Unset, int] = UNSET
    created: Union[Unset, None, datetime.datetime] = UNSET
    modified: Union[Unset, None, datetime.datetime] = UNSET
    creator: Union[Unset, None, str] = UNSET
    displayname: Union[Unset, str] = UNSET
    equipment: Union[Unset, str] = UNSET
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
    is_usable: Union[Unset, ReparatieItemgetResponseSchemaDataIsUsable] = UNSET
    costs_charged_to_customer: Union[Unset, None, str] = UNSET
    subproject: Union[Unset, None, str] = UNSET
    stock_location: Union[Unset, None, str] = UNSET
    tags: Union[Unset, str] = UNSET
    custom: Union[Unset, ReparatieItemgetResponseSchemaDataCustom] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        created: Union[Unset, None, str] = UNSET
        if not isinstance(self.created, Unset):
            created = self.created.isoformat() if self.created else None

        modified: Union[Unset, None, str] = UNSET
        if not isinstance(self.modified, Unset):
            modified = self.modified.isoformat() if self.modified else None

        creator = self.creator
        displayname = self.displayname
        equipment = self.equipment
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
        tags = self.tags
        custom: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.custom, Unset):
            custom = self.custom.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if created is not UNSET:
            field_dict["created"] = created
        if modified is not UNSET:
            field_dict["modified"] = modified
        if creator is not UNSET:
            field_dict["creator"] = creator
        if displayname is not UNSET:
            field_dict["displayname"] = displayname
        if equipment is not UNSET:
            field_dict["equipment"] = equipment
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
        if tags is not UNSET:
            field_dict["tags"] = tags
        if custom is not UNSET:
            field_dict["custom"] = custom

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        created = None
        _created = d.pop("created", UNSET)
        if _created is not None and not isinstance(_created, Unset):
            created = isoparse(_created)

        modified = None
        _modified = d.pop("modified", UNSET)
        if _modified is not None and not isinstance(_modified, Unset):
            modified = isoparse(_modified)

        creator = d.pop("creator", UNSET)

        displayname = d.pop("displayname", UNSET)

        equipment = d.pop("equipment", UNSET)

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

        is_usable: Union[Unset, ReparatieItemgetResponseSchemaDataIsUsable] = UNSET
        _is_usable = d.pop("is_usable", UNSET)
        if not isinstance(_is_usable, Unset):
            is_usable = ReparatieItemgetResponseSchemaDataIsUsable(_is_usable)

        costs_charged_to_customer = d.pop("costs_charged_to_customer", UNSET)

        subproject = d.pop("subproject", UNSET)

        stock_location = d.pop("stock_location", UNSET)

        tags = d.pop("tags", UNSET)

        custom: Union[Unset, ReparatieItemgetResponseSchemaDataCustom] = UNSET
        _custom = d.pop("custom", UNSET)
        if not isinstance(_custom, Unset):
            custom = ReparatieItemgetResponseSchemaDataCustom.from_dict(_custom)

        reparatie_itemget_response_schema_data = cls(
            id=id,
            created=created,
            modified=modified,
            creator=creator,
            displayname=displayname,
            equipment=equipment,
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
            tags=tags,
            custom=custom,
        )

        reparatie_itemget_response_schema_data.additional_properties = d
        return reparatie_itemget_response_schema_data

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

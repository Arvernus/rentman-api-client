import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.equipment_collectionput_response_schema_data_item_country_of_origin import (
    EquipmentCollectionputResponseSchemaDataItemCountryOfOrigin,
)
from ..models.equipment_collectionput_response_schema_data_item_custom import (
    EquipmentCollectionputResponseSchemaDataItemCustom,
)
from ..models.equipment_collectionput_response_schema_data_item_is_physical import (
    EquipmentCollectionputResponseSchemaDataItemIsPhysical,
)
from ..models.equipment_collectionput_response_schema_data_item_rental_sales import (
    EquipmentCollectionputResponseSchemaDataItemRentalSales,
)
from ..models.equipment_collectionput_response_schema_data_item_stock_management import (
    EquipmentCollectionputResponseSchemaDataItemStockManagement,
)
from ..models.equipment_collectionput_response_schema_data_item_type import (
    EquipmentCollectionputResponseSchemaDataItemType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="EquipmentCollectionputResponseSchemaDataItem")


@attr.s(auto_attribs=True)
class EquipmentCollectionputResponseSchemaDataItem:
    """ """

    can_edit_content_during_planning: Union[Unset, bool] = UNSET
    code: Union[Unset, str] = UNSET
    country_of_origin: Union[Unset, EquipmentCollectionputResponseSchemaDataItemCountryOfOrigin] = UNSET
    created: Union[Unset, None, datetime.datetime] = UNSET
    created_with_flexible_cases_equipment_database_flag: Union[Unset, bool] = UNSET
    creator: Union[Unset, None, str] = UNSET
    critical_stock_level: Union[Unset, int] = UNSET
    current: Union[Unset, float] = UNSET
    custom: Union[Unset, EquipmentCollectionputResponseSchemaDataItemCustom] = UNSET
    defaultgroup: Union[Unset, str] = UNSET
    displayname: Union[Unset, str] = UNSET
    external_remark: Union[Unset, str] = UNSET
    folder: Union[Unset, None, str] = UNSET
    height: Union[Unset, float] = UNSET
    id: Union[Unset, int] = UNSET
    image: Union[Unset, None, str] = UNSET
    in_archive: Union[Unset, bool] = UNSET
    in_planner: Union[Unset, bool] = UNSET
    in_shop: Union[Unset, bool] = UNSET
    internal_remark: Union[Unset, str] = UNSET
    is_combination: Union[Unset, bool] = UNSET
    is_physical: Union[Unset, EquipmentCollectionputResponseSchemaDataItemIsPhysical] = UNSET
    ledger: Union[Unset, None, str] = UNSET
    length: Union[Unset, float] = UNSET
    list_price: Union[Unset, float] = UNSET
    location_in_warehouse: Union[Unset, str] = UNSET
    modified: Union[Unset, None, datetime.datetime] = UNSET
    name: Union[Unset, str] = UNSET
    packed_per: Union[Unset, int] = UNSET
    power: Union[Unset, float] = UNSET
    price: Union[Unset, float] = UNSET
    qrcodes: Union[Unset, str] = UNSET
    qrcodes_of_serial_numbers: Union[Unset, str] = UNSET
    rental_sales: Union[Unset, EquipmentCollectionputResponseSchemaDataItemRentalSales] = UNSET
    shop_description_long: Union[Unset, str] = UNSET
    shop_description_short: Union[Unset, str] = UNSET
    shop_featured: Union[Unset, bool] = UNSET
    shop_seo_description: Union[Unset, str] = UNSET
    shop_seo_keyword: Union[Unset, str] = UNSET
    shop_seo_title: Union[Unset, str] = UNSET
    stock_management: Union[Unset, EquipmentCollectionputResponseSchemaDataItemStockManagement] = UNSET
    subrental_costs: Union[Unset, float] = UNSET
    surface_article: Union[Unset, bool] = UNSET
    tags: Union[Unset, str] = UNSET
    taxclass: Union[Unset, None, str] = UNSET
    temporary: Union[Unset, bool] = UNSET
    type: Union[Unset, EquipmentCollectionputResponseSchemaDataItemType] = UNSET
    unit: Union[Unset, str] = UNSET
    volume: Union[Unset, float] = UNSET
    weight: Union[Unset, float] = UNSET
    width: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        can_edit_content_during_planning = self.can_edit_content_during_planning
        code = self.code
        country_of_origin: Union[Unset, str] = UNSET
        if not isinstance(self.country_of_origin, Unset):
            country_of_origin = self.country_of_origin.value

        created: Union[Unset, None, str] = UNSET
        if not isinstance(self.created, Unset):
            created = self.created.isoformat() if self.created else None

        created_with_flexible_cases_equipment_database_flag = self.created_with_flexible_cases_equipment_database_flag
        creator = self.creator
        critical_stock_level = self.critical_stock_level
        current = self.current
        custom: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.custom, Unset):
            custom = self.custom.to_dict()

        defaultgroup = self.defaultgroup
        displayname = self.displayname
        external_remark = self.external_remark
        folder = self.folder
        height = self.height
        id = self.id
        image = self.image
        in_archive = self.in_archive
        in_planner = self.in_planner
        in_shop = self.in_shop
        internal_remark = self.internal_remark
        is_combination = self.is_combination
        is_physical: Union[Unset, str] = UNSET
        if not isinstance(self.is_physical, Unset):
            is_physical = self.is_physical.value

        ledger = self.ledger
        length = self.length
        list_price = self.list_price
        location_in_warehouse = self.location_in_warehouse
        modified: Union[Unset, None, str] = UNSET
        if not isinstance(self.modified, Unset):
            modified = self.modified.isoformat() if self.modified else None

        name = self.name
        packed_per = self.packed_per
        power = self.power
        price = self.price
        qrcodes = self.qrcodes
        qrcodes_of_serial_numbers = self.qrcodes_of_serial_numbers
        rental_sales: Union[Unset, str] = UNSET
        if not isinstance(self.rental_sales, Unset):
            rental_sales = self.rental_sales.value

        shop_description_long = self.shop_description_long
        shop_description_short = self.shop_description_short
        shop_featured = self.shop_featured
        shop_seo_description = self.shop_seo_description
        shop_seo_keyword = self.shop_seo_keyword
        shop_seo_title = self.shop_seo_title
        stock_management: Union[Unset, str] = UNSET
        if not isinstance(self.stock_management, Unset):
            stock_management = self.stock_management.value

        subrental_costs = self.subrental_costs
        surface_article = self.surface_article
        tags = self.tags
        taxclass = self.taxclass
        temporary = self.temporary
        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        unit = self.unit
        volume = self.volume
        weight = self.weight
        width = self.width

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if can_edit_content_during_planning is not UNSET:
            field_dict["can_edit_content_during_planning"] = can_edit_content_during_planning
        if code is not UNSET:
            field_dict["code"] = code
        if country_of_origin is not UNSET:
            field_dict["country_of_origin"] = country_of_origin
        if created is not UNSET:
            field_dict["created"] = created
        if created_with_flexible_cases_equipment_database_flag is not UNSET:
            field_dict[
                "created_with_flexible_cases_equipment_database_flag"
            ] = created_with_flexible_cases_equipment_database_flag
        if creator is not UNSET:
            field_dict["creator"] = creator
        if critical_stock_level is not UNSET:
            field_dict["critical_stock_level"] = critical_stock_level
        if current is not UNSET:
            field_dict["current"] = current
        if custom is not UNSET:
            field_dict["custom"] = custom
        if defaultgroup is not UNSET:
            field_dict["defaultgroup"] = defaultgroup
        if displayname is not UNSET:
            field_dict["displayname"] = displayname
        if external_remark is not UNSET:
            field_dict["external_remark"] = external_remark
        if folder is not UNSET:
            field_dict["folder"] = folder
        if height is not UNSET:
            field_dict["height"] = height
        if id is not UNSET:
            field_dict["id"] = id
        if image is not UNSET:
            field_dict["image"] = image
        if in_archive is not UNSET:
            field_dict["in_archive"] = in_archive
        if in_planner is not UNSET:
            field_dict["in_planner"] = in_planner
        if in_shop is not UNSET:
            field_dict["in_shop"] = in_shop
        if internal_remark is not UNSET:
            field_dict["internal_remark"] = internal_remark
        if is_combination is not UNSET:
            field_dict["is_combination"] = is_combination
        if is_physical is not UNSET:
            field_dict["is_physical"] = is_physical
        if ledger is not UNSET:
            field_dict["ledger"] = ledger
        if length is not UNSET:
            field_dict["length"] = length
        if list_price is not UNSET:
            field_dict["list_price"] = list_price
        if location_in_warehouse is not UNSET:
            field_dict["location_in_warehouse"] = location_in_warehouse
        if modified is not UNSET:
            field_dict["modified"] = modified
        if name is not UNSET:
            field_dict["name"] = name
        if packed_per is not UNSET:
            field_dict["packed_per"] = packed_per
        if power is not UNSET:
            field_dict["power"] = power
        if price is not UNSET:
            field_dict["price"] = price
        if qrcodes is not UNSET:
            field_dict["qrcodes"] = qrcodes
        if qrcodes_of_serial_numbers is not UNSET:
            field_dict["qrcodes_of_serial_numbers"] = qrcodes_of_serial_numbers
        if rental_sales is not UNSET:
            field_dict["rental_sales"] = rental_sales
        if shop_description_long is not UNSET:
            field_dict["shop_description_long"] = shop_description_long
        if shop_description_short is not UNSET:
            field_dict["shop_description_short"] = shop_description_short
        if shop_featured is not UNSET:
            field_dict["shop_featured"] = shop_featured
        if shop_seo_description is not UNSET:
            field_dict["shop_seo_description"] = shop_seo_description
        if shop_seo_keyword is not UNSET:
            field_dict["shop_seo_keyword"] = shop_seo_keyword
        if shop_seo_title is not UNSET:
            field_dict["shop_seo_title"] = shop_seo_title
        if stock_management is not UNSET:
            field_dict["stock_management"] = stock_management
        if subrental_costs is not UNSET:
            field_dict["subrental_costs"] = subrental_costs
        if surface_article is not UNSET:
            field_dict["surface_article"] = surface_article
        if tags is not UNSET:
            field_dict["tags"] = tags
        if taxclass is not UNSET:
            field_dict["taxclass"] = taxclass
        if temporary is not UNSET:
            field_dict["temporary"] = temporary
        if type is not UNSET:
            field_dict["type"] = type
        if unit is not UNSET:
            field_dict["unit"] = unit
        if volume is not UNSET:
            field_dict["volume"] = volume
        if weight is not UNSET:
            field_dict["weight"] = weight
        if width is not UNSET:
            field_dict["width"] = width

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        can_edit_content_during_planning = d.pop("can_edit_content_during_planning", UNSET)

        code = d.pop("code", UNSET)

        country_of_origin: Union[Unset, EquipmentCollectionputResponseSchemaDataItemCountryOfOrigin] = UNSET
        _country_of_origin = d.pop("country_of_origin", UNSET)
        if not isinstance(_country_of_origin, Unset):
            country_of_origin = EquipmentCollectionputResponseSchemaDataItemCountryOfOrigin(_country_of_origin)

        created = None
        _created = d.pop("created", UNSET)
        if _created is not None and not isinstance(_created, Unset):
            created = isoparse(_created)

        created_with_flexible_cases_equipment_database_flag = d.pop(
            "created_with_flexible_cases_equipment_database_flag", UNSET
        )

        creator = d.pop("creator", UNSET)

        critical_stock_level = d.pop("critical_stock_level", UNSET)

        current = d.pop("current", UNSET)

        custom: Union[Unset, EquipmentCollectionputResponseSchemaDataItemCustom] = UNSET
        _custom = d.pop("custom", UNSET)
        if not isinstance(_custom, Unset):
            custom = EquipmentCollectionputResponseSchemaDataItemCustom.from_dict(_custom)

        defaultgroup = d.pop("defaultgroup", UNSET)

        displayname = d.pop("displayname", UNSET)

        external_remark = d.pop("external_remark", UNSET)

        folder = d.pop("folder", UNSET)

        height = d.pop("height", UNSET)

        id = d.pop("id", UNSET)

        image = d.pop("image", UNSET)

        in_archive = d.pop("in_archive", UNSET)

        in_planner = d.pop("in_planner", UNSET)

        in_shop = d.pop("in_shop", UNSET)

        internal_remark = d.pop("internal_remark", UNSET)

        is_combination = d.pop("is_combination", UNSET)

        is_physical: Union[Unset, EquipmentCollectionputResponseSchemaDataItemIsPhysical] = UNSET
        _is_physical = d.pop("is_physical", UNSET)
        if not isinstance(_is_physical, Unset):
            is_physical = EquipmentCollectionputResponseSchemaDataItemIsPhysical(_is_physical)

        ledger = d.pop("ledger", UNSET)

        length = d.pop("length", UNSET)

        list_price = d.pop("list_price", UNSET)

        location_in_warehouse = d.pop("location_in_warehouse", UNSET)

        modified = None
        _modified = d.pop("modified", UNSET)
        if _modified is not None and not isinstance(_modified, Unset):
            modified = isoparse(_modified)

        name = d.pop("name", UNSET)

        packed_per = d.pop("packed_per", UNSET)

        power = d.pop("power", UNSET)

        price = d.pop("price", UNSET)

        qrcodes = d.pop("qrcodes", UNSET)

        qrcodes_of_serial_numbers = d.pop("qrcodes_of_serial_numbers", UNSET)

        rental_sales: Union[Unset, EquipmentCollectionputResponseSchemaDataItemRentalSales] = UNSET
        _rental_sales = d.pop("rental_sales", UNSET)
        if not isinstance(_rental_sales, Unset):
            rental_sales = EquipmentCollectionputResponseSchemaDataItemRentalSales(_rental_sales)

        shop_description_long = d.pop("shop_description_long", UNSET)

        shop_description_short = d.pop("shop_description_short", UNSET)

        shop_featured = d.pop("shop_featured", UNSET)

        shop_seo_description = d.pop("shop_seo_description", UNSET)

        shop_seo_keyword = d.pop("shop_seo_keyword", UNSET)

        shop_seo_title = d.pop("shop_seo_title", UNSET)

        stock_management: Union[Unset, EquipmentCollectionputResponseSchemaDataItemStockManagement] = UNSET
        _stock_management = d.pop("stock_management", UNSET)
        if not isinstance(_stock_management, Unset):
            stock_management = EquipmentCollectionputResponseSchemaDataItemStockManagement(_stock_management)

        subrental_costs = d.pop("subrental_costs", UNSET)

        surface_article = d.pop("surface_article", UNSET)

        tags = d.pop("tags", UNSET)

        taxclass = d.pop("taxclass", UNSET)

        temporary = d.pop("temporary", UNSET)

        type: Union[Unset, EquipmentCollectionputResponseSchemaDataItemType] = UNSET
        _type = d.pop("type", UNSET)
        if not isinstance(_type, Unset):
            type = EquipmentCollectionputResponseSchemaDataItemType(_type)

        unit = d.pop("unit", UNSET)

        volume = d.pop("volume", UNSET)

        weight = d.pop("weight", UNSET)

        width = d.pop("width", UNSET)

        equipment_collectionput_response_schema_data_item = cls(
            can_edit_content_during_planning=can_edit_content_during_planning,
            code=code,
            country_of_origin=country_of_origin,
            created=created,
            created_with_flexible_cases_equipment_database_flag=created_with_flexible_cases_equipment_database_flag,
            creator=creator,
            critical_stock_level=critical_stock_level,
            current=current,
            custom=custom,
            defaultgroup=defaultgroup,
            displayname=displayname,
            external_remark=external_remark,
            folder=folder,
            height=height,
            id=id,
            image=image,
            in_archive=in_archive,
            in_planner=in_planner,
            in_shop=in_shop,
            internal_remark=internal_remark,
            is_combination=is_combination,
            is_physical=is_physical,
            ledger=ledger,
            length=length,
            list_price=list_price,
            location_in_warehouse=location_in_warehouse,
            modified=modified,
            name=name,
            packed_per=packed_per,
            power=power,
            price=price,
            qrcodes=qrcodes,
            qrcodes_of_serial_numbers=qrcodes_of_serial_numbers,
            rental_sales=rental_sales,
            shop_description_long=shop_description_long,
            shop_description_short=shop_description_short,
            shop_featured=shop_featured,
            shop_seo_description=shop_seo_description,
            shop_seo_keyword=shop_seo_keyword,
            shop_seo_title=shop_seo_title,
            stock_management=stock_management,
            subrental_costs=subrental_costs,
            surface_article=surface_article,
            tags=tags,
            taxclass=taxclass,
            temporary=temporary,
            type=type,
            unit=unit,
            volume=volume,
            weight=weight,
            width=width,
        )

        equipment_collectionput_response_schema_data_item.additional_properties = d
        return equipment_collectionput_response_schema_data_item

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

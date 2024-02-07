from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.materiaal_itemput_request_schema_country_of_origin import MateriaalItemputRequestSchemaCountryOfOrigin
from ..models.materiaal_itemput_request_schema_custom import MateriaalItemputRequestSchemaCustom
from ..models.materiaal_itemput_request_schema_is_physical import MateriaalItemputRequestSchemaIsPhysical
from ..models.materiaal_itemput_request_schema_rental_sales import MateriaalItemputRequestSchemaRentalSales
from ..models.materiaal_itemput_request_schema_stock_management import MateriaalItemputRequestSchemaStockManagement
from ..models.materiaal_itemput_request_schema_type import MateriaalItemputRequestSchemaType
from ..types import UNSET, Unset

T = TypeVar("T", bound="MateriaalItemputRequestSchema")


@attr.s(auto_attribs=True)
class MateriaalItemputRequestSchema:
    """ """

    folder: Union[Unset, None, str] = UNSET
    code: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    internal_remark: Union[Unset, str] = UNSET
    external_remark: Union[Unset, str] = UNSET
    location_in_warehouse: Union[Unset, str] = UNSET
    unit: Union[Unset, str] = UNSET
    in_shop: Union[Unset, bool] = UNSET
    surface_article: Union[Unset, bool] = UNSET
    shop_description_short: Union[Unset, str] = UNSET
    shop_description_long: Union[Unset, str] = UNSET
    shop_seo_title: Union[Unset, str] = UNSET
    shop_seo_keyword: Union[Unset, str] = UNSET
    shop_seo_description: Union[Unset, str] = UNSET
    shop_featured: Union[Unset, bool] = UNSET
    price: Union[Unset, float] = UNSET
    subrental_costs: Union[Unset, float] = UNSET
    critical_stock_level: Union[Unset, int] = UNSET
    type: Union[Unset, MateriaalItemputRequestSchemaType] = UNSET
    rental_sales: Union[Unset, MateriaalItemputRequestSchemaRentalSales] = UNSET
    temporary: Union[Unset, bool] = UNSET
    in_planner: Union[Unset, bool] = UNSET
    in_archive: Union[Unset, bool] = UNSET
    stock_management: Union[Unset, MateriaalItemputRequestSchemaStockManagement] = UNSET
    taxclass: Union[Unset, None, str] = UNSET
    list_price: Union[Unset, float] = UNSET
    volume: Union[Unset, float] = UNSET
    packed_per: Union[Unset, int] = UNSET
    height: Union[Unset, float] = UNSET
    width: Union[Unset, float] = UNSET
    length: Union[Unset, float] = UNSET
    weight: Union[Unset, float] = UNSET
    power: Union[Unset, float] = UNSET
    current: Union[Unset, float] = UNSET
    country_of_origin: Union[Unset, MateriaalItemputRequestSchemaCountryOfOrigin] = UNSET
    image: Union[Unset, None, str] = UNSET
    ledger: Union[Unset, None, str] = UNSET
    defaultgroup: Union[Unset, str] = UNSET
    is_combination: Union[Unset, bool] = UNSET
    is_physical: Union[Unset, MateriaalItemputRequestSchemaIsPhysical] = UNSET
    can_edit_content_during_planning: Union[Unset, bool] = UNSET
    created_with_flexible_cases_equipment_database_flag: Union[Unset, bool] = UNSET
    custom: Union[Unset, MateriaalItemputRequestSchemaCustom] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        folder = self.folder
        code = self.code
        name = self.name
        internal_remark = self.internal_remark
        external_remark = self.external_remark
        location_in_warehouse = self.location_in_warehouse
        unit = self.unit
        in_shop = self.in_shop
        surface_article = self.surface_article
        shop_description_short = self.shop_description_short
        shop_description_long = self.shop_description_long
        shop_seo_title = self.shop_seo_title
        shop_seo_keyword = self.shop_seo_keyword
        shop_seo_description = self.shop_seo_description
        shop_featured = self.shop_featured
        price = self.price
        subrental_costs = self.subrental_costs
        critical_stock_level = self.critical_stock_level
        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        rental_sales: Union[Unset, str] = UNSET
        if not isinstance(self.rental_sales, Unset):
            rental_sales = self.rental_sales.value

        temporary = self.temporary
        in_planner = self.in_planner
        in_archive = self.in_archive
        stock_management: Union[Unset, str] = UNSET
        if not isinstance(self.stock_management, Unset):
            stock_management = self.stock_management.value

        taxclass = self.taxclass
        list_price = self.list_price
        volume = self.volume
        packed_per = self.packed_per
        height = self.height
        width = self.width
        length = self.length
        weight = self.weight
        power = self.power
        current = self.current
        country_of_origin: Union[Unset, str] = UNSET
        if not isinstance(self.country_of_origin, Unset):
            country_of_origin = self.country_of_origin.value

        image = self.image
        ledger = self.ledger
        defaultgroup = self.defaultgroup
        is_combination = self.is_combination
        is_physical: Union[Unset, str] = UNSET
        if not isinstance(self.is_physical, Unset):
            is_physical = self.is_physical.value

        can_edit_content_during_planning = self.can_edit_content_during_planning
        created_with_flexible_cases_equipment_database_flag = self.created_with_flexible_cases_equipment_database_flag
        custom: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.custom, Unset):
            custom = self.custom.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if folder is not UNSET:
            field_dict["folder"] = folder
        if code is not UNSET:
            field_dict["code"] = code
        if name is not UNSET:
            field_dict["name"] = name
        if internal_remark is not UNSET:
            field_dict["internal_remark"] = internal_remark
        if external_remark is not UNSET:
            field_dict["external_remark"] = external_remark
        if location_in_warehouse is not UNSET:
            field_dict["location_in_warehouse"] = location_in_warehouse
        if unit is not UNSET:
            field_dict["unit"] = unit
        if in_shop is not UNSET:
            field_dict["in_shop"] = in_shop
        if surface_article is not UNSET:
            field_dict["surface_article"] = surface_article
        if shop_description_short is not UNSET:
            field_dict["shop_description_short"] = shop_description_short
        if shop_description_long is not UNSET:
            field_dict["shop_description_long"] = shop_description_long
        if shop_seo_title is not UNSET:
            field_dict["shop_seo_title"] = shop_seo_title
        if shop_seo_keyword is not UNSET:
            field_dict["shop_seo_keyword"] = shop_seo_keyword
        if shop_seo_description is not UNSET:
            field_dict["shop_seo_description"] = shop_seo_description
        if shop_featured is not UNSET:
            field_dict["shop_featured"] = shop_featured
        if price is not UNSET:
            field_dict["price"] = price
        if subrental_costs is not UNSET:
            field_dict["subrental_costs"] = subrental_costs
        if critical_stock_level is not UNSET:
            field_dict["critical_stock_level"] = critical_stock_level
        if type is not UNSET:
            field_dict["type"] = type
        if rental_sales is not UNSET:
            field_dict["rental_sales"] = rental_sales
        if temporary is not UNSET:
            field_dict["temporary"] = temporary
        if in_planner is not UNSET:
            field_dict["in_planner"] = in_planner
        if in_archive is not UNSET:
            field_dict["in_archive"] = in_archive
        if stock_management is not UNSET:
            field_dict["stock_management"] = stock_management
        if taxclass is not UNSET:
            field_dict["taxclass"] = taxclass
        if list_price is not UNSET:
            field_dict["list_price"] = list_price
        if volume is not UNSET:
            field_dict["volume"] = volume
        if packed_per is not UNSET:
            field_dict["packed_per"] = packed_per
        if height is not UNSET:
            field_dict["height"] = height
        if width is not UNSET:
            field_dict["width"] = width
        if length is not UNSET:
            field_dict["length"] = length
        if weight is not UNSET:
            field_dict["weight"] = weight
        if power is not UNSET:
            field_dict["power"] = power
        if current is not UNSET:
            field_dict["current"] = current
        if country_of_origin is not UNSET:
            field_dict["country_of_origin"] = country_of_origin
        if image is not UNSET:
            field_dict["image"] = image
        if ledger is not UNSET:
            field_dict["ledger"] = ledger
        if defaultgroup is not UNSET:
            field_dict["defaultgroup"] = defaultgroup
        if is_combination is not UNSET:
            field_dict["is_combination"] = is_combination
        if is_physical is not UNSET:
            field_dict["is_physical"] = is_physical
        if can_edit_content_during_planning is not UNSET:
            field_dict["can_edit_content_during_planning"] = can_edit_content_during_planning
        if created_with_flexible_cases_equipment_database_flag is not UNSET:
            field_dict[
                "created_with_flexible_cases_equipment_database_flag"
            ] = created_with_flexible_cases_equipment_database_flag
        if custom is not UNSET:
            field_dict["custom"] = custom

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        folder = d.pop("folder", UNSET)

        code = d.pop("code", UNSET)

        name = d.pop("name", UNSET)

        internal_remark = d.pop("internal_remark", UNSET)

        external_remark = d.pop("external_remark", UNSET)

        location_in_warehouse = d.pop("location_in_warehouse", UNSET)

        unit = d.pop("unit", UNSET)

        in_shop = d.pop("in_shop", UNSET)

        surface_article = d.pop("surface_article", UNSET)

        shop_description_short = d.pop("shop_description_short", UNSET)

        shop_description_long = d.pop("shop_description_long", UNSET)

        shop_seo_title = d.pop("shop_seo_title", UNSET)

        shop_seo_keyword = d.pop("shop_seo_keyword", UNSET)

        shop_seo_description = d.pop("shop_seo_description", UNSET)

        shop_featured = d.pop("shop_featured", UNSET)

        price = d.pop("price", UNSET)

        subrental_costs = d.pop("subrental_costs", UNSET)

        critical_stock_level = d.pop("critical_stock_level", UNSET)

        type: Union[Unset, MateriaalItemputRequestSchemaType] = UNSET
        _type = d.pop("type", UNSET)
        if not isinstance(_type, Unset):
            type = MateriaalItemputRequestSchemaType(_type)

        rental_sales: Union[Unset, MateriaalItemputRequestSchemaRentalSales] = UNSET
        _rental_sales = d.pop("rental_sales", UNSET)
        if not isinstance(_rental_sales, Unset):
            rental_sales = MateriaalItemputRequestSchemaRentalSales(_rental_sales)

        temporary = d.pop("temporary", UNSET)

        in_planner = d.pop("in_planner", UNSET)

        in_archive = d.pop("in_archive", UNSET)

        stock_management: Union[Unset, MateriaalItemputRequestSchemaStockManagement] = UNSET
        _stock_management = d.pop("stock_management", UNSET)
        if not isinstance(_stock_management, Unset):
            stock_management = MateriaalItemputRequestSchemaStockManagement(_stock_management)

        taxclass = d.pop("taxclass", UNSET)

        list_price = d.pop("list_price", UNSET)

        volume = d.pop("volume", UNSET)

        packed_per = d.pop("packed_per", UNSET)

        height = d.pop("height", UNSET)

        width = d.pop("width", UNSET)

        length = d.pop("length", UNSET)

        weight = d.pop("weight", UNSET)

        power = d.pop("power", UNSET)

        current = d.pop("current", UNSET)

        country_of_origin: Union[Unset, MateriaalItemputRequestSchemaCountryOfOrigin] = UNSET
        _country_of_origin = d.pop("country_of_origin", UNSET)
        if not isinstance(_country_of_origin, Unset):
            country_of_origin = MateriaalItemputRequestSchemaCountryOfOrigin(_country_of_origin)

        image = d.pop("image", UNSET)

        ledger = d.pop("ledger", UNSET)

        defaultgroup = d.pop("defaultgroup", UNSET)

        is_combination = d.pop("is_combination", UNSET)

        is_physical: Union[Unset, MateriaalItemputRequestSchemaIsPhysical] = UNSET
        _is_physical = d.pop("is_physical", UNSET)
        if not isinstance(_is_physical, Unset):
            is_physical = MateriaalItemputRequestSchemaIsPhysical(_is_physical)

        can_edit_content_during_planning = d.pop("can_edit_content_during_planning", UNSET)

        created_with_flexible_cases_equipment_database_flag = d.pop(
            "created_with_flexible_cases_equipment_database_flag", UNSET
        )

        custom: Union[Unset, MateriaalItemputRequestSchemaCustom] = UNSET
        _custom = d.pop("custom", UNSET)
        if not isinstance(_custom, Unset):
            custom = MateriaalItemputRequestSchemaCustom.from_dict(_custom)

        materiaal_itemput_request_schema = cls(
            folder=folder,
            code=code,
            name=name,
            internal_remark=internal_remark,
            external_remark=external_remark,
            location_in_warehouse=location_in_warehouse,
            unit=unit,
            in_shop=in_shop,
            surface_article=surface_article,
            shop_description_short=shop_description_short,
            shop_description_long=shop_description_long,
            shop_seo_title=shop_seo_title,
            shop_seo_keyword=shop_seo_keyword,
            shop_seo_description=shop_seo_description,
            shop_featured=shop_featured,
            price=price,
            subrental_costs=subrental_costs,
            critical_stock_level=critical_stock_level,
            type=type,
            rental_sales=rental_sales,
            temporary=temporary,
            in_planner=in_planner,
            in_archive=in_archive,
            stock_management=stock_management,
            taxclass=taxclass,
            list_price=list_price,
            volume=volume,
            packed_per=packed_per,
            height=height,
            width=width,
            length=length,
            weight=weight,
            power=power,
            current=current,
            country_of_origin=country_of_origin,
            image=image,
            ledger=ledger,
            defaultgroup=defaultgroup,
            is_combination=is_combination,
            is_physical=is_physical,
            can_edit_content_during_planning=can_edit_content_during_planning,
            created_with_flexible_cases_equipment_database_flag=created_with_flexible_cases_equipment_database_flag,
            custom=custom,
        )

        materiaal_itemput_request_schema.additional_properties = d
        return materiaal_itemput_request_schema

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

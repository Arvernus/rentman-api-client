from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.file_itemget_request_schema_previewstatus import FileItemgetRequestSchemaPreviewstatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="FileItemgetRequestSchema")


@attr.s(auto_attribs=True)
class FileItemgetRequestSchema:
    """ """

    classified: Union[Unset, bool] = UNSET
    description: Union[Unset, str] = UNSET
    expiration: Union[Unset, None, str] = UNSET
    file_item: Union[Unset, int] = UNSET
    file_itemtype: Union[Unset, str] = UNSET
    image: Union[Unset, bool] = UNSET
    in_documents: Union[Unset, bool] = UNSET
    in_webshop: Union[Unset, bool] = UNSET
    itemtype: Union[Unset, None, int] = UNSET
    preview_of: Union[Unset, None, str] = UNSET
    previewstatus: Union[Unset, FileItemgetRequestSchemaPreviewstatus] = UNSET
    public: Union[Unset, bool] = UNSET
    readable_name: Union[Unset, str] = UNSET
    size: Union[Unset, int] = UNSET
    type: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        classified = self.classified
        description = self.description
        expiration = self.expiration
        file_item = self.file_item
        file_itemtype = self.file_itemtype
        image = self.image
        in_documents = self.in_documents
        in_webshop = self.in_webshop
        itemtype = self.itemtype
        preview_of = self.preview_of
        previewstatus: Union[Unset, bool] = UNSET
        if not isinstance(self.previewstatus, Unset):
            previewstatus = self.previewstatus.value

        public = self.public
        readable_name = self.readable_name
        size = self.size
        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if classified is not UNSET:
            field_dict["classified"] = classified
        if description is not UNSET:
            field_dict["description"] = description
        if expiration is not UNSET:
            field_dict["expiration"] = expiration
        if file_item is not UNSET:
            field_dict["file_item"] = file_item
        if file_itemtype is not UNSET:
            field_dict["file_itemtype"] = file_itemtype
        if image is not UNSET:
            field_dict["image"] = image
        if in_documents is not UNSET:
            field_dict["in_documents"] = in_documents
        if in_webshop is not UNSET:
            field_dict["in_webshop"] = in_webshop
        if itemtype is not UNSET:
            field_dict["itemtype"] = itemtype
        if preview_of is not UNSET:
            field_dict["preview_of"] = preview_of
        if previewstatus is not UNSET:
            field_dict["previewstatus"] = previewstatus
        if public is not UNSET:
            field_dict["public"] = public
        if readable_name is not UNSET:
            field_dict["readable_name"] = readable_name
        if size is not UNSET:
            field_dict["size"] = size
        if type is not UNSET:
            field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        classified = d.pop("classified", UNSET)

        description = d.pop("description", UNSET)

        expiration = d.pop("expiration", UNSET)

        file_item = d.pop("file_item", UNSET)

        file_itemtype = d.pop("file_itemtype", UNSET)

        image = d.pop("image", UNSET)

        in_documents = d.pop("in_documents", UNSET)

        in_webshop = d.pop("in_webshop", UNSET)

        itemtype = d.pop("itemtype", UNSET)

        preview_of = d.pop("preview_of", UNSET)

        previewstatus: Union[Unset, FileItemgetRequestSchemaPreviewstatus] = UNSET
        _previewstatus = d.pop("previewstatus", UNSET)
        if not isinstance(_previewstatus, Unset):
            previewstatus = FileItemgetRequestSchemaPreviewstatus(_previewstatus)

        public = d.pop("public", UNSET)

        readable_name = d.pop("readable_name", UNSET)

        size = d.pop("size", UNSET)

        type = d.pop("type", UNSET)

        file_itemget_request_schema = cls(
            classified=classified,
            description=description,
            expiration=expiration,
            file_item=file_item,
            file_itemtype=file_itemtype,
            image=image,
            in_documents=in_documents,
            in_webshop=in_webshop,
            itemtype=itemtype,
            preview_of=preview_of,
            previewstatus=previewstatus,
            public=public,
            readable_name=readable_name,
            size=size,
            type=type,
        )

        file_itemget_request_schema.additional_properties = d
        return file_itemget_request_schema

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

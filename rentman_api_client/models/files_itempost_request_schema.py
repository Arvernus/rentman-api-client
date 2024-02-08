from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.files_itempost_request_schema_previewstatus import FilesItempostRequestSchemaPreviewstatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="FilesItempostRequestSchema")


@attr.s(auto_attribs=True)
class FilesItempostRequestSchema:
    """ """

    readable_name: Union[Unset, str] = UNSET
    expiration: Union[Unset, None, str] = UNSET
    size: Union[Unset, int] = UNSET
    image: Union[Unset, bool] = UNSET
    itemtype: Union[Unset, None, int] = UNSET
    description: Union[Unset, str] = UNSET
    in_documents: Union[Unset, bool] = UNSET
    in_webshop: Union[Unset, bool] = UNSET
    classified: Union[Unset, bool] = UNSET
    public: Union[Unset, bool] = UNSET
    type: Union[Unset, str] = UNSET
    preview_of: Union[Unset, None, str] = UNSET
    previewstatus: Union[Unset, FilesItempostRequestSchemaPreviewstatus] = UNSET
    file_item: Union[Unset, int] = UNSET
    file_itemtype: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        readable_name = self.readable_name
        expiration = self.expiration
        size = self.size
        image = self.image
        itemtype = self.itemtype
        description = self.description
        in_documents = self.in_documents
        in_webshop = self.in_webshop
        classified = self.classified
        public = self.public
        type = self.type
        preview_of = self.preview_of
        previewstatus: Union[Unset, bool] = UNSET
        if not isinstance(self.previewstatus, Unset):
            previewstatus = self.previewstatus.value

        file_item = self.file_item
        file_itemtype = self.file_itemtype

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if readable_name is not UNSET:
            field_dict["readable_name"] = readable_name
        if expiration is not UNSET:
            field_dict["expiration"] = expiration
        if size is not UNSET:
            field_dict["size"] = size
        if image is not UNSET:
            field_dict["image"] = image
        if itemtype is not UNSET:
            field_dict["itemtype"] = itemtype
        if description is not UNSET:
            field_dict["description"] = description
        if in_documents is not UNSET:
            field_dict["in_documents"] = in_documents
        if in_webshop is not UNSET:
            field_dict["in_webshop"] = in_webshop
        if classified is not UNSET:
            field_dict["classified"] = classified
        if public is not UNSET:
            field_dict["public"] = public
        if type is not UNSET:
            field_dict["type"] = type
        if preview_of is not UNSET:
            field_dict["preview_of"] = preview_of
        if previewstatus is not UNSET:
            field_dict["previewstatus"] = previewstatus
        if file_item is not UNSET:
            field_dict["file_item"] = file_item
        if file_itemtype is not UNSET:
            field_dict["file_itemtype"] = file_itemtype

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        readable_name = d.pop("readable_name", UNSET)

        expiration = d.pop("expiration", UNSET)

        size = d.pop("size", UNSET)

        image = d.pop("image", UNSET)

        itemtype = d.pop("itemtype", UNSET)

        description = d.pop("description", UNSET)

        in_documents = d.pop("in_documents", UNSET)

        in_webshop = d.pop("in_webshop", UNSET)

        classified = d.pop("classified", UNSET)

        public = d.pop("public", UNSET)

        type = d.pop("type", UNSET)

        preview_of = d.pop("preview_of", UNSET)

        previewstatus: Union[Unset, FilesItempostRequestSchemaPreviewstatus] = UNSET
        _previewstatus = d.pop("previewstatus", UNSET)
        if not isinstance(_previewstatus, Unset):
            previewstatus = FilesItempostRequestSchemaPreviewstatus(_previewstatus)

        file_item = d.pop("file_item", UNSET)

        file_itemtype = d.pop("file_itemtype", UNSET)

        files_itempost_request_schema = cls(
            readable_name=readable_name,
            expiration=expiration,
            size=size,
            image=image,
            itemtype=itemtype,
            description=description,
            in_documents=in_documents,
            in_webshop=in_webshop,
            classified=classified,
            public=public,
            type=type,
            preview_of=preview_of,
            previewstatus=previewstatus,
            file_item=file_item,
            file_itemtype=file_itemtype,
        )

        files_itempost_request_schema.additional_properties = d
        return files_itempost_request_schema

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

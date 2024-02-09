from typing import Any, Dict, Optional

import httpx

from ...client import Client
from ...models.stockmovement_itemput_request_schema import StockmovementItemputRequestSchema
from ...models.stockmovement_itemput_response_schema import StockmovementItemputResponseSchema
from ...types import Response


def _get_kwargs(
    *,
    client: Client,
    id: int,
    json_body: StockmovementItemputRequestSchema,
) -> Dict[str, Any]:
    url = "{}/stockmovements/{id}".format(client.base_url, id=id)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body = json_body.to_dict()

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
    }


def _parse_response(*, response: httpx.Response) -> Optional[StockmovementItemputResponseSchema]:
    if response.status_code == 200:
        response_200 = StockmovementItemputResponseSchema.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[StockmovementItemputResponseSchema]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    id: int,
    json_body: StockmovementItemputRequestSchema,
) -> Response[StockmovementItemputResponseSchema]:
    kwargs = _get_kwargs(
        client=client,
        id=id,
        json_body=json_body,
    )

    response = httpx.put(
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
    id: int,
    json_body: StockmovementItemputRequestSchema,
) -> Optional[StockmovementItemputResponseSchema]:
    """ """

    return sync_detailed(
        client=client,
        id=id,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    id: int,
    json_body: StockmovementItemputRequestSchema,
) -> Response[StockmovementItemputResponseSchema]:
    kwargs = _get_kwargs(
        client=client,
        id=id,
        json_body=json_body,
    )

    async with httpx.AsyncClient() as _client:
        response = await _client.put(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    id: int,
    json_body: StockmovementItemputRequestSchema,
) -> Optional[StockmovementItemputResponseSchema]:
    """ """

    return (
        await asyncio_detailed(
            client=client,
            id=id,
            json_body=json_body,
        )
    ).parsed

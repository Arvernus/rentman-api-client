from typing import Any, Dict, Optional

import httpx

from ...client import Client
from ...models.stock_location_collectionget_response_schema import StockLocationCollectiongetResponseSchema
from ...types import Response


def _get_kwargs(
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/stocklocations".format(client.base_url)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[StockLocationCollectiongetResponseSchema]:
    if response.status_code == 200:
        response_200 = StockLocationCollectiongetResponseSchema.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[StockLocationCollectiongetResponseSchema]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
) -> Response[StockLocationCollectiongetResponseSchema]:
    kwargs = _get_kwargs(
        client=client,
    )

    response = httpx.get(
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
) -> Optional[StockLocationCollectiongetResponseSchema]:
    """ """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
) -> Response[StockLocationCollectiongetResponseSchema]:
    kwargs = _get_kwargs(
        client=client,
    )

    async with httpx.AsyncClient() as _client:
        response = await _client.get(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
) -> Optional[StockLocationCollectiongetResponseSchema]:
    """ """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed

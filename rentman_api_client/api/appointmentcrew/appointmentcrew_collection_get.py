from typing import Any, Dict, Optional

import httpx

from ...client import Client
from ...models.appointmentcrew_collectionget_response_schema import AppointmentcrewCollectiongetResponseSchema
from ...types import Response


def _get_kwargs(
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/appointmentcrew".format(client.base_url)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[AppointmentcrewCollectiongetResponseSchema]:
    if response.status_code == 200:
        response_200 = AppointmentcrewCollectiongetResponseSchema.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[AppointmentcrewCollectiongetResponseSchema]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
) -> Response[AppointmentcrewCollectiongetResponseSchema]:
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
) -> Optional[AppointmentcrewCollectiongetResponseSchema]:
    """ """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
) -> Response[AppointmentcrewCollectiongetResponseSchema]:
    kwargs = _get_kwargs(
        client=client,
    )

    async with httpx.AsyncClient() as _client:
        response = await _client.get(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
) -> Optional[AppointmentcrewCollectiongetResponseSchema]:
    """ """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed

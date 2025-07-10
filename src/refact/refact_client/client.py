import json
from typing import Any, AsyncGenerator

from aiohttp import ClientResponseError, ClientSession

from refact.config import REFACT_API_URL
from refact.refact_client.models import (
    ActRequest,
    ActResponse,
    ReasonRequest,
    ReasonResponse,
    RefactRequest,
)


class RefactClient:
    def __init__(self, client_session: ClientSession):
        self._client_session: ClientSession = client_session
        self._headers = {
            "Content-Type": "application/json",
        }

    async def _handle_response_error(self, response):
        """Handle non-200 responses and extract error details"""
        if response.status != 200:
            try:
                error_data = await response.json()
                detail = error_data.get("detail", "Unknown issue.")
                raise ClientResponseError(
                    request_info=response.request_info,
                    history=response.history,
                    status=response.status,
                    message=detail,
                )
            except (json.JSONDecodeError, KeyError):
                raise ClientResponseError(
                    request_info=response.request_info,
                    history=response.history,
                    status=response.status,
                    message="Unknown issue.",
                )

    async def refact(self, refact_request: RefactRequest) -> AsyncGenerator[str, None]:
        async with self._client_session.request(
            "POST",
            f"{REFACT_API_URL}/v1/refact",
            headers=self._headers,
            json=refact_request.model_dump(),
        ) as response:
            if response.status != 200:
                await self._handle_response_error(response)
            async for line in response.content:
                if line:
                    yield line.decode("utf-8")

    async def reason(self, reason_request: ReasonRequest) -> ReasonResponse:
        async with self._client_session.request(
            "POST",
            f"{REFACT_API_URL}/v1/reason",
            headers=self._headers,
            json=reason_request.model_dump(),
        ) as response:
            if response.status != 200:
                await self._handle_response_error(response)

            return ReasonResponse(**await response.json())

    async def act(self, action: ActRequest) -> ActResponse:
        async with self._client_session.request(
            "POST",
            f"{REFACT_API_URL}/v1/act",
            headers=self._headers,
            json=action.model_dump(),
        ) as response:
            if response.status != 200:
                await self._handle_response_error(response)

            return ActResponse(**await response.json())

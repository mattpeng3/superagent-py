# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import datetime as dt
import typing

import pydantic

from ..core.datetime_utils import serialize_datetime
from .tool_type import ToolType
from pydantic import ConfigDict


class PrismaModelsTool(pydantic.BaseModel):
    """
    Represents a Tool record
    """

    id: str
    name: str
    description: str
    type: ToolType
    return_direct: bool = pydantic.Field(alias="returnDirect")
    metadata: str
    created_at: dt.datetime = pydantic.Field(alias="createdAt")
    updated_at: dt.datetime = pydantic.Field(alias="updatedAt")
    api_user_id: str = pydantic.Field(alias="apiUserId")
    api_user: typing.Optional[PrismaModelsApiUser] = pydantic.Field(alias="apiUser")
    tools: typing.Optional[typing.List[PrismaModelsAgentTool]] = None

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)
    # TODO[pydantic]: The following keys were removed: `smart_union`, `json_encoders`.
    # Check https://docs.pydantic.dev/dev-v2/migration/#changes-to-config for more information.
    model_config = ConfigDict(frozen=True, smart_union=True, populate_by_name=True, json_encoders={dt.datetime: serialize_datetime})


from .prisma_models_agent_tool import PrismaModelsAgentTool  # noqa: E402
from .prisma_models_api_user import PrismaModelsApiUser  # noqa: E402

PrismaModelsTool.update_forward_refs()

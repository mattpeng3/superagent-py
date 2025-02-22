# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from ..core.datetime_utils import serialize_datetime
from .prisma_models_api_user import PrismaModelsApiUser
from pydantic import ConfigDict


class AppModelsResponseApiUser(pydantic.BaseModel):
    success: bool
    data: typing.Optional[PrismaModelsApiUser] = None

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)
    # TODO[pydantic]: The following keys were removed: `smart_union`, `json_encoders`.
    # Check https://docs.pydantic.dev/dev-v2/migration/#changes-to-config for more information.
    model_config = ConfigDict(frozen=True, smart_union=True, json_encoders={dt.datetime: serialize_datetime})

import base64
import binascii
import json
from typing import Annotated
from typing import Type, TypeVar, Generic
from pydantic import AfterValidator, BaseModel, PlainSerializer
from fastapi.exceptions import RequestValidationError


Base64DecodedJSONTypeVar = TypeVar("Base64DecodedJSONTypeVar", bound=BaseModel)


def base64decode(model: Type[Base64DecodedJSONTypeVar]):
    """Returns a validator that decodes Base64 and validates JSON with the given Pydantic model."""

    def validator(s: str) -> Base64DecodedJSONTypeVar:
        try:
            data = base64.b64decode(s).decode()
        except (binascii.Error, TypeError, ValueError):
            raise ValueError("An invalid base64 string was passed.")
        try:
            json_data = json.loads(data)
        except json.JSONDecodeError:
            raise ValueError("Invalid JSON structure was passed.")

        return model.model_validate(json_data)

    return AfterValidator(validator)

class Base64DecodedJSON(Generic[Base64DecodedJSONTypeVar]):
    def __class_getitem__(cls, model: Type[Base64DecodedJSONTypeVar]):
        return Annotated[str, base64decode(model)]


def int2bool(number: int) -> bool:
    try:
        return bool(number)
    except TypeError:
        raise RequestValidationError("Invalid binary value")

BinaryBoolType = Annotated[
    int,
    AfterValidator(int2bool),
    PlainSerializer(lambda v: bool(v))
]

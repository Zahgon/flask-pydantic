from functools import wraps
from typing import Any, Callable, Iterable, List, Optional, Tuple, Type, Union

from flask import Response, current_app, jsonify, make_response, request
from pydantic import BaseModel, RootModel, TypeAdapter, ValidationError
from pydantic.v1 import BaseModel as V1BaseModel
from pydantic.v1.error_wrappers import ValidationError as V1ValidationError
from pydantic.v1.tools import parse_obj_as

from .converters import convert_query_params
from .exceptions import (
    InvalidIterableOfModelsException,
    JsonBodyParsingError,
    ManyModelValidationError,
)
from .exceptions import ValidationError as FailedValidation

try:
    from flask_restful import original_flask_make_response as make_response
except ImportError:
    pass

V1OrV2BaseModel = Union[BaseModel, V1BaseModel]


def _model_dump_json(model: V1OrV2BaseModel, **kwargs):
    """Adapter to dump a model to json, whether it's a Pydantic V1 or V2 model."""
    pass


def _sanitize_ctx_errors(errors):
    """
    Make Pydantic `ctx["error"]` JSON-serializable by replacing
    exception instances with {type, message}.
    """
    pass


def make_json_response(
    content: Union[V1OrV2BaseModel, Iterable[V1OrV2BaseModel]],
    status_code: int,
    by_alias: bool,
    exclude_none: bool = False,
    many: bool = False,
) -> Response:
    """serializes model, creates JSON response with given status code"""
    pass












def validate(
    body: Optional[Type[V1OrV2BaseModel]] = None,
    query: Optional[Type[V1OrV2BaseModel]] = None,
    on_success_status: int = 200,
    exclude_none: bool = False,
    response_many: bool = False,
    request_body_many: bool = False,
    response_by_alias: bool = False,
    get_json_params: Optional[dict] = None,
    form: Optional[Type[V1OrV2BaseModel]] = None,
):
    """
    Decorator for route methods which will validate query, body and form parameters
    as well as serialize the response (if it derives from pydantic's BaseModel
    class).

    Request parameters are accessible via flask's `request` variable:
        - request.query_params
        - request.body_params
        - request.form_params

    Or directly as `kwargs`, if you define them in the decorated function.

    `exclude_none` whether to remove None fields from response
    `response_many` whether content of response consists of many objects
        (e. g. List[BaseModel]). Resulting response will be an array of serialized
        models.
    `request_body_many` whether response body contains array of given model
        (request.body_params then contains list of models i. e. List[BaseModel])
    `response_by_alias` whether Pydantic's alias is used
    `get_json_params` - parameters to be passed to Request.get_json() function

    example::

        from flask import request
        from flask_pydantic import validate
        from pydantic import BaseModel

        class Query(BaseModel):
            query: str

        class Body(BaseModel):
            color: str

        class Form(BaseModel):
            name: str

        class MyModel(BaseModel):
            id: int
            color: str
            description: str

        ...

        @app.route("/")
        @validate(query=Query, body=Body, form=Form)
        def test_route():
            query = request.query_params.query
            color = request.body_params.query

            return MyModel(...)

        @app.route("/kwargs")
        @validate()
        def test_route_kwargs(query:Query, body:Body, form:Form):

            return MyModel(...)

    -> that will render JSON response with serialized MyModel instance
    """
    pass

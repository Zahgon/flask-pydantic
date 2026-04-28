import types
from collections import deque
from typing import Deque, FrozenSet, List, Sequence, Set, Tuple, Type, Union

try:
    from typing import get_args, get_origin
except ImportError:
    from typing_extensions import get_args, get_origin

from pydantic import BaseModel
from pydantic.v1 import BaseModel as V1BaseModel
from werkzeug.datastructures import ImmutableMultiDict

V1OrV2BaseModel = Union[BaseModel, V1BaseModel]
UnionType = getattr(types, "UnionType", Union)

sequence_types = {
    Sequence,
    List,
    list,
    Tuple,
    tuple,
    Set,
    set,
    FrozenSet,
    frozenset,
    Deque,
    deque,
}




def convert_query_params(
    query_params: ImmutableMultiDict, model: Type[V1OrV2BaseModel]
) -> dict:
    """
    group query parameters into lists if model defines them

    :param query_params: flasks request.args
    :param model: query parameter's model
    :return: resulting parameters
    """
    pass

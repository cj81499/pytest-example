"""
This type stub file was generated by pyright.
"""

from types import TracebackType
from typing import (
    Any,
    Callable,
    Generic,
    Optional,
    Pattern,
    Tuple,
    Type,
    TypeVar,
    Union,
    final,
    overload,
)

import _pytest._code

E = TypeVar("E", bound=BaseException)

@overload
def raises(expected_exception: E) -> RaisesContext[E]: ...
@overload
def raises(
    expected_exception: Union[Type[E], Tuple[Type[E], ...]],
    *,
    match: Optional[Union[str, Pattern[str]]] = ...,
) -> RaisesContext[E]: ...
@overload
def raises(
    expected_exception: Union[Type[E], Tuple[Type[E], ...]],
    func: Callable[..., Any],
    *args: Any,
    **kwargs: Any,
) -> _pytest._code.ExceptionInfo[E]: ...
@final
class RaisesContext(Generic[E]):
    def __init__(
        self,
        expected_exception: Union[Type[E], Tuple[Type[E], ...]],
        message: str,
        match_expr: Optional[Union[str, Pattern[str]]] = ...,
    ) -> None: ...
    def __enter__(self) -> _pytest._code.ExceptionInfo[E]: ...
    def __exit__(
        self,
        exc_type: Optional[Type[BaseException]],
        exc_val: Optional[BaseException],
        exc_tb: Optional[TracebackType],
    ) -> bool: ...
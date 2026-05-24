import functools
from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cache_storage = {}

    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        key = (args, tuple(sorted(kwargs.items())))
        if key not in cache_storage:
            cache_storage[key] = func(*args, **kwargs)
        return cache_storage[key]
    return wrapper

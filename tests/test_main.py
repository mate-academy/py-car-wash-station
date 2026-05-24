import pytest
from app.main import cache


def test_cache_initial() -> None:
    @cache
    def inside_func(x: int) -> int:
        inside_func.calls += 1
        return x * 2

    inside_func.calls = 0

    assert inside_func(5) == 10
    assert inside_func(5) == 10
    # Якщо кеш працює, функція всередині викликалася лише 1 раз
    assert inside_func.calls == 1


def test_cache_with_multiple_arguments() -> None:
    @cache
    def add(a: int, b: int) -> int:
        add.calls += 1
        return a + b

    add.calls = 0

    assert add(2, 3) == 5
    assert add(2, 3) == 5
    assert add(4, 5) == 9
    assert add(2, 3) == 5
    assert add.calls == 2
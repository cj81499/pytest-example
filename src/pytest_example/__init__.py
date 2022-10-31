import typing as t


class MyException(Exception):
    pass


def example() -> t.NoReturn:
    raise MyException("my message")

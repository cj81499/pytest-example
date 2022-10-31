import re

import pytest

from pytest_example import MyException, example


def test_example_bad() -> None:
    with pytest.raises(MyException("my message")):
        example()


def test_example_good() -> None:
    with pytest.raises(MyException, match=re.escape("my message")):
        example()

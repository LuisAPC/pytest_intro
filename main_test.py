import pytest
from main import add

def test_add():
    assert add(2, 2) == 4

@pytest.mark.parametrize(
        "input_x, input_y, expected",
        [
            (3, 2, 5),
            (2, 3, 3),
            (add(3, 2), 5, 10),
            (3, add(2, 5), 10)
        ]
)
def test_add_parametrize(input_x, input_y, expected):
    assert add(input_x, input_y) == expected

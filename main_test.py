import pytest
from main import add, write

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

#utilizar tmpdir para no tener que crear un archivo y despues borrarlo, esto lo hace automaticamente
def test_write_tmp_dir(tmpdir):
    data_in = "Soy Luis"
    fpath = f"{tmpdir}/test_write_text.txt"
    write(fpath, data_in)

    with open(fpath) as file_out:
        data_out = file_out.read()

    assert data_in == "data_out"
    # assert data_in == data_out


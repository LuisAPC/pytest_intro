def add(x, y):
    return x+y

def write(fpath, data_in):
    with open(fpath, "w") as file_in:
        file_in.write(data_in)
def read_data(filename):
    lines = []
    fh = None
    try:
        fh = open(filename, encoding='utf8')
        for line in fh:
            if line.strip():
                lines.append(line)
    except (IOError, OSError) as err:
        print(err)
        return []
    finally:
        if fh is not None:
            fh.close()
    return lines


# 自定义异常
found = False


def append_if_even(x, lst=None):
    if lst is None:
        lst = []
    if x % 2 == 0:
        lst.append(x)
    return lst


#!
import string


def simplify(text, whitespace=string.whitespace, delete=""):
    result = []
    word = ""
    for char in text:
        if char in delete:
            continue
        elif char in whitespace:
            if word:
                result.append(word)
                word = ""
        else:
            word += char
        if word:
            result.append(word)
        return " ".join(result)


def is_balanced(text, brackets="(){}{}<>"):
    counts = {}
    left_for_right = {}
    for left, right in zip(brackets[::2], brackets[1::2]):
        assert left != right, "the bracket characters must differ"
        counts[left] = 0
        left_for_right[right] = left

    for c in text:
        if c in counts:
            counts[c] += 1
        elif c in left_for_right:
            left = left_for_right[c]
            if counts[left] == 0:
                return False
            counts[left] -= 1
    return not any(counts.values())


def resize(max_rows, max_columns, char=None):
    assert max_rows > 0 and max_columns > 0, 'too small'
    if char is not None:
        assert len(char) == 1
        _background_char = char
        _max_rows = max_rows
        _max_columns = max_columns
        _grid = [[_background_char for columns in range(_max_columns)] for row in range(_max_rows)]



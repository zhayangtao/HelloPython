def func():
    pass

func()
func.attr = 1


def intersect(seq1, seq2):
    res = []
    for x in seq1:
        if x in seq2:
            res.append(x)
    return res

s1 = []
s2 = []
[x for x in s1 if x in s2]


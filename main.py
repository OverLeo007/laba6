def inters_size(x1, y1, x2, y2, x3, y3, x4, y4):
    if (res := (min(y1, y3) - max(y2, y4)) * (min(x4, x2) - max(x1, x3))) < 0:
        return 0
    else:
        return res


def union_size(x1, y1, x2, y2, x3, y3, x4, y4):
    return (x2 - x1) * (y1 - y2) + (x4 - x3) * (y3 - y4) - inters_size(x1, y1, x2, y2, x3, y3, x4, y4) * 2



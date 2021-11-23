def inters_size(x1, y1, x2, y2, x3, y3, x4, y4):
    if (res := (min(y1, y3) - max(y2, y4)) * (min(x4, x2) - max(x1, x3))) < 0:
        return 0
    else:
        return res


def union_size(x1, y1, x2, y2, x3, y3, x4, y4):
    s_rect1 = (x2 - x1) * (y1 - y2)
    s_rect2 = (x4 - x3) * (y3 - y4)
    rect_inter = inters_size(x1, y1, x2, y2, x3, y3, x4, y4)
    if rect_inter == s_rect2 and rect_inter == s_rect1:
        return rect_inter
    elif rect_inter == s_rect2 or rect_inter == s_rect1:
        return s_rect1 + s_rect2 - rect_inter
    else:
        return s_rect1 + s_rect2 - rect_inter * 2



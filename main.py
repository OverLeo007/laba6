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
    elif rect_inter == s_rect2 and rect_inter == s_rect1:
        return s_rect1 + s_rect2 - rect_inter
    else:
        return s_rect1 + s_rect2 - rect_inter * 2


def main():
    print('Пример 1')
    print('Входные параметры: 1, 4, 5, 2, 3, 6, 7, 1')
    print('Площадь пересечения:', inters_size(1, 4, 5, 2, 3, 6, 7, 1))
    print('Площадь объединения:', union_size(1, 4, 5, 2, 3, 6, 7, 1))
    print('Пример 2')
    print('Входные параметры: 2, 2, 3, 1, 4, 5, 7, 2')
    print('Площадь пересечения:', inters_size(2, 2, 3, 1, 4, 5, 7, 2))
    print('Площадь объединения:', union_size(2, 2, 3, 1, 4, 5, 7, 2))
    print('Пример 3')
    print('Входные параметры: 2, 2, 3, 1, 2, 5, 7, 1')
    print('Площадь пересечения:', inters_size(2, 2, 3, 1, 2, 5, 7, 1))
    print('Площадь объединения:', union_size(2, 2, 3, 1, 2, 5, 7, 1))


if __name__ == '__main__':
    main()

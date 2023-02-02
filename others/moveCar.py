# 汽车从某个坐标开始，沿东南西北某个方向移动
# G: 向前移动一格
# L: 向左转
# R: 向右转
# B: 调头

def move_car():
    orders = input().strip()
    location = [0, 0]
    direction = "N"

    change_dict = {
        ("N", "L"): "W",
        ("N", "R"): "E",
        ("N", "B"): "S",
        ("S", "L"): "E",
        ("S", "R"): "W",
        ("S", "B"): "N",
        ("W", "L"): "S",
        ("W", "R"): "N",
        ("W", "B"): "E",
        ("E", "L"): "N",
        ("E", "R"): "S",
        ("E", "B"): "W",
    }
    move_dict = {
        "N": (0, 1),
        "S": (0, -1),
        "W": (-1, 0),
        "E": (1, 0),
    }

    for x in orders:
        if x in ("L", "R", "B"):
            direction = change_dict[(direction, x)]
        else:
            location[0] += move_dict[direction][0]
            location[1] += move_dict[direction][1]

    return location


def move_car2():
    orders = input().strip()
    location = [0, 0]
    # 东南西北: 0123
    direction = 1

    for x in orders:
        if x == "L":
            direction = (direction + 1) % 4
        elif x == "R":
            direction = (direction - 1) % 4
        elif x == "B":
            direction = (direction + 2) % 4
        else:
            if direction == 0:
                location[0] += 1
            elif direction == 1:
                location[1] += 1
            elif direction == 2:
                location[0] -= 1
            elif direction == 3:
                location[1] -= 1
    return location


if __name__ == '__main__':
    # print(move_car())
    print(move_car2())

import json


tile_type = {
"E": "EMPTY",
"W": "WHIRLPOOL",
"C": "CENTER",
"O": "OBJECTIVE"
}

objective_type = [
"BLUE_MOON",
"YELLOW_WHEEL",
"GREEN_SATURN",
"RED_STAR",
"YELLOW_MOON",
"GREEN_WHEEL",
"RED_SATURN",
"BLUE_STAR",
"GREEN_MOON",
"RED_WHEEL",
"BLUE_SATURN",
"YELLOW_STAR",
"RED_MOON",
"BLUE_WHEEL",
"YELLOW_SATURN",
"GREEN_STAR",
]


def ask_urld_for_tile(urld):
    v = ""
    while v not in ["0", "1"]:
        v = input("%s [1]: " % urld)

        if not v:
            v = "1"

    return v


def ask_info_for_tile(x, y):
    t_type = ""
    o_type = ""
    t_id = "%s" % ((x * 100) + y)
    while t_type not in tile_type:
        t_type = input(
            "Type of Tile at (Col,Line) (%s,%s)"
            "(C, W, E, O) [E]: " % (x,y)
        )
        if not t_type:
            t_type = "E"

        if t_type == "O":
            while o_type not in objective_type:
                o_type = input("What Objective is it :")

        urlds = {}
        for urld in ["UP", "RIGHT", "DOWN", "LEFT"]:
            urlds[urld] = ask_urld_for_tile(urld)

    tile = {
        "id": t_id,
        "coord": {
            "x": x,
            "y": y
        },
        "type": tile_type[t_type],
        "urdl": "%s%s%s%s" % (
            urlds["UP"],
            urlds["RIGHT"],
            urlds["DOWN"],
            urlds["LEFT"]
        )
    }

    if o_type:
        tile["objective_type"] = o_type

    return tile


if __name__ == "__main__":
    tiles = []
    for y in range(1, 9):
        for x in range(1, 9):
            tiles.append(ask_info_for_tile(x, y))

    with open("plates_01.json", "wb") as f:
        f.write(json.dumps(tiles).encode("UTF-8"))

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


def ask_urdl_for_tile(urdl):
    v = ""
    while v not in ["0", "1"]:
        v = input("%s [1]: " % urdl)

        if not v:
            v = "1"

    return v


def calculate_id(x, y):
    return "%s" % ((x * 100) + y)


def ask_info_for_tile(x, y):
    t_type = ""
    o_type = ""
    t_id = calculate_id(x, y)
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

        urdls = {}
        for urdl in ["UP", "RIGHT", "DOWN", "LEFT"]:
            urdls[urdl] = ask_urdl_for_tile(urdl)

    tile = {
        "id": t_id,
        "coord": {
            "x": x,
            "y": y
        },
        "type": tile_type[t_type],
        "urdl": int(
            "%s%s%s%s" % (
                urdls["UP"],
                urdls["RIGHT"],
                urdls["DOWN"],
                urdls["LEFT"]
            )
        )
    }

    if o_type:
        tile["objective_type"] = o_type

    return tile


def is_up_authorized(tile):
    return True if tile["urdl"] >= 1000 else False


def is_left_authorized(tile):
    return True if tile["urdl"] % 2 != 0 else False


def is_right_authorized(tile):
    urdl = tile["urdl"]
    if urdl >= 1000:
        urdl = urdl - 1000

    return True if urdl >= 100 else False


def is_down_authorized(tile):
    urdl = tile["urdl"]
    if urdl >= 1000:
        urdl = urdl - 1000

    if urdl >= 100:
        urdl = urdl - 100

    return True if urdl >= 10 else False


def add_to_collection(tiles, tile):
    if tile["coord"]["y"] == 1:  # First Line cannot go up.
        if is_up_authorized(tile):  # Means UP If authorized
            print("You can't go up on firt line ...")
            return True

    if tile["coord"]["x"] == 1:  # First Row cannot go left.
        if is_left_authorized(tile):  # Not pair, mean Left is authorized
            print("you can't go left on first row ...")
            return True

    if tile["coord"]["x"] == 8:  # Last col should go right
        if not is_right_authorized(tile):
            print("you should go right on last col ...")
            return True

    if tile["coord"]["y"] == 8:  # Last row should go down except on WHIRLPOOL
        if not is_down_authorized(tile) and tile["type"] != tile_type["W"]:
            print("you should go down on last row ...")
            return True

    if tile["coord"]["x"] == 1 and tile['coord']['y'] == 1:
        tiles[tile["coord"]["y"]][tile["coord"]["x"]] = tile
        return False  #it's the first tile

    # Looking at upper tile for cohesion
    if tile["coord"]["y"] != 1:
        if is_down_authorized(
            tiles[tile["coord"]["y"]-1][tile["coord"]["x"]]
        ) != is_up_authorized(tile):
            print("Superior tile is not compatible with this one")
            return True

    # looking left at you
    if tile["coord"]["x"] != 1:
        if is_right_authorized(
            tiles[tile["coord"]["y"]][tile["coord"]["x"]-1]
        ) != is_left_authorized(tile):
            print("Right tile is not compatible with this one")
            return True

    tiles[tile["coord"]["y"]][tile["coord"]["x"]] = tile
    return False  # All is ok


if __name__ == "__main__":
    tiles = {}
    for y in range(1, 9):
        tiles[y] = {}
        for x in range(1, 9):
            b = True
            while b:
                tile = ask_info_for_tile(x, y)
                b = add_to_collection(tiles, tile)

    with open("plates_01.json", "wb") as f:
        f.write(json.dumps(tiles).encode("UTF-8"))

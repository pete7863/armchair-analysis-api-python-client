class Player:
    def __init__(self, dictionary):
        for k, v in dictionary.items():
            setattr(self, "_" + k, v)


class GameStats:
    def __init__(self, dictionary):
        for k, v in dictionary.items():
            setattr(self, "_" + k, v)


class DriveStats:
    def __init__(self, dictionary):
        for k, v in dictionary.items():
            setattr(self, "_" + k, v)


class TeamStats:
    def __init__(self, dictionary):
        for k, v in dictionary.items():
            setattr(self, "_" + k, v)


class OffensiveStats:
    def __init__(self, dictionary):
        for k, v in dictionary.items():
            setattr(self, "_" + k, v)


class DefensiveStats:
    def __init__(self, dictionary):
        for k, v in dictionary.items():
            setattr(self, "_" + k, v)


class KickingStats:
    def __init__(self, dictionary):
        for k, v in dictionary.items():
            setattr(self, "_" + k, v)


class RedZoneStats:
    def __init__(self, dictionary):
        for k, v in dictionary.items():
            setattr(self, "_" + k, v)


class Injury:
    def __init__(self, dictionary):
        for k, v in dictionary.items():
            setattr(self, "_" + k, v)


class Game:
    def __init__(self, dictionary):
        for k, v in dictionary.items():
            setattr(self, "_" + k, v)


class Play:
    def __init__(self, dictionary):
        for k, v in dictionary.items():
            setattr(self, "_" + k, v)


class PlayExpanded:
    def __init__(self, dictionary):
        for k, v in dictionary.items():
            # Expanded plays need special handling since they have more than one layer of depth
            v = parse_key_value(k, v)
            setattr(self, "_" + k, v)


class Pass:
    def __init__(self, dictionary):
        for k, v in dictionary.items():
            setattr(self, "_" + k, v)


class Rush:
    def __init__(self, dictionary):
        for k, v in dictionary.items():
            setattr(self, "_" + k, v)


class Touchdown:
    def __init__(self, dictionary):
        for k, v in dictionary.items():
            setattr(self, "_" + k, v)


class FieldGoalExtraPoint:
    def __init__(self, dictionary):
        for k, v in dictionary.items():
            setattr(self, "_" + k, v)


class Conversion:
    def __init__(self, dictionary):
        for k, v in dictionary.items():
            setattr(self, "_" + k, v)


class Punt:
    def __init__(self, dictionary):
        for k, v in dictionary.items():
            setattr(self, "_" + k, v)


# TODO: determine what this is???
class Chart:
    def __init__(self, dictionary):
        for k, v in dictionary.items():
            setattr(self, "_" + k, v)


class Tackle:
    def __init__(self, dictionary):
        for k, v in dictionary.items():
            setattr(self, "_" + k, v)


class Sack:
    def __init__(self, dictionary):
        for k, v in dictionary.items():
            setattr(self, "_" + k, v)


class Fumble:
    def __init__(self, dictionary):
        for k, v in dictionary.items():
            setattr(self, "_" + k, v)


class Interception:
    def __init__(self, dictionary):
        for k, v in dictionary.items():
            setattr(self, "_" + k, v)


class Block:
    def __init__(self, dictionary):
        for k, v in dictionary.items():
            setattr(self, "_" + k, v)


class Safety:
    def __init__(self, dictionary):
        for k, v in dictionary.items():
            setattr(self, "_" + k, v)


class Penalty:
    def __init__(self, dictionary):
        for k, v in dictionary.items():
            setattr(self, "_" + k, v)


class Kickoff:
    def __init__(self, dictionary):
        for k, v in dictionary.items():
            setattr(self, "_" + k, v)


class OffensiveLine:
    def __init__(self, dictionary):
        for k, v in dictionary.items():
            setattr(self, "_" + k, v)


def parse_key_value(k, v):
    if k == "tck":
        v = parse_optional_value(v, Tackle)
    elif k == "sk":
        v = parse_optional_value(v, Sack)
    elif k == "pen":
        v = parse_optional_value(v, Penalty)
    elif k == "ints":
        v = parse_optional_value(v, Interception)
    elif k == "fum":
        v = parse_optional_value(v, Fumble)
    elif k == "saf":
        v = parse_optional_value(v, Safety)
    elif k == "blk":
        v = parse_optional_value(v, Block)

    # TODO need to handle the play types (Pass, Rush, Punt, Kickoff, Field Goal, Extra Point, Conversion)

    return v


def parse_optional_value(v, class_type):
    if v == 0:
        items = []
    elif isinstance(v, list):
        items = []
        for item in v:
            items.append(class_type(item))
    else:
        items = [class_type(v)]

    return items

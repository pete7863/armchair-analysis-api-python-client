from armchair_analysis_api_python_client import datatypes
from armchair_analysis_api_python_client.endpoints import request


def get_generic(url, class_type, params=None):
    items = []

    r = request.get(url, params=params)

    if 'data' in r.json():
        for item in r.json()['data']:
            items.append(class_type(item))

    return items


def get_blocks(_id):
    url = "http://armchairanalysis.com/api/1.0/player/%s/blocks" % _id

    return get_generic(url, datatypes.Block)


def get_conversions(_id):
    url = "http://armchairanalysis.com/api/1.0/player/%s/conversions" % _id

    return get_generic(url, datatypes.Conversion)


def get_defense_stats(_id):
    url = "http://armchairanalysis.com/api/1.0/player/%s/defense" % _id

    return get_generic(url, datatypes.DefensiveStats)


def get_field_goals_and_extra_points(_id):
    url = "http://armchairanalysis.com/api/1.0/player/%s/fgxps" % _id

    return get_generic(url, datatypes.FieldGoalExtraPoint)


def get_fumbles(_id):
    url = "http://armchairanalysis.com/api/1.0/player/%s/fumbles" % _id

    return get_generic(url, datatypes.Fumble)


def get_injuries(_id):
    url = "http://armchairanalysis.com/api/1.0/player/%s/injuries" % _id

    return get_generic(url, datatypes.Injury)


def get_interceptions(_id):
    url = "http://armchairanalysis.com/api/1.0/player/%s/interceptions" % _id

    return get_generic(url, datatypes.Interception)


def get_kicking_stats(_id):
    url = "http://armchairanalysis.com/api/1.0/player/%s/kickers" % _id

    return get_generic(url, datatypes.KickingStats)


def get_kickoffs(_id):
    url = "http://armchairanalysis.com/api/1.0/player/%s/kickoffs" % _id

    return get_generic(url, datatypes.Kickoff)


def get_offensive_statines(_id):
    url = "http://armchairanalysis.com/api/1.0/player/%s/offense" % _id

    return get_generic(url, datatypes.OffensiveStats)


# TODO: needs pagination
# TODO: if no pagination supplied - return all
def get_passes(_id):
    url = "http://armchairanalysis.com/api/1.0/player/%s/passing" % _id

    return get_generic(url, datatypes.Pass)


def get_penalties(_id):
    url = "http://armchairanalysis.com/api/1.0/player/%s/penalties" % _id

    return get_generic(url, datatypes.Penalty)


def get_player_by_full_name(full_name):
    url = "http://armchairanalysis.com/api/1.0/player/%s" % full_name

    return get_generic(url, datatypes.Player)


def get_player_by_id(_id):
    url = "http://armchairanalysis.com/api/1.0/player/%s" % _id

    return get_generic(url, datatypes.Player)


def get_punts(_id):
    url = "http://armchairanalysis.com/api/1.0/player/%s/punts" % _id

    return get_generic(url, datatypes.Punt)


def get_redzone_stats(_id):
    url = "http://armchairanalysis.com/api/1.0/player/%s/redzone" % _id

    return get_generic(url, datatypes.RedZoneStats)


def get_rushes(_id):
    url = "http://armchairanalysis.com/api/1.0/player/%s/rushing" % _id

    return get_generic(url, datatypes.Rush)


def get_sacks(_id):
    url = "http://armchairanalysis.com/api/1.0/player/%s/sacks" % _id

    return get_generic(url, datatypes.Sack)


def get_safeties(_id):
    url = "http://armchairanalysis.com/api/1.0/player/%s/safeties" % _id

    return get_generic(url, datatypes.Safety)


def get_tackles(_id):
    url = "http://armchairanalysis.com/api/1.0/player/%s/tackles" % _id

    return get_generic(url, datatypes.Tackle)


def get_touchdowns(_id):
    url = "http://armchairanalysis.com/api/1.0/player/%s/touchdowns" % _id

    return get_generic(url, datatypes.Touchdown)

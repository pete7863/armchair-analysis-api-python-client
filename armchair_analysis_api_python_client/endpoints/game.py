from armchair_analysis_api_python_client import datatypes
from armchair_analysis_api_python_client.endpoints import request


def get_generic(url, class_type, params=None):
    items = []

    r = request.get(url, params=params)

    if 'data' in r.json():
        for item in r.json()['data']:
            items.append(class_type(item))

    return items


def get_blocks(gid):
    url = "http://armchairanalysis.com/api/1.0/game/%s/blocks" % gid

    return get_generic(url, datatypes.Block)


def get_conversions(gid):
    url = "http://armchairanalysis.com/api/1.0/game/%s/conversions" % gid

    return get_generic(url, datatypes.Conversion)


def get_defense_stats(gid):
    url = "http://armchairanalysis.com/api/1.0/defense/%s" % gid

    return get_generic(url, datatypes.DefensiveStats)


def get_drive_stats(gid):
    url = "http://armchairanalysis.com/api/1.0/drives/%s" % gid

    return get_generic(url, datatypes.DriveStats)


def get_field_goals_and_extra_points(gid):
    url = "http://armchairanalysis.com/api/1.0/game/%s/fgxps" % gid

    return get_generic(url, datatypes.FieldGoalExtraPoint)


def get_fumbles(gid):
    url = "http://armchairanalysis.com/api/1.0/game/%s/fumbles" % gid

    return get_generic(url, datatypes.Fumble)


def get_game_details(gid):
    url = "http://armchairanalysis.com/api/1.0/game/%s" % gid

    return get_generic(url, datatypes.Game)


def get_injuries(gid):
    url = "http://armchairanalysis.com/api/1.0/game/%s/injuries" % gid

    return get_generic(url, datatypes.Injury)


def get_interceptions(gid):
    url = "http://armchairanalysis.com/api/1.0/game/%s/interceptions" % gid

    return get_generic(url, datatypes.Interception)


def get_kicking_stats(gid):
    url = "http://armchairanalysis.com/api/1.0/kickers/%s" % gid

    return get_generic(url, datatypes.KickingStats)


def get_kickoffs(gid):
    url = "http://armchairanalysis.com/api/1.0/game/%s/kickoffs" % gid

    return get_generic(url, datatypes.Kickoff)


def get_offensive_statines(gid):
    url = "http://armchairanalysis.com/api/1.0/offense/%s" % gid

    return get_generic(url, datatypes.OffensiveStats)


def get_passes(gid):
    url = "http://armchairanalysis.com/api/1.0/game/%s/passing" % gid

    return get_generic(url, datatypes.Pass)


def get_penalties(gid):
    url = "http://armchairanalysis.com/api/1.0/game/%s/penalties" % gid

    return get_generic(url, datatypes.Penalty)


def get_plays(gid):
    url = "http://armchairanalysis.com/api/1.0/plays/%s" % gid

    return get_generic(url, datatypes.Play)


def get_plays_expanded(gid):
    params = {"mode": "expanded"}
    url = "http://armchairanalysis.com/api/1.0/plays/%s" % gid

    return get_generic(url, datatypes.PlayExpanded, params=params)


def get_punts(gid):
    url = "http://armchairanalysis.com/api/1.0/game/%s/punts" % gid

    return get_generic(url, datatypes.Punt)


def get_redzone_stats(gid):
    url = "http://armchairanalysis.com/api/1.0/redzone/%s" % gid

    return get_generic(url, datatypes.RedZoneStats)


def get_rushes(gid):
    url = "http://armchairanalysis.com/api/1.0/game/%s/rushing" % gid

    return get_generic(url, datatypes.Rush)


def get_sacks(gid):
    url = "http://armchairanalysis.com/api/1.0/game/%s/sacks" % gid

    return get_generic(url, datatypes.Sack)


def get_safeties(gid):
    url = "http://armchairanalysis.com/api/1.0/game/%s/safeties" % gid

    return get_generic(url, datatypes.Safety)


def get_tackles(gid):
    url = "http://armchairanalysis.com/api/1.0/game/%s/tackles" % gid

    return get_generic(url, datatypes.Tackle)


def get_team_stats(gid):
    url = "http://armchairanalysis.com/api/1.0/teams/%s" % gid

    return get_generic(url, datatypes.TeamStats)


def get_touchdowns(gid):
    url = "http://armchairanalysis.com/api/1.0/game/%s/touchdowns" % gid

    return get_generic(url, datatypes.Touchdown)

from armchair_analysis_api_python_client import datatypes
from armchair_analysis_api_python_client.endpoints import request


# TODO: for all functions with pagination below, if no pagination is supplied, get all data

def get_generic(url, class_type, params=None):
    items = []

    r = request.get(url, params=params)

    if 'data' in r.json():
        for item in r.json()['data']:
            items.append(class_type(item))

    return items


def get_parameters(count=None, start=None):
    params = {}

    if count is not None:
        params["count"] = count

    if start is not None:
        params["start"] = start
    
    return params


def get_blocks(yr, count=None, start=None):
    params = get_parameters(count, start)
    url = "http://armchairanalysis.com/api/1.0/games/%s/blocks" % yr

    return get_generic(url, datatypes.Block, params=params)


def get_conversions(yr, count=None, start=None):
    params = get_parameters(count, start)
    url = "http://armchairanalysis.com/api/1.0/games/%s/conversions" % yr

    return get_generic(url, datatypes.Conversion, params=params)


def get_defense_stats(yr, count=None, start=None):
    params = get_parameters(count, start)
    url = "http://armchairanalysis.com/api/1.0/defense/%s" % yr

    return get_generic(url, datatypes.DefensiveStats, params=params)


def get_drive_stats(yr, count=None, start=None):
    params = get_parameters(count, start)
    url = "http://armchairanalysis.com/api/1.0/drives/%s" % yr

    return get_generic(url, datatypes.DriveStats, params=params)


def get_field_goals_and_extra_points(yr, count=None, start=None):
    params = get_parameters(count, start)
    url = "http://armchairanalysis.com/api/1.0/games/%s/fgxps" % yr

    return get_generic(url, datatypes.FieldGoalExtraPoint, params=params)


def get_fumbles(yr, count=None, start=None):
    params = get_parameters(count, start)
    url = "http://armchairanalysis.com/api/1.0/games/%s/fumbles" % yr

    return get_generic(url, datatypes.Fumble, params=params)


def get_game_details(count=None, start=None):
    params = get_parameters(count, start)
    url = "http://armchairanalysis.com/api/1.0/games"

    return get_generic(url, datatypes.Game, params=params)


def get_game_details_by_year(yr, count=None, start=None):
    params = get_parameters(count, start)
    url = "http://armchairanalysis.com/api/1.0/games/%s" % yr

    return get_generic(url, datatypes.Game, params=params)


def get_game_details_by_team(team, count=None, start=None):
    params = get_parameters(count, start)
    url = "http://armchairanalysis.com/api/1.0/games/%s" % team

    return get_generic(url, datatypes.Game, params=params)


def get_injuries(yr, count=None, start=None):
    params = get_parameters(count, start)
    url = "http://armchairanalysis.com/api/1.0/games/%s/injuries" % yr

    return get_generic(url, datatypes.Injury, params=params)


def get_interceptions(yr, count=None, start=None):
    params = get_parameters(count, start)
    url = "http://armchairanalysis.com/api/1.0/games/%s/interceptions" % yr

    return get_generic(url, datatypes.Interception, params=params)


def get_kicking_stats(yr, count=None, start=None):
    params = get_parameters(count, start)
    url = "http://armchairanalysis.com/api/1.0/kickers/%s" % yr

    return get_generic(url, datatypes.KickingStats, params=params)


def get_kickoffs(yr, count=None, start=None):
    params = get_parameters(count, start)
    url = "http://armchairanalysis.com/api/1.0/games/%s/kickoffs" % yr

    return get_generic(url, datatypes.Kickoff, params=params)


def get_offensive_statines(yr, count=None, start=None):
    params = get_parameters(count, start)
    url = "http://armchairanalysis.com/api/1.0/offense/%s" % yr

    return get_generic(url, datatypes.OffensiveStats, params=params)


def get_passes(yr, count=None, start=None):
    params = get_parameters(count, start)
    url = "http://armchairanalysis.com/api/1.0/games/%s/passing" % yr

    return get_generic(url, datatypes.Pass, params=params)


def get_penalties(yr, count=None, start=None):
    params = get_parameters(count, start)
    url = "http://armchairanalysis.com/api/1.0/games/%s/penalties" % yr

    return get_generic(url, datatypes.Penalty, params=params)


def get_plays(yr, count=None, start=None):
    params = get_parameters(count, start)
    url = "http://armchairanalysis.com/api/1.0/plays/%s" % yr

    return get_generic(url, datatypes.Play, params=params)


def get_plays_expanded(yr, count=None, start=None):
    params = get_parameters(count, start)
    params["mode"] = "expanded"
    url = "http://armchairanalysis.com/api/1.0/plays/%s" % yr

    return get_generic(url, datatypes.PlayExpanded, params=params)


def get_punts(yr, count=None, start=None):
    params = get_parameters(count, start)
    url = "http://armchairanalysis.com/api/1.0/games/%s/punts" % yr

    return get_generic(url, datatypes.Punt, params=params)


def get_redzone_stats(yr, count=None, start=None):
    params = get_parameters(count, start)
    url = "http://armchairanalysis.com/api/1.0/redzone/%s" % yr

    return get_generic(url, datatypes.RedZoneStats, params=params)


def get_rushes(yr, count=None, start=None):
    params = get_parameters(count, start)
    url = "http://armchairanalysis.com/api/1.0/games/%s/rushing" % yr

    return get_generic(url, datatypes.Rush, params=params)


def get_sacks(yr, count=None, start=None):
    params = get_parameters(count, start)
    url = "http://armchairanalysis.com/api/1.0/games/%s/sacks" % yr

    return get_generic(url, datatypes.Sack, params=params)


def get_safeties(yr, count=None, start=None):
    params = get_parameters(count, start)
    url = "http://armchairanalysis.com/api/1.0/games/%s/safeties" % yr

    return get_generic(url, datatypes.Safety, params=params)


def get_tackles(yr, count=None, start=None):
    params = get_parameters(count, start)
    url = "http://armchairanalysis.com/api/1.0/games/%s/tackles" % yr

    return get_generic(url, datatypes.Tackle, params=params)


def get_team_stats(yr, count=None, start=None):
    params = get_parameters(count, start)
    url = "http://armchairanalysis.com/api/1.0/teams/%s" % yr

    return get_generic(url, datatypes.TeamStats, params=params)


def get_touchdowns(yr, count=None, start=None):
    params = get_parameters(count, start)
    url = "http://armchairanalysis.com/api/1.0/games/%s/touchdowns" % yr

    return get_generic(url, datatypes.Touchdown, params=params)

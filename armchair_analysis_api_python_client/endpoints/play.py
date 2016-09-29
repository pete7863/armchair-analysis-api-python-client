from armchair_analysis_api_python_client import datatypes
from armchair_analysis_api_python_client.endpoints import request


def get_generic(url, class_type, params=None):
    items = []

    r = request.get(url, params=params)

    if 'data' in r.json():
        for item in r.json()['data']:
            items.append(class_type(item))

    return items


def get_block(pid):
    url = "http://armchairanalysis.com/api/1.0/block/%s" % pid

    return get_generic(url, datatypes.Block)


def get_conversion(pid):
    url = "http://armchairanalysis.com/api/1.0/conversion/%s" % pid

    return get_generic(url, datatypes.Conversion)


def get_field_goal_or_extra_point(pid):
    url = "http://armchairanalysis.com/api/1.0/fgxp/%s" % pid

    return get_generic(url, datatypes.FieldGoalExtraPoint)


def get_fumble(pid):
    url = "http://armchairanalysis.com/api/1.0/fumble/%s" % pid

    return get_generic(url, datatypes.Fumble)


def get_interception(pid):
    url = "http://armchairanalysis.com/api/1.0/interception/%s" % pid

    return get_generic(url, datatypes.Interception)


def get_kickoff(pid):
    url = "http://armchairanalysis.com/api/1.0/kickoff/%s" % pid

    return get_generic(url, datatypes.Kickoff)


def get_pass(pid):
    url = "http://armchairanalysis.com/api/1.0/pass/%s" % pid

    return get_generic(url, datatypes.Pass)


def get_penalty(pid):
    url = "http://armchairanalysis.com/api/1.0/penalty" % pid

    return get_generic(url, datatypes.Penalty)


def get_play(pid):
    url = "http://armchairanalysis.com/api/1.0/play/%s" % pid

    return get_generic(url, datatypes.Play)


def get_play_expanded(pid):
    params = {"mode": "expanded"}
    url = "http://armchairanalysis.com/api/1.0/play/%s" % pid

    return get_generic(url, datatypes.PlayExpanded, params=params)


def get_punt(pid):
    url = "http://armchairanalysis.com/api/1.0/punt/%s" % pid

    return get_generic(url, datatypes.Punt)


def get_rush(pid):
    url = "http://armchairanalysis.com/api/1.0/rush/%s" % pid

    return get_generic(url, datatypes.Rush)


def get_sack(pid):
    url = "http://armchairanalysis.com/api/1.0/sack/%s" % pid

    return get_generic(url, datatypes.Sack)


def get_safety(pid):
    url = "http://armchairanalysis.com/api/1.0/safety/%s" % pid

    return get_generic(url, datatypes.Safety)


def get_tackle(pid):
    url = "http://armchairanalysis.com/api/1.0/tackle/%s" % pid

    return get_generic(url, datatypes.Tackle)


def get_touchdown(pid):
    url = "http://armchairanalysis.com/api/1.0/touchdown/%s" % pid

    return get_generic(url, datatypes.Touchdown)

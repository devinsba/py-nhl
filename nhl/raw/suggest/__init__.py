SERVER_ADDRESS = "https://suggest.svc.nhl.com"
PATH_PATTERN = "/svc/suggest/v1/minplayers/{}/99999"


def suggest_players(query):
    url = SERVER_ADDRESS + PATH_PATTERN.format(query)
    return url

from json import loads
from yaml import full_load


with open('config.yaml') as cfg_file:
    cfg = full_load(cfg_file)


class Data:
    name = tuple(cfg['bs_servers']['folders'].keys())[0]
    players_stats_file = (
        cfg['bs_servers']['path'] +
        cfg['bs_servers']['folders'][name] +
        cfg['bs_servers']['players_stats_file']
    )


def update_data(name: str) -> None:
    Data.name = name
    Data.players_stats_file = (
        cfg['bs_servers']['path'] +
        cfg['bs_servers']['folders'][name] +
        cfg['bs_servers']['players_stats_file']
    )


def get_players_stats() -> dict:
    with open(Data.players_stats_file) as stats_file:
        return loads(stats_file.read())


def get_players_top() -> tuple:
    return tuple(map(
        lambda x: x[1],
        sorted(
            get_players_stats().items(),
            key=lambda x: x[1]['kills'],
            reverse=True
        )
    ))

# This file will list all different repositories with dependancies

repos = [
    {
        "name": "endora",
        "type": "module",
        "url": "git@gitlab.com:khaos-serv/endora.git",
        "dep": []
    },
    {
        "name": "amadion",
        "type": "module",
        "url": "git@gitlab.com:khaos-serv/amadion.git",
        "dep": [
            "endora"
        ]
    },
    {
        "name": "importer",
        "type": "module",
        "url": "git@gitlab.com:khaos-serv/importer.git",
        "dep": []
    },
    {
        "name": "loader",
        "type": "module",
        "url": "git@gitlab.com:khaos-serv/loader.git",
        "dep": [
            "importer"
        ]
    },
    {
        "name": "rustoid",
        "type": "project",
        "url": "git@gitlab.com:khaos-serv/fifth-kingdom.git",
        "dep": [
            "endora",
            "amadion",
            "loader"
        ]
    },
]

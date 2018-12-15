# This file will list all different repositories with dependancies

repos = [
    {
        "name": "endora",
        "type": "module",
        "url": "git@github.com:Mazrog/endora.git",
        "dep": []
    },
    {
        "name": "amadion",
        "type": "module",
        "url": "git@gitlab.com:Khabooh/amadion-template.git",
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
        "name": "rustoid",
        "type": "project",
        "url": "git@gitlab.com:khaos-serv/fifth-kingdom.git",
        "dep": [
            "endora",
            "amadion"
        ]
    },
]

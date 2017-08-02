# config.py

import config_default


def merge(defaults, override):
    """Merge default configs and override configs.
    """
    r = {}
    for k, v in defaults.items():
        if k in override:
            if isinstance(v, dict):
                r[k] = merge(v, override[k])
            else:
                r[k] = override[k]
        else:
            r[k] = v

    return r

def toDict(d):
    """Convert dict to Dict.
    """
    D = Dict()
    for (k, v) in d.items():
        D[k] = toDict(v) if isinstance(v, dict) else v
    return D

class Dict(dict):
    """Simple dict but support access like x.y style."""
    def __init__(self, names=(), values=(), **kw):
        super().__init__(**kw)
        for (k, v) in zip(names, values):
            self[k] = v

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value




configs = config_default.configs

try:
    import config_override
    configs = merge(configs, config_override.configs)
except ImportError:
    pass

configs = toDict(configs)


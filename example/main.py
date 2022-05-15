from pyedit import Writable

import config

config = Writable(config)

config.total += 1
config.ran = True

def ew(ew: str) -> "ew":
    print("ew", ew)

config.ew = ew

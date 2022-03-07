try:
    from .dto import *
except ImportError:
    from dto import *

SCRIPTS = {
    'test42': './test42.py',
    'test13': './test13.sh',
}

for script in SCRIPTS:
    SCRIPTS[script] = Script(name=script, command=SCRIPTS[script])
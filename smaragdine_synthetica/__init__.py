from .navigator import lookup, list_versicles, analyse_operation
from . import navigator

import sys
from pathlib import Path
_ENGINE = Path(__file__).parent.parent.parent / 'lang' / 'emerald-tablet-engine'
if str(_ENGINE) not in sys.path:
    sys.path.insert(0, str(_ENGINE))

from emerald_tablet_engine.session import EmeraldSession, SessionState

__version__ = '1.0.0'
__all__ = [
    'EmeraldSession',
    'SessionState',
    'lookup',
    'list_versicles',
    'analyse_operation',
    'navigator',
]

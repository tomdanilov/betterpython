"""Betterpy imports and declarations"""

from __future__ import annotations
from dataclasses import dataclass

from .functions import *
from .struct import *
from .switch import *

import sys
import os

try:
    arguments = sys.argv
except:
    pass

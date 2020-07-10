from __future__ import annotations
from .struct import Statement, Default, Else
from .functions import run

def switch(value: Any, checks: dict) -> None:
    if value in checks:
        run(checks.get(value))
    elif Else in checks:
        run(checks.get(Else))

    if Default in checks:
        run(checks.get(Default))

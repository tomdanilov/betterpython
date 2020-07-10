from __future__ import annotations
from typing import Any

def isequal(a: Any, b: Any) -> bool:
    return a == b

def notequal(a: Any, b: Any) -> bool:
    return a != b

def ismain(name: str) -> bool:
    return name == '__main__'

def run(thing: Any) -> None:
    thing()

def length(value: Any) -> int:
    try:
        return len(value)
    except:
        return len(str(value))

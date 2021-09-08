from random import choice
from typing import Optional


def check_list(lst: list) -> Optional[int]:
    """Get random el or None"""
    if len(lst) == 0:
        return None
    else:
        return choice(lst)

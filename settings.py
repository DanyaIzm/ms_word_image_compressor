from dataclasses import dataclass


@dataclass
class Settings:
    path: str
    should_replace: bool
    postfix: str
    ignore_less_than: int

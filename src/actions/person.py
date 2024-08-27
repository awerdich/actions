from __future__ import annotations
from typing import Collection

class Person:
    def __init__(self, name: str, age: int, *, jobs: Collection[str] | None = None) -> None:
        self.name = name
        self.age = age
        self.jobs = jobs or []

    @property
    def first_name(self) -> str:
        return self.name.split(" ")[0]

    @property
    def last_name(self) -> str:
        name = self.name.split(" ")[-1]
        return name if name != self.first_name else None

    def celebrate_birthday(self) -> None:
        self.age += 1

    def add_job(self, title: str) -> None:
        self.jobs.append(title)
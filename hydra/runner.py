#! /usr/bin/env python3

from abc import ABC, abstractmethod
from typing import Any, Iterable
from hydra.baseline import Baseline


class Runner(ABC):

    @abstractmethod
    def run(self, baseline: Baseline, data: Iterable[Any]) -> int:
        pass

    @abstractmethod
    def get_job(self, uid: int):
        pass

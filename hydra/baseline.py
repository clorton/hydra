#! /usr/bin/env python3

from abc import ABC, abstractmethod
from hydra.instance import Instance
from typing import List


class Baseline(ABC):

    @abstractmethod
    def get_common_files(self) -> List[str]:
        pass

    @abstractmethod
    def get_instance(self, data) -> Instance:
        pass

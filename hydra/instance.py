#! /usr/bin/env python3

from abc import ABC, abstractmethod
from typing import List


class Instance(ABC):

    @abstractmethod
    def get_commandline(self) -> str:
        pass

    @abstractmethod
    def get_instance_files(self) -> List[str]:
        pass

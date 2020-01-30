#! /usr/bin/env python3

from hydra.instance import Instance
from typing import Iterable


class SimulationInstance(Instance):
    def __init__(self, base):
        self.config = "invalid.json"
        return

    # Instance methods
    def get_commandline(self) -> str:
        return f"Eradication -C {self.config} -I . -O output"

    def get_instance_files(self) -> Iterable[str]:
        return [self.config]

    # Custom methods
    def set_run_number(self, run_number: int):
        self.config = f"config_{run_number:02}.json"

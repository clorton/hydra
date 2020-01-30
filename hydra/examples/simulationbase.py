#! /usr/bin/env python3

from hydra.baseline import Baseline
from hydra.instance import Instance
from hydra.examples.simulationinstance import SimulationInstance
from typing import Any, List


class SimulationBase(Baseline):

    def __init__(self):
        self.config = None
        self.campaign = "campaign"
        self.demographics = "demographics.json"
        self.migration = "migration.bin"
        self.weather = None
        self.customizer = None
        return

    @staticmethod
    def add_file(filename: str, files: List[str]) -> None:
        if filename:
            files.append(filename)
        return

    def get_common_files(self) -> List[str]:
        files = []
        self.add_file(self.config, files)
        self.add_file(self.campaign, files)
        self.add_file(self.demographics, files)
        self.add_file(self.migration, files)
        self.add_file(self.weather, files)

        return files

    def get_instance(self, data: Any) -> Instance:
        instance = SimulationInstance(self)
        if self.customizer:
            self.customizer(instance, data)
        return instance

    @property
    def config_filename(self) -> str:
        return self.config

    @config_filename.setter
    def config_filename(self, value: str):
        self.config = value

    @property
    def campaign_filename(self) -> str:
        return self.campaign

    @campaign_filename.setter
    def campaign_filename(self, value: str):
        self.campaign = value

    @property
    def demographics_filename(self) -> str:
        return self.demographics

    @demographics_filename.setter
    def demographics_filename(self, value: str):
        self.demographics = value

    @property
    def migration_filename(self) -> str:
        return self.migration

    @migration_filename.setter
    def migration_filename(self, value: str):
        self.migration = value

    @property
    def weather_filename(self) -> str:
        return self.weather

    @weather_filename.setter
    def weather_filename(self, value: str):
        self.weather = value


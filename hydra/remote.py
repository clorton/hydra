#! /usr/bin/env python3

from typing import Any, Iterable
from hydra.runner import Runner
from hydra.baseline import Baseline
from hydra.instance import Instance


class Remote(Runner):
    def __init__(self):
        self.jobs = []
        return

    def run(self, baseline: Baseline, data: Iterable[Any]) -> int:
        common = baseline.get_common_files()
        print(f"Creating asset collection for common files: {common}")
        count = 0
        for item in data:
            instance = baseline.get_instance(item)
            self.execute(instance)
            count += 1
        return count

    def get_job(self, uid: int):
        return self.jobs[uid]

    def execute(self, instance: Instance):
        commandline = instance.get_commandline()
        files = instance.get_instance_files()
        if len(files):
            print(f"Creating asset collection for bespoke files: {files}")
        print(f"Running instance REMOTELY with commandline '{commandline}'")
        self.jobs.append((commandline, files))
        return

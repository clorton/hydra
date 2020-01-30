#! /usr/bin/env python

from argparse import ArgumentParser

from hydra.examples.simulationbase import SimulationBase
from hydra.examples.simulationinstance import SimulationInstance
from hydra.local import Local
from hydra.remote import Remote


def customize(instance: SimulationInstance, run: int):
    instance.set_run_number(run)
    return


def main(run_remote: bool) -> None:
    baseline = SimulationBase()
    baseline.customizer = customize
    runner = Local() if not run_remote else Remote()
    count = runner.run(baseline, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    print(f"Commissioned {count} jobs:")
    for job in range(count):
        info = runner.get_job(job)
        print(f"Job {job}: '{info[0]}' with files '{info[1]}' and '{baseline.get_common_files()}'")

    return


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("-r", "--remote", action="store_true", help="Remote execution")

    args = parser.parse_args()

    main(args.remote)

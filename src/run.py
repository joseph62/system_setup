#! /usr/bin/env python3
import system_setup

if __name__ == "__main__":
    for installer in system_setup.installers:
        installer()

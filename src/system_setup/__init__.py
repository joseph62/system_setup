import bash

installers = [
        bash.install
        ]

if __name__ == "__main__":
    for installer in installers:
        installer()

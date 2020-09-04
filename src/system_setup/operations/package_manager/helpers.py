def options(*package_managers):
    return dict(package_managers)


def same_package(package, *package_managers):
    return [package_manager(package) for package_manager in package_managers]


def brew(*packages):
    return ("brew", f"brew install {' '.join(packages)}")


def apt(*packages):
    return ("apt", f"sudo apt install {' '.join(packages)}")


def dnf(*packages):
    return ("dnf", f"sudo dnf install {' '.join(packages)}")

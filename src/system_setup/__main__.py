from . import installers, cleaners

for installer in installers:
    installer()

for cleaner in cleaners:
    cleaner()

# System Setup

## Description

The system setup utility configures a Unix-like system with a variety of configuration files and packages to get the system up and running.

## Usage

Run all setups available to system_setup
```
./system_setup
```

Run all setups available and attempt to install packages
```
./system_setup --install-package
```

Run the vim and zsh setups only
```
./system_setup -i vim zsh
```

## Customization 

System Setup does not currently support customizations without code modification. Any additional setup modules must be added to the ```setups``` array to be registered.
#! /usr/bin/env sh

# Always install brew if it does not exist on macos
if [ "${OSTYPE#darwin}" != "$OSTYPE" ] # darwin prefix in OSTYPE
then
    if [ "$(command -v brew)" = "" ] # and brew command not available
    then
        /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
    fi
fi

if [ "$(command -v pip3)" = "" ]
then
    if [ -f /etc/os-release ]
    then
        . /etc/os-release
    fi

    if  [ "$NAME" = "Ubuntu" ]
    then
        sudo apt install python3-pip
    elif  [ "$NAME" = "Fedora Linux" ]
    then
        sudo dnf install python3-pip
    elif [ "${OSTYPE#darwin}" != "$OSTYPE" ] # darwin prefix in OSTYPE
    then
        brew install python3
    else
        echo 'Unable to detect os and install pip. Please install pip to continue'
        exit 1
    fi
fi

if [ "$(command -v ansible-playbook)" = "" ]
then
    sudo -H pip3 install ansible
fi

script_dir="$(dirname $0)"
ansible-galaxy collection install community.general
ansible-playbook -K "$script_dir/main.yml" $@

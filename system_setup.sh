#! /usr/bin/env sh

if ! [ $(command -v pip3) ]; then
    if [ -f /etc/os-release ]; then
        . /etc/os-release
    fi

    if  [[ "$NAME" == "Ubuntu" ]]; then
        sudo apt install python3-pip
    elif  [[ "$NAME" == "Fedora" ]]; then
        sudo dnf install python3-pip
    elif [[ "$OSTYPE" == "darwin"* ]]; then
        if ! [ $(command -v brew) ]; then
            /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
        fi
        brew install python3
    else 
        echo 'Unable to detect os and install pip. Please install pip to continue'
        exit 1
    fi
fi

if ! [ $(command -v ansible-playbook) ]; then
    pip3 install ansible
fi

script_dir=$(dirname $0)
ansible-playbook -K "$script_dir/main.yml"

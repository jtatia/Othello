# Othello Game
Othello is the trading name of a much older board game, Reversi. In both its originally named form and the newer trademark this game has become very popular on computers as much as in board format. Often referred to as a game of abstract strategy, Othello can only be played as a 2 player game. Made up of 8 rows and 8 columns.

#### Table of Contents

1. [Build](#build)
   1. [Prerequisites](#prerequisites)
   2. [Build Command](#build-command)

## Build
### Prerequisites

#### Python

The module is a Django Application and hence requires python installed in the system to launch the sever.

If you want to build the master branch you will need Python 3.0 and above.

#### Django

Pip is a package management system for python. Python has a central package repository from which we can download the python package. It's called Python Package Index (PyPI).

We will use python 3 for Django as recommended by the Django website. Next, we will install pip for python 3 from the Ubuntu repository with this apt command:

```bash
apt-get install python3-pip
```

The installation will add a new binary file called 'pip3'. To make it easier to use pip, I will create a symlink for pip3 to pip:

which pip3

```bash
ln -s /usr/bin/pip3 /usr/bin/pip
```


The pip installation is done. Now we can use the pip command to install python packages. Let's install Django on our server with pip command below:

```bash
pip install django==1.10
```


When the installation is done, check the Django version with the command below:

```bash
django-admin --version
```

#### Git

Install the version control tool [git](https://git-scm.com/) and clone this repository with

```bash
git clone https://github.com/jtatia/Othello.git
```

### Build Command

After you have taken care of the [Prerequisites](#prerequisites)

Execute the following from the command line

```bash
cd Othello
python manage.py runserver
```

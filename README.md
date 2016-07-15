GuruList REST API
=================

Dev Setup
---------

We use [pip](https://pypi.python.org/pypi/pip) to manage our python packages.  If you don't already have pip installed, follow the directions [here](https://pip.pypa.io/en/stable/installing/) to do so.

Once you install pip, it's recommended you use [virtualenv](http://docs.python-guide.org/en/latest/dev/virtualenvs/) to create a separate development evironment to work on this project.  We also use [virtualenvwrapper](http://virtualenvwrapper.readthedocs.io/en/latest/install.html) to help manage these Python environments.

You can download virtualenv and virtualenvwrapper using pip:

```
pip install virtualenv
pip install virtualenvwrapper
```

Then add the following to `.bashrc` to set the location where the virtual environments should live, the location of your development project directories, and the location of the script installed with this package (usually `/usr/local/bin/virtualenvwrapper.sh`):

```
export WORKON_HOME=$HOME/.virtualenvs
export PROJECT_HOME=$HOME/Devel
source /usr/local/bin/virtualenvwrapper.sh
```

`WORKON_HOME` tells virtualenvwrapper where to place your virtual environments
`PROJECT_HOME` tells virtualenvwrapper where to place your project working directories

Then run

```
source ~/.bashrc
```

Create an environment for this project, and activate it

```
mkvirtualenv guru_api
workon guru_api
```

Lastly, install the packages from `dev_requirements.txt` using `pip`

```
pip install -r dev_requirements.txt
```

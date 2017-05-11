# Cheers

### Requirements

* Python 3.5+

### Installation

#### OSX

Install Homebrew

    $ /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

Install Required Packages:

    $ brew install python3


#### Ubuntu/Debian

Install Required Packages:
(python3 is already installed as default on 16.04)

    $ sudo apt-get install python3-dev libpq-dev

### Building the Project

Create Virtual Environment (3.5+)

    $ virtualenv --python=$(which python3) env
    $ sourve env/bin/activate

Clone the repository and:

    $ git clone git@github.com:bahattincinic/cheers.git
    $ cd cheers/

install requirements

    $ pip install -r requirements.txt

copy settings file

    $ cp cheers/settings/dev.py-dist cheers/settings.dev.py
    $ export DJANGO_SETTINGS_MODULE="cheers.settings.dev"

To run the project, Follow the following commands:

    $ python manage.py migrate
    $ python manage.py runserver

if you want to import initial data, You can run the following commands:

    $ python manage.py loaddata cheers/fixtures/supplier.json
    $ python manage.py loaddata cheers/fixtures/criterion.json


## Deployment

```
$ heroku login
$ git push heroku master
```

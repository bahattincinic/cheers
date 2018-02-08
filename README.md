# Cheers

This project covers supply selection and supply chain management, which includes steps from production to delivery and support. All calculations has been bundled into a web application to make examination useful.

Supply selection is an extensive problem with many variables involved. Comparison between suppliers is crucial and needs to be performed with utmost delicacy. In order to perform this comparison one can compare two criterias in each step. AHP is one of the methods which can perform comparison with many criterias involved, can be used to help compare suppliers with many criterias. In this project AHP is used to compare such suppliers with the help of the real world variables obtained from real world institutions. Using this real world data a Python application has been written to simulate comparision between suppliers with many criterias.

**keywords:** supply chain management, decision making with many variables, AHP, python, django ....

## Articles

- https://en.wikipedia.org/wiki/Analytic_hierarchy_process
- https://en.wikipedia.org/wiki/VIKOR_method

## Demo

- Short Video: https://www.youtube.com/watch?v=bJ3PLNz7LLQ
- Long Video: https://www.youtube.com/watch?v=MfXDSCaNHF8


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

## Contributors
- Bahattin Cinic
- Besna Ruken Tarkan

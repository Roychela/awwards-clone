## TITLE
Awwards-clone

## AUTHOR
Roy Chela

## DESCRIPTION
A django clone application of the awwards website

## DATE
04/08/2019

## BEHAVIOUR DRIVEN DEVELOPMENT(BDD)

| Behaviour | Input                     | Output                    |
| --------- | ------------------------- | ------------------------- |
|Navigate to website and view various projects on the homepage|click on visit site  | Redirects you to site |
|Use projects and profiles api|Input api urls on browser|All profiles and/or projects are displayed in json format|
|Navigate to search input| Type in a project|The searched profile is displayed if available|


## SETUP
### Requirements
* Django 1.11 
### Installation
* Fork the data onto your own personal repository.
* Clone Project to your machine
* Activate a virtual environment on terminal: `source virtual/bin/activate`
* Install all the requirements found in requirements file.
* Access the live site using the local host provided

### Prerequisites
1. [Python3.6](https://www.python.org/downloads/)
)
2. [virtualenv](https://virtualenv.pypa.io/en/stable/installation/)
3. [Pip](https://pip.pypa.io/en/stable/installing/)
#### Clone the Repo and rename it to suit your needs.
```bash
git clone https://github.com/Roychela/awwards-clone.git
```
#### Initialize git and add the remote repository
```bash
git init
```
```bash
git remote add origin <your-repository-url>
```

#### Create and activate the virtual environment
```bash
python3.6 -m virtualenv virtual
```

```bash
source virtual/bin/activate
```

#### Setting up environment variables
Create a `.env` file and paste the following filling where appropriate:
```
SECRET_KEY='your_Secret_key'
DEBUG=True
DB_USER='your_database_username'
DB_PASSWORD='your_database_password'
DB_HOST='127.0.0.1'
MODE='dev' 
ALLOWED_HOSTS='.localhost', '.herokuapp.com', '.127.0.0.1'
DISABLE_COLLECTSTATIC=1
```

#### Install dependancies
Install dependencies that will create an environment for the app to run
`pip install -r requirements.txt`

#### Make and run migrations
```bash
python3.6 manage.py makemigrations && python3.6 manage.py migrate
```

#### Run the app
```bash
python3.6 manage.py runserver
```
Open [localhost:8000](http://127.0.0.1:8000/)


## LIVE SITE
Click [Live site](https://roy1awwards.herokuapp.com/) to view the deployed application
## KNOWN BUGS
None

## TECHNOLOGIES
* Python3.6
* Django
* Javascript
* Css
* Scss

## LICENSE
[MIT](https://github.com/Roychela/awwards-clone/blob/master/LICENSE)
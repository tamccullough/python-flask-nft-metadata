## This is a Remix of the following
## Python Metadata API for OpenSea Creatures
found here [OpenSea Metadata API Python](https://github.com/ProjectOpenSea/metadata-api-python)

### About
It is still a;
Very simple sample Python Flask app for serving the ERC721 metadata for a collection of items.

## Requirements

### Python 3

You'll need a machine with Python 3 installed.

### The Google Cloud Storage has been stripped

I have served this through Heroku.

## Setup

Create a virtualenv with Python3

run `pip install --upgrade pip`

run `pip install -r requirements.txt`

## Running and Testing

Run the API with `python app.py` and hit http://localhost:5000/0

depending on the size of your collection

you would change the number after the last / to go to it

http://localhost:5000/1 or http://localhost:5000/56

## Deploying

To deploy on Heroku;
use Heroku CLI
heroku login -i
cd <to this main directory>
heroku create
git init
git add .
git commit -am 'comments go here'
git push heroku master

then hit http://appname.herokuapp.com/0

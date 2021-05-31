## This is a Remix of the following

Python Metadata API for OpenSea Creatures

[OpenSea Metadata API Python](https://github.com/ProjectOpenSea/metadata-api-python)

### About

It is still a...

very simple sample Python Flask app for serving the ERC721 metadata for a collection of items.

But now, it is more generic and it doesn't require any google authorization to save the files.

While OpenSea recommends 350x350px images and you could certainly store a lot more at that size, my images are larger at 2048x2048px and I exceed the soft storage limit of 300MB with 409 images.

So I am in the process of linking to storage with IPFS, and with that, only the .csv file would be stored on this slug.

You could always implement it yourself, and remix this repo.

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

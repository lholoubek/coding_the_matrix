# coding_the_matrix
Working through Coding the Matrix

## Getting started
Note: all assumes python 3
### Set up virtualenv

Create a virtual env

        python3 -m venv env

Then enter the virtual env

        source env/bin/activate

Note: 'env' can be replaced with whatever you want to call it.

We could use a Docker container, but it's easier for now to use a virtual environment.

## Dependencies

### External dependencies
Install everything you need with pip:

        pip install -r requirements.txt

### Install code from the book
The [website for the book](http://resources.codingthematrix.com) has links to download all deps as python files. They are downloaded and stored under `./support`.

This is packaged into a Python module. 
First, cd into /support and then install it:

        python setup.py install

Once installed, support modules are available anywhere inside the virutalenv.

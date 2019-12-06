# Advent of Code - 2019

This is my personal code repo for the 2019 Advent of Code competition.

It is recommended that you have `pyenv` and `pipenv` installed in order to run this repo.

## How the code is organized

Each day is contained within its on Class in the `days` folder.  The individual Days subclass the Base `Class Day`.  

The input data is stored in the folder: `data`

## How to run
A CLI was created to allow easy running of each day.  You can invoke the CLI from the root folder by running:

`pipenv run avocd -d 1 -p 1 -i data`

The flags `-d` and `-p` denote day and puzzle.

## Running Tests

Tests were created for `pytest`.  You can run the tests by invoking:

`pipenv run tests`

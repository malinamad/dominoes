# Domino game
This is a simple command-line implementation of the popular game of Dominoes written in Python.

## Game rules
After the game started, the following interface will be displayed: 

```
======================================================================
Stock pieces: 14 <- pieces pool, 14 is default
Computer pieces: < amount of pieces computer has >

< the highest piece taken from both hands a.k.a. starting piece of domino snake >

Your pieces:
< each of your piece displayed in ordered list >

Status: < current status who's turn now >
```

In order to place a piece (in other words - to move), follow those rules:
1. Place domino to right side of the snake, input a positive number from 1 to 6
2. Place domino to the left side of the snake, input a negative number from -1 to -6
3. To take a piece from the stock use 0

Before placing a domino piece, the piece must have a number 
that will match the end of the snake regardless of the side 

## Installation
To run this program, [Python 3](https://www.python.org/downloads/) version is required to be installed on your computer. 
You can download it from the Python website.

To install the program, simply clone this repository to your local machine:

`git clone https://github.com/malinamad/dominoes.git`

## Run program
To start a game, navigate to the directory where the repository was cloned and run the following command:

`python dominoes.py`

## Made with
* Python

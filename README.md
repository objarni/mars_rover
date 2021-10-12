# Mars Rover tech challenge

This is one of the infinite possible sollutions to Google's [Mars Rover tech challenge](https://code.google.com/archive/p/marsrovertechchallenge/). It was done in Python according the specification below.

## 👨‍🚀 The challenge

A squad of robotic rovers are to be landed by NASA on a plateau on Mars.

This plateau, which is curiously rectangular, must be navigated by the rovers so that their onboard cameras can get a complete view of the surrounding terrain to send back to Earth.

A rover's position is represented by a combination of an x and y coordinates and a letter representing one of the four cardinal compass points. The plateau is divided up into a grid to simplify navigation. An example position might be 0, 0, N, which means the rover is in the bottom left corner and facing North.

In order to control a rover, NASA sends a simple string of letters. The possible letters are 'L', 'R' and 'M'. 'L' and 'R' makes the rover spin 90 degrees left or right respectively, without moving from its current spot. 'M' means move forward one grid point, and maintain the same heading.Assume that the square directly North from (x, y) is (x, y+1).

### Input

The first line of input is the upper-right coordinates of the plateau, the lower-left coordinates are assumed to be 0,0.

The rest of the input is information pertaining to the rovers that have been deployed. Each rover has two lines of input. The first line gives the rover's position, and the second line is a series of instructions telling the rover how to explore the plateau.

The position is made up of two integers and a letter separated by spaces, corresponding to the x and y co-ordinates and the rover's orientation.

Each rover will be finished sequentially, which means that the second rover won't start to move until the first one has finished moving.

### Output

The output for each rover should be its final coordinates and heading.

### Test Input

```
5 5
1 2 N
LMLMLMLMM
3 3 E
MMRMMRMRRM
```

### Expected Output

```
1 3 N
5 1 E
```

## 🚀 Running the code

Assuming you have [Python 3.6+](https://www.python.org/downloads/) in your system, no installation is required. Just clone the repository and you're good to go!

```sh
git clone https://github.com/rlawisch/mars_rover.git
cd mars_rover
python3 mars_rover.py
```

You'll be prompted for a file with the input formatted as above. You can also specify the file as a command line argument:

```sh
python3 mars_rover.py file_name.txt
```

## 🧪 Testing

The tests use the Python built-in `unittest` module and are located in file `test.py`. To run the tests, just run the file as common Python code:
```sh
python3 test.py
```

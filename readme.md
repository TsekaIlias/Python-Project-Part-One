MULTIPLICATION PARSER PROJECT
=

Description
-----------
This project is a Python-based utility designed to generate random alphanumeric 
text (including Greek characters), inject specifically formatted multiplication 
commands (e.g., "ΠΟΛΛΑΠΛΑΣΙΑΣΕ(X, Y)"), and compute the total sum of all 
extracted multiplication operations using regular expressions. 

The project is split into three main parts: core functionality, unit testing, 
and performance benchmarking.

Files Included
--------------
1. erotima1.py
   The core script containing the main logic. 
   - `generate_random_text(n)`: Generates a string of length `n` using Greek 
     letters and numbers.
   - `inject_multiplications(txt, n)`: Randomly inserts `n` multiplication 
     commands into the text.
   - `compute(txt)`: Uses regex to find all "ΠΟΛΛΑΠΛΑΣΙΑΣΕ(X, Y)" instances, 
     multiplies X and Y, and returns the total sum.
   Running this file directly demonstrates a small-scale example (300 
   characters, 3 injections).

2. erotima2.py
   The testing suite using Python's built-in `unittest` framework.
   - Tests manual edge cases (e.g., handling spaces, single vs. double digits, 
     multiple commands in one string).
   - Includes a file-based test that reads from a local file 
     (`test_multiplications1.txt`) and asserts the computed sum matches the 
     expected value (1035105).

3. erotima3.py
   The performance benchmarking script. 
   - Generates a massive text string (1,000,000 characters).
   - Injects a high volume of multiplication commands (100,000).
   - Computes the final sum.
   - Tracks and prints the execution time for each step to evaluate efficiency.

Requirements
------------
- Python 3.x
- No external libraries required. The project relies strictly on Python 
  standard libraries (`random`, `string`, `re`, `unittest`, `time`).
- IMPORTANT: `erotima2.py` requires a file named `test_multiplications1.txt` 
  to be present in the same directory to successfully run `test_file_input`.

How to Run
----------
Open your terminal or command prompt and navigate to the project directory.

To run the basic demonstration:
    python erotima1.py

To run the unit tests:
    python erotima2.py
    # Note: Ensure test_multiplications1.txt is in the same folder.

To run the performance benchmark:
    python erotima3.py

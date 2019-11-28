# DESIGN DOCUMENT

## 1. CONSIDERATIONS

### 1.1 SCOPE 

1. Rules for processing large numbers e.g. two lakh twenty one thousand
2. Addition of Voice Input in-place of Spoken Text to enhance user experience (This would involve use of additional libraries)
3. Performing various arithmetic calculations e.g. four plus four (arithmetic rules adding to rules function)
4. Spellchecker
5. Checking the grammar for vowels e.g. **a umbrella** --->  **an umbrella**
6. Processing uppercase words e.g. THREE, TRIPLE etc.

### 1.2. CONSTRAINTS

1. The only language this library can work with is English
2. The next update would include only basic arithmetic operations (plus, minus, multiply, divide, modulus)


## 2. INSTALLATION

### 2.1 Python Installation Architecture

If you install a Python project using `py -3 setup.py install`, `Distutils`—which is included in the standard library—will copy the files onto your system.

Python packages and modules will land in the Python directory that is loaded when the interpreter starts: under the latest Ubuntu they will wind up in `/usr/local/lib/python/dist-packages/` and under Fedora in `/usr/local/lib/python/sites-packages/`.
Data files defined in a project can land anywhere on the system.
The executable script will land in a bin directory on the system. Depending on the platform, this could be `/usr/local/bin` or in a `bin` directory specific to the Python installation.


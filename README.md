# InHouse-Operations-Pytest

![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/ForrestSwift/inhouse-operations-pytest)
![GitHub commit activity](https://img.shields.io/github/commit-activity/m/ForrestSwift/inhouse-operations-pytest)
![GitHub closed issues](https://img.shields.io/github/issues-closed-raw/ForrestSwift/inhouse-operations-pytest)
![GitHub Workflow Status](https://img.shields.io/github/workflow/status/ForrestSwift/inhouse-operations-pytest/Test?label=Tests)
![GitHub Workflow Status](https://img.shields.io/github/workflow/status/ForrestSwift/inhouse-operations-pytest/Test?label=Build)

### Overview
This repository is for the In House Operations team. The repository is meant to  lint, test and build on push and pull requests..
These are used for sytle checking and linting. These tools help devlopment groups keep their work uniform and also allows for better testing. This repository also includes 
pytest for bubble sort, selection sort and quick sort. Next I will outlinewhat these tools are.

Python Black: Python black is used for style checking. It is considered a safe way to format your code. Python black will format the code without comproimsing it.
This is one of its biggest advantages. Python black is also easily intergrated making it easy to use no matter what IDE you prefer. Black reports formatting errors and also 
automatically fixes them. Black is usually used for formatting code on large group projects becuase in most cases every progrrammer has their personal style which can 
cause confusion on larger projects. Black differs from Flake8 becuase it doesnt force the devlopers to fix their own formatting errors.

Flake8: Flake8 is used for for linting. Linting is when you check the sytanx of your code and make sure it follows the syntax of the language.  Flake8 allows for devlopers to 
check their formatting and see what they must do to change it. This is mainly used to help devlopers who work in teams be more uniform. It also helps devlopers catch errors 
before it is to late. Flake8 checks agains the offical python syntax. The main advantage of using Flake8 is that it has a low percentage of false positives. Flake8 also 
pulls from other linting tools like Pep8, Pychecker, and Pyflakes.
**Build:** The build package is located in the actions tab and can be downloaded from there

### Installation
1. Download package from latest workflow run (located under artifacts) `python-packages`
2. extract .zip to your desired directory
3. open a new shell terminal from that director and run `pip install .\sort_lib-1.0.tar.gz`

### Usage
Once installed, you can import the module into any python file or interpreter
`import int_sort`
or if you only need one algorithm for all your sorting needs:
`from int_sort import bubble`
the int_sort module contains the following sorts
*NOTE: All sorts take exactly one argument, a list*
- `quick` quick sort
- `selection` selection sort
- `bubble` bubble sort'

### Workflow
- The repository is set up to lint, test and build on push and pull requests. 
- Changes made must pass Black and Flake8 linters as well as a couple different unit tests (if sorting algorithms are altered or new ones are added)
- If you are pushing from the command line, a pre-commit check is run and your code will be automatically sent through Black *(this requires you to add your file to the commit again, but it will allow you to forgo the headache of watching failed test in the git-hub actions tab*
---
![Lint](https://github.com/ForrestSwift/inhouse-operations-pytest/actions/workflows/lint.yml/badge.svg) 
Linting with Flake8 and Black (Ubuntu-latest)

![Test](https://github.com/ForrestSwift/inhouse-operations-pytest/actions/workflows/test.yml/badge.svg) 
Unit Tests with Pytest (verified on Windows-latest, MacOs-latest, Ubuntu-Latest)

![Build](https://github.com/ForrestSwift/inhouse-operations-pytest/actions/workflows/build.yml/badge.svg) 
Build package can be found in artifacts (verified on Windows-latest, MacOs-latest, Ubuntu-Latest)




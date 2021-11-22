# InHouse-Operations-Pytest
---
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/ForrestSwift/inhouse-operations-pytest)
![GitHub commit activity](https://img.shields.io/github/commit-activity/m/ForrestSwift/inhouse-operations-pytest)
![GitHub closed issues](https://img.shields.io/github/issues-closed-raw/ForrestSwift/inhouse-operations-pytest)
![GitHub Workflow Status](https://img.shields.io/github/workflow/status/ForrestSwift/inhouse-operations-pytest/Test?label=Tests)
![GitHub Workflow Status](https://img.shields.io/github/workflow/status/ForrestSwift/inhouse-operations-pytest/Test?label=Build)

### Overview
This repository holds three different sorting algorithms for integer arrays.
- bubble, quick and insertion sorts
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
![Lint](https://github.com/ForrestSwift/inhouse-operations-pytest/actions/workflows/lint.yml/badge.svg) Linting with Flake8 and Black (Ubuntu-latest)

![Test](https://github.com/ForrestSwift/inhouse-operations-pytest/actions/workflows/test.yml/badge.svg) Unit Tests with Pytest (verified on Windows-latest, MacOs-latest, Ubuntu-Latest)

![Build](https://github.com/ForrestSwift/inhouse-operations-pytest/actions/workflows/build.yml/badge.svg) Build (verified on Windows-latest, MacOs-latest, Ubuntu-Latest)




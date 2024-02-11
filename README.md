# progpysmt - A SMT-LIB, SyGuS and ProgSynth parser

This repository is a modification of [pySMT: a Python API for SMT](https://github.com/pysmt/pysmt). The goal of this project is to extend the parser in order to accept the [SyGuS](https://sygus-org.github.io/) format and adapts the output to the [ProgSynth](https://github.com/nathanael-fijalkow/ProgSynth/tree/main) format. 

# Usage
In order to use the SMT-LIB parser from the original `pySMT` repository, please follow the instructions on their personal github. 
In order to use the parser on a given file of name `file_name`:
```Python
from  progpysmt.smtlib.parser  import  ProgSmtLibParser
from  progpysmt.pslobject  import  PSLObject

parser = ProgSmtLibParser()
with open(file_name) as f:
	pslobject = parser.get_script(f, file_name)
```
   
This will create a `PSLObject` that contains all the values required to use ProgSynth.

# Installation
## From source
If you install this from source, you will need Python 3.7 or higher.
### Install
You can use pip to install the project.

```shell
pip install progpysmt
```



<div align="center">

# SPARQL VoID to python API

</div>

A package to automatically generate python API package from a SPARQL endpoint VoID description

A CLI to generate python code with dataclasses to materialize an API for a SPARQL endpoint using its VoID description.

```sh
void-to-python gen <void-ttl-file> <directory-to-generate-python-code>
```

Example API for Bgee:

```python
from bgee_api import bgee

# Or:
from bgee_api import Gene, AnatomicalEntity


# 1. Get a specific instance of a class
p1_gene = bgee.orth_gene.get(
    iri="http://P00001", # Mandatory
    id="P0001", # Nice to have
    # fields=["label"], # Later
)
# Or could be something like:
p1_gene = Gene("http://P00001")

# Only retrieve ID, label
print(p1_gene.label)
# Everything is lazy, when the user asks for fields we run a query to get it
# Later we will try to optimize by retrieving many fields if asked at once
print(p1_gene.description)

print(p1_gene.encodes)

# bgee.gene.get(id="P00001")
bgee.species.get(iri="P00001")

# 2. Get the list of instances of a class
gene_list = bgee.gene.list()
# Retrieves a list of Gene object. Only ID is preloaded.
```

> ⚠️ If conflicts in class name, e.g. `orth:Gene` and `up:Gene` we should be smart about it

## 📦️ Installation

This package requires Python >=3.8, simply install it with:

```bash
pip install sparql-void-to-python
```

You can also install directly from the git repository:

```bash
pip install git+https://github.com/TRIPLE-CHIST-ERA/sparql-void-to-python.git
```

## 🪄 Usage

### ⌨️ Use as a command-line interface

You can easily use your package from your terminal after installing `sparql-void-to-python` with pip:

```bash
sparql-void-to-python
```

Get a full rundown of the available options with:

```bash
sparql-void-to-python --help
```

### 🐍 Use with python

 Use this package in python scripts:

 ```python
import sparql_void_to_python

# TODO: add example to use your package
 ```

## 🧑‍💻 Development setup

The final section of the README is for if you want to run the package in development, and get involved by making a code contribution.


### 📥️ Clone

Clone the repository:

```bash
git clone https://github.com/TRIPLE-CHIST-ERA/sparql-void-to-python
cd sparql-void-to-python
```

### 🐣 Install dependencies

Install [Hatch](https://hatch.pypa.io), this will automatically handle virtual environments and make sure all dependencies are installed when you run a script in the project:

```bash
pipx install hatch
```

Or you could install in your favorite virtual env:

```bash
pip install -e ".[test]"

### Develop

Open a shell with virtual env to run your scripts:

```bash
hatch shell
```

### ☑️ Run tests

Make sure the existing tests still work by running the test suite and linting checks. Note that any pull requests to the fairworkflows repository on github will automatically trigger running of the test suite;

```bash
hatch run test
```

To display all logs when debugging:

```bash
hatch run test -s
```



### ♻️ Reset the environment

In case you are facing issues with dependencies not updating properly you can easily reset the virtual environment with:

```bash
hatch env prune
```

Manually trigger installing the dependencies in a local virtual environment:

```bash
hatch -v env create
```

### 🏷️ New release process

The deployment of new releases is done automatically by a GitHub Action workflow when a new release is created on GitHub. To release a new version:

1. Make sure the `PYPI_TOKEN` secret has been defined in the GitHub repository (in Settings > Secrets > Actions). You can get an API token from PyPI at [pypi.org/manage/account](https://pypi.org/manage/account).
2. Increment the `version` number in the `pyproject.toml` file in the root folder of the repository.

    ```bash
    hatch version fix
    ```

3. Create a new release on GitHub, which will automatically trigger the publish workflow, and publish the new release to PyPI.

You can also build and publish from your computer:

```bash
hatch build
hatch publish
```

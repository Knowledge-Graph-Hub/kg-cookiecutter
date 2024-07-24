# kg-cookiecutter
A cookiecutter template for KG generation.

# Getting started

First, install the [cruft](https://github.com/cruft/cruft) package. Cruft enables keeping projects up-to-date with future updates made to this original template.

```
pip install cruft
```

Next, create a project using the `sphintoxetry-cookiecutter` template.
```
cruft create https://github.com/Knowledge-Graph-Hub/kg-cookiecutter
```

This kickstarts an interactive session where you declare the following:
 - `project_name`: Name of the project. [defaults to: Project_X]
 - `project_description`: Description of the project. [defaults to: This is the project description.].
 - `full_name`: Your name [defaults to: Harshad Hegde]
 - `email`: your email [defaults to: hhegde@lbl.gov]
 - `license`: Choose one from [`MIT`, `BSD-3`, `GNU GPL v3.0`, `Apache Software License 2.0`] [defaults to: `MIT`]
 - ⚠️ `github_token_for_doc_deployment`: The github token **variable name** for document deployment using `Sphinx`. [defaults to: `GH_TOKEN`]
 
 > :warning: **Do NOT enter actual token here, this is just the variable name that holds the token value in the project repository's Secrets.**

This will generate the project folder abiding by the template configuration specified by `kg-cookiecutter` in the [`cookiecutter.json`](https://github.com/Knowledge-Graph-Hub/kg-cookiecutter/blob/main/cookiecutter.json) file. 

# What does this do?

The following files and directories are autogenerated in the project:

 - Github wokflows:
   - For code quality checks (`qc.yml`)
   - Documentation deployment (`deploy-docs.yml`)
 - `docs` directory with `Sphinx` configuration files and an `index.rst`file.
 - `project_name` directory
   - Within the `project_name` directory, there are 4 python files:
     - `merge_utils` directory: `kg merge` functionality.
     - `transform_utils` directory: `kg transform` functionality.
       - `atc_transform`: An example for transforming data resources using [`koza`](https://github.com/monarch-initiative/koza).
       - `example_transform`: A basic example for the transform architecture.
       - `ontology_transform`: Sample transform for ontology files.
     - `download.py`: Runs the download of resources from `download.yaml`.
     - `query.py`: SPARQL query functionality.
     - `run.py`: The main driver for CLI commands.
     - `transform.py`: Connects resource to Transform implementation.
 - `templates` directory: Builds of the KG.
 - `tests` directory with a very basic test.
 - `download.yaml`: All configurations for downloading resources
 - `poetry` compatible `pyproject.toml` file containing minimal package requirements.
 - `tox.ini` file containing configuration for:
   -  `coverage-clean`
   -  `lint`
   -  `flake8`
   -  `mypy`
   -  `docstr-coverage`
   -  `pytest`
- `LICENSE` file based on the choice made during setup. 
- `README.md` file containing `project_description` value entered during setup.

# Further setup

## Install `poetry`
Install `poetry` if you haven't already.
```shell
pip install poetry
```
## Install dependencies
```shell
poetry install
```

## Add `poetry-dynamic-versioning` as a plugin
```shell
poetry self add "poetry-dynamic-versioning[plugin]"
```

**Note**: If you are using a Linux system and the above doesn't work giving you the following error `Invalid PEP 440 version: ...`, you could alternatively run:
```
poetry add poetry-dynamic-versioning
```

## Run `tox` to see if the setup works
```
poetry run tox
```

This should run all the bullets mentioned above under the `tox` configuration and ideally you should see the following at the end of the run:
```shell
  coverage-clean: commands succeeded
  lint: commands succeeded
  flake8: commands succeeded
  mypy: commands succeeded
  docstr-coverage: commands succeeded
  py: commands succeeded
  congratulations :)
```

And as the last line says: `congratulations :)`!! Your project is ready to evolve!

# Final test to see everything is wired properly
To download resources:

```shell
kg download
```

By default, this will read from `download.yaml` and save downloaded data to `data/raw`.

To transform downloaded resources:

```shell
kg transform
```

By default, this will run all transforms defined in `transform.py` and save results to `data/transformed`.  Use `-s` option with a transform name to run just one, e.g., `kg transform -s EnvoTransform`.

To build the merged graph:

```shell
kg merge
```

By default, this will merge all inputs defined in `merge.py` and save results to `data/merged`. All three commands should work properly. They basically download transform and merge the `ENVO` and `HP` ontologies and the Anatomical Therapeutic Chemical Classification (`ATC`) dataset.

kg-chat
-------
The cookiecutter also includes [`kg-chat`](https://github.com/Knowledge-Graph-Hub/kg-chat) and all CLI commands run the same:

The first step is to locate the directory containing KGX nodes and edges tsv file (say `data/`).

Then, import the data:

```shell
kg import --data-dir data
```
This imports the nodes and edges tsv file into a `duckdb` database.

You are all set!!!

To query the graph using the interactive chart tool using:

```shell
kg chat --data-dir data
```

or you could launch the app locally:
```shell
kg app --data-dir data
```


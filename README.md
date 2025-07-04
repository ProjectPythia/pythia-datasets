| CI          | [![GitHub Workflow Status][github-ci-badge]][github-ci-link] [![GitHub Workflow Status][pre-commit-badge]][pre-commit-link] [![Code Coverage Status][codecov-badge]][codecov-link] |
| :---------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: |
| **Docs**    |                                                                   [![Documentation Status][rtd-badge]][rtd-link]                                                                   |
| **Package** |                                                        [![Conda][conda-badge]][conda-link] [![PyPI][pypi-badge]][pypi-link]                                                        |
| **License** |                                                                       [![License][license-badge]][repo-link]                                                                       |

# pythia-datasets

Data repository for with sample data for the [Pythia Foundations](https://foundations.projectpythia.org) book.

## Sample data sets

These files are used as sample data in [Pythia Foundations](https://foundations.projectpythia.org) and are downloaded by `pythia_datasets` package:

- `NARR_19930313_0000.nc`
- `enso_data.csv`
- `jan-17-co-asos.txt.xz`
- `CESM2_sst_data.nc`
- `CESM2_grid_variables.nc`
- `daymet_v4_precip_sept_2013.nc`

## Adding new datasets

The scope of this data collection is to serve examples for [Pythia Foundations](https://foundations.projectpythia.org).
If you are adding new content to Foundations that requires a new dataset file, please follow these steps:

1. Add the dataset file to the `data/` directory
2. From the command line, run `python make_registry.py` script to update the registry file residing in `pythia_datasets/registry.txt`
3. Commit and push your changes to GitHub

## Using datasets in notebooks and/or scripts

- Ensure the `pythia_datasets` package is installed in your environment

  ```bash
  python -m pip install pythia-datasets

  # or

  python -m pip install git+https://github.com/ProjectPythia/pythia-datasets
  ```

- Import `DATASETS` and inspect the registry to find out which datasets are available

  ```python
  In [1]: from pythia_datasets import DATASETS

  In [2]: DATASETS.registry_files
  Out[2]: ['jan-17-co-asos.txt.xz', 'NARR_19930313_0000.nc']
  ```

- To fetch a data file of interest, use the `.fetch` method and provide the filename of the data file. This will

  - download and cache the file if it doesn't exist already.
  - retrieve and return the local path

  ```python
  In [4]: filepath = DATASETS.fetch('jan-17-co-asos.txt.xz')

  In [5]: filepath
  Out[5]: '/Users/abanihi/Library/Caches/pythia-datasets/jan-17-co-asos.txt.xz'
  ```

- Once you have access to the local filepath, you can then use it to load your dataset into pandas or xarray or your package of choice:

  ```python
  In [6]: df = pd.read_csv(filepath)
  ```

## Changing the default data cache location

The default cache location (where the data are saved on your local system) is dependent on the operating system. You can use the `locate()` method to identify it:

```python
from pythia_datasets import locate

locate()
```

The location can be overwritten by the `PYTHIA_DATASETS_DIR` environment
variable to the desired destination.

[github-ci-badge]: https://github.com/ProjectPythia/pythia-datasets/actions/workflows/ci.yaml/badge.svg
[pre-commit-badge]: https://results.pre-commit.ci/badge/github/ProjectPythia/pythia-datasets/main.svg
[github-ci-link]: https://github.com/ProjectPythia/pythia-datasets/actions?query=workflow%3ACI
[pre-commit-link]: https://results.pre-commit.ci/latest/github/ProjectPythia/pythia-datasets/main
[codecov-badge]: https://img.shields.io/codecov/c/github/ProjectPythia/pythia-datasets.svg?logo=codecov
[codecov-link]: https://codecov.io/gh/ProjectPythia/pythia-datasets
[rtd-badge]: https://img.shields.io/readthedocs/pythia-datasets/latest.svg?style=for-the-badge
[rtd-link]: https://pythia-datasets.readthedocs.io/en/latest/?badge=latest
[pypi-badge]: https://img.shields.io/pypi/v/pythia-datasets?logo=pypi&style=for-the-badge
[pypi-link]: https://pypi.org/project/pythia-datasets
[conda-badge]: https://img.shields.io/conda/vn/conda-forge/pythia-datasets?logo=anaconda&style=for-the-badge
[conda-link]: https://anaconda.org/conda-forge/pythia-datasets
[license-badge]: https://img.shields.io/github/license/ProjectPythia/pythia-datasets?style=for-the-badge
[repo-link]: https://github.com/ProjectPythia/pythia-datasets

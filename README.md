# pythia-datasets

| CI          | [![GitHub Workflow Status][github-ci-badge]][github-ci-link] [![GitHub Workflow Status][github-lint-badge]][github-lint-link] [![Code Coverage Status][codecov-badge]][codecov-link] |
| :---------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: |
| **Docs**    |                                                                    [![Documentation Status][rtd-badge]][rtd-link]                                                                    |
| **Package** |                                                         [![Conda][conda-badge]][conda-link] [![PyPI][pypi-badge]][pypi-link]                                                         |
| **License** |                                                                        [![License][license-badge]][repo-link]                                                                        |

Data repository for Project Pythia examples/notebooks

## Sample data sets

These files are used as sample data in Pythia Project examples/notebooks and are downloaded by `pythia_datasets` package:

- `NARR_19930313_0000.nc`
- `enso_data.csv`
- `jan-17-co-asos.txt.xz`

### Adding new datasets

To add a new dataset file, please follow these steps:

1. Add the dataset file to the `data/` directory
2. From the command line, run `python make_registry.py` script to update the registry file residing in `pythia_datasets/registry.txt`
3. Commit and push your changes to GitHub

[github-ci-badge]: https://img.shields.io/github/workflow/status/ProjectPythia/pythia-datasets/CI?label=CI&logo=github&style=for-the-badge
[github-lint-badge]: https://img.shields.io/github/workflow/status/ProjectPythia/pythia-datasets/linting?label=linting&logo=github&style=for-the-badge
[github-ci-link]: https://github.com/ProjectPythia/pythia-datasets/actions?query=workflow%3ACI
[github-lint-link]: https://github.com/ProjectPythia/pythia-datasets/actions?query=workflow%3Alinting
[codecov-badge]: https://img.shields.io/codecov/c/github/ProjectPythia/pythia-datasets.svg?logo=codecov&style=for-the-badge
[codecov-link]: https://codecov.io/gh/ProjectPythia/pythia-datasets
[rtd-badge]: https://img.shields.io/readthedocs/pythia-datasets/latest.svg?style=for-the-badge
[rtd-link]: https://pythia-datasets.readthedocs.io/en/latest/?badge=latest
[pypi-badge]: https://img.shields.io/pypi/v/pythia-datasets?logo=pypi&style=for-the-badge
[pypi-link]: https://pypi.org/project/pythia-datasets
[conda-badge]: https://img.shields.io/conda/vn/conda-forge/pythia-datasets?logo=anaconda&style=for-the-badge
[conda-link]: https://anaconda.org/conda-forge/pythia-datasets
[license-badge]: https://img.shields.io/github/license/ProjectPythia/pythia-datasets?style=for-the-badge
[repo-link]: https://github.com/ProjectPythia/pythia-datasets

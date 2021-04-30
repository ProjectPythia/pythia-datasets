import pathlib

from pythia_datasets import DATASETS, locate


def test_registry():
    files = DATASETS.registry_files
    assert len(files) > 0


def test_locate():
    p = locate()
    assert 'pythia-datasets' in p
    assert pathlib.Path(p).exists

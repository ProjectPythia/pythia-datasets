from pythia_datasets import DATASETS


def test_registry():
    files = DATASETS.registry_files
    assert len(files) > 0

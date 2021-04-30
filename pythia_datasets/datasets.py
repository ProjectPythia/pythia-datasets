import pkg_resources
import pooch

DATASETS = pooch.create(
    path=pooch.os_cache('pythia-datasets'),
    base_url='https://github.com/ProjectPythia/pythia-datasets/raw/main/data/',
    env='PYTHIA_DATASETS_DIR',
)

with pkg_resources.resource_stream('pythia_datasets', 'registry.txt') as registry_file:
    DATASETS.load_registry(registry_file)

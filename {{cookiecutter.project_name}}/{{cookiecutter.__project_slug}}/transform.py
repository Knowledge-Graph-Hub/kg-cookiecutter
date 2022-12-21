import logging
from typing import List

from {{cookiecutter.__project_slug}}.transform_utils.ontology import OntologyTransform
from {{cookiecutter.__project_slug}}.transform_utils.ontology.ontology_transform import ONTOLOGIES

DATA_SOURCES = {
    # "MondoTransform": OntologyTransform,
    # "ChebiTransform": OntologyTransform,
    "HPOTransform": OntologyTransform,
    "ENVOTransform": OntologyTransform,
    # "GOTransform": OntologyTransform,
    # "OGMSTransform": OntologyTransform,
    # "DrugCentralTransform": DrugCentralTransform,
    # "OrphanetTransform": OrphanetTransform,
    # "OMIMTransform": OMIMTransform,
    # "ReactomeTransform": ReactomeTransform,
    # "GOCAMTransform": GOCAMTransform,
    # "TCRDTransform": TCRDTransform,
    # "ProteinAtlasTransform": ProteinAtlasTransform,
    # "STRINGTransform": STRINGTransform,
    # "ATCTransform": ATCTransform,
}


def transform(input_dir: str, output_dir: str, sources: List[str] = None) -> None:
    """Call scripts in kg_idg/transform/[source name]/ to
    transform each source into a graph format that
    KGX can ingest directly, in either TSV or JSON format:
    https://github.com/biolink/kgx/blob/master/data-preparation.md

    Args:
        input_dir: A string pointing to the directory to import data from.
        output_dir: A string pointing to the directory to output data to.
        sources: A list of sources to transform.

    Returns:
        None.

    """
    if not sources:
        # run all sources
        sources = list(DATA_SOURCES.keys())

    for source in sources:
        if source in DATA_SOURCES:
            logging.info(f"Parsing {source}")
            t = DATA_SOURCES[source](input_dir, output_dir)
            if source in ONTOLOGIES.keys():
                t.run(ONTOLOGIES[source])
            else:
                t.run()

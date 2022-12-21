"""Transform module."""
import logging
from typing import List, Optional

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


def transform(
    input_dir: Optional[Path], output_dir: Optional[Path], sources: List[str] = None
) -> None:
    """Transform based on resource and class declared in DATA_SOURCES.
    
    Call scripts in {{cookiecutter.__project_slug}}/transform/[source name]/ to
    transform each source into a graph format that
    KGX can ingest directly, in either TSV or JSON format:
    https://github.com/biolink/kgx/blob/master/data-preparation.md

    :param input_dir: A string pointing to the directory to import data from.
    :param output_dir: A string pointing to the directory to output data to.
    :param sources: A list of sources to transform.
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

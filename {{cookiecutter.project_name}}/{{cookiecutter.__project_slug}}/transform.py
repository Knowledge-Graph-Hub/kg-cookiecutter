from {{cookiecutter.__project_slug}}.transform_utils.ontology import OntologyTransform

DATA_SOURCES = {
    "MondoTransform": OntologyTransform,
    "ChebiTransform": OntologyTransform,
    "HPOTransform": OntologyTransform,
    "GOTransform": OntologyTransform,
    "OGMSTransform": OntologyTransform,
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
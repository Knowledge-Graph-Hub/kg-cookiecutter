"""Ontology transform module."""
from pathlib import Path
from typing import Optional, Union

# from kgx.transformer import Transformer
from kgx.cli.cli_utils import transform

from ..transform import Transform

ONTOLOGIES = {
    "HpTransform": "hp.json",
    # 'GoTransform': 'go-plus.json',
    # 'NCBITransform':  'ncbitaxon.json',
    # 'ChebiTransform': 'chebi.json',
    "EnvoTransform": "envo.json",
    # 'GoTransform': 'go.json'
}


class OntologyTransform(Transform):
    """OntologyTransform parses an Obograph JSON form of an Ontology into nodes nad edges."""

    def __init__(self, input_dir: Optional[Path] = None, output_dir: Optional[Path] = None):
        """Instatiate object."""
        source_name = "ontologies"
        super().__init__(source_name, input_dir, output_dir)

    def run(self, data_file: Union[Optional[Path], Optional[str]] = None) -> None:
        """Transform an ontology.

        :param data_file: data file to parse
        :return: None.
        """
        if data_file:
            k = str(data_file).split(".")[0]
            data_file = self.input_base_dir / data_file
            self.parse(k, data_file, k)
        else:
            # load all ontologies
            for k in ONTOLOGIES.keys():
                data_file = self.input_base_dir / ONTOLOGIES[k]
                self.parse(k, data_file, k)

    def parse(self, name: str, data_file: Optional[Path], source: str) -> None:
        """Process the data_file.

        :param name: Name of the ontology.
        :param data_file: data file to parse.
        :param source: Source name.
        :return: None.
        """
        transform(
            inputs=[data_file],
            input_format="obojson",
            output=self.output_dir / name,
            output_format="tsv",
        )

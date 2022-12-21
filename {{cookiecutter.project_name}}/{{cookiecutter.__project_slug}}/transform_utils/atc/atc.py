"""ATC transfer utility module."""
import gzip
import os
import shutil
from typing import Optional
from pathlib import Path

from koza.cli_runner import transform_source  # type: ignore

from {{cookiecutter.__project_slug}}.transform_utils.transform import Transform

"""
ATC is the Anatomical Therapeutic Chemical Classification.
We use it to categorize relationships among classes of drugs,
with codes provided by DrugCentral.
See details on source files here:
https://bioportal.bioontology.org/ontologies/ATC/?p=summary
"""

ATC_SOURCES = {
    "ATC_DATA": "atc.csv.gz",
}

ATC_CONFIGS = {
    "ATC_DATA": "atc-classes.yaml",
}

TRANSLATION_TABLE = "./{{cookiecutter.__project_slug}}/transform_utils/translation_table.yaml"


class ATCTransform(Transform):
    """This transform ingests the ATC CSV file.
    It is transformed to KGX-format node and edge lists.
    """

    def __init__(self, input_dir: Optional[Path] = None, output_dir: Optional[Path] = None) -> None:
        """Instantiation of a transform.

        :param input_dir: Path to input directory, defaults to None
        :param output_dir: Path to output directory, defaults to None
        """
        source_name = "atc"
        super().__init__(source_name, input_dir, output_dir)

    def run(self, atc_file: Optional[Path] = None) -> None:  # type: ignore
        """
        Set up the ATC for Koza and call the parse function.
        """
        if atc_file:
            for source in [atc_file]:
                k = str(source).split(".")[0]
                data_file = self.input_bas_dir / source
                self.parse(k, data_file, k)
        else:
            for k in ATC_SOURCES.keys():
                name = ATC_SOURCES[k]
                data_file = self.input_base_dir / name
                self.parse(name, data_file, k)

    def parse(self, name: str, data_file: str, source: str) -> None:
        """Transform ATC file with Koza.Need to decompress it first.

        :param name: Name of the resource
        :param data_file: Data file of resource.
        :param source: _description_
        :raises ValueError: _description_
        """
        print(f"Parsing {data_file}")
        config = Path(__file__).resolve().parent / ATC_CONFIGS[source]
        output = self.output_dir

        # Decompress
        outname = name[:-3]
        outpath = self.input_base_dir / outname
        with gzip.open(data_file, "rb") as data_file_gz:
            with open(outpath, "wb") as data_file_new:
                shutil.copyfileobj(data_file_gz, data_file_new)

        # If source is unknown then we aren't going to guess
        if source not in ATC_CONFIGS:
            raise ValueError(f"Source file {source} not recognized - not transforming.")
        else:
            transform_source(
                source=config,
                output_dir=output,
                output_format="tsv",
                global_table=TRANSLATION_TABLE,
                local_table=None,
            )

        os.remove(outpath)
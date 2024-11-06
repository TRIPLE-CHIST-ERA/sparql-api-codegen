from dataclasses import dataclass
from typing import Optional


@dataclass
class Bgee:
    id: str
    # greet: str = field(default_factory=lambda: os.environ.get("GREET", "world"))
    # many_times: int = field(default_factory=lambda: int(os.environ.get("MANY_TIMES", "2")))


@dataclass
class Entity:
    iri: str
    sparql_endpoint: str = "https://www.bgee.org/sparql/"

    # TODO: add functions to get the data from the SPARQL endpoint


@dataclass
class AnatomicalEntity(Entity):
    description: str
    expressed: Optional["Gene"]

    @property
    def description(self):
        # TODO: SPARQL query to retrieve the description
        return self._description

    # @description.setter
    # def description(self, value):
    #     self._description = value

    @property
    def expressed(self):
        return self._expressed

    # @expressed.setter
    # def expressed(self, value):
    #     self._expressed = value


@dataclass
class Gene(Entity):
    isExpressedIn: Optional[AnatomicalEntity]
    xrefUniprot: str


# TODO: how to handle circular references?

if __name__ == "__main__":
    anat = AnatomicalEntity(iri="http://purl.obolibrary.org/obo/UBERON_0002107", description="brain", expressed=None)
    gene = Gene(iri="http://purl.uniprot.org/uniprot/P12345", isExpressedIn=anat, xrefUniprot="P123")
    print(anat, gene)

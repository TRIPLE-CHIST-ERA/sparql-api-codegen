from dataclasses import dataclass, field, asdict



@dataclass
class Bgee:
    id: str
    # greet: str = field(default_factory=lambda: os.environ.get("GREET", "world"))
    # many_times: int = field(default_factory=lambda: int(os.environ.get("MANY_TIMES", "2")))


@dataclass
class Entity:
    iri: str

    # TODO: add functions to get the data from the SPARQL endpoint


@dataclass
class AnatomicalEntity(Entity):
    description: str
    # expressed: Gene


@dataclass
class Gene(Entity):
    isExpressedIn: AnatomicalEntity
    xrefUniprot: str


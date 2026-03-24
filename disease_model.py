# Auto generated from schema.yaml by pythongen.py version: 0.0.1
# Generation date: 2026-03-24T09:38:56
# Schema: disease-phenotype-model
#
# id: https://w3id.org/my-github/disease-model
# description:
# license: https://creativecommons.org/publicdomain/zero/1.0/

import dataclasses
import re
from dataclasses import dataclass
from datetime import (
    date,
    datetime,
    time
)
from typing import (
    Any,
    ClassVar,
    Dict,
    List,
    Optional,
    Union
)

from jsonasobj2 import (
    JsonObj,
    as_dict
)
from linkml_runtime.linkml_model.meta import (
    EnumDefinition,
    PermissibleValue,
    PvFormulaOptions
)
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from linkml_runtime.utils.formatutils import (
    camelcase,
    sfx,
    underscore
)
from linkml_runtime.utils.metamodelcore import (
    bnode,
    empty_dict,
    empty_list
)
from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.yamlutils import (
    YAMLRoot,
    extended_float,
    extended_int,
    extended_str
)
from rdflib import (
    Namespace,
    URIRef
)

from linkml_runtime.linkml_model.types import String

metamodel_version = "1.7.0"
version = None

# Namespaces
HPO = CurieNamespace('hpo', 'http://purl.obolibrary.org/obo/HP_')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
MONDO = CurieNamespace('mondo', 'http://purl.obolibrary.org/obo/MONDO_')
DEFAULT_ = CurieNamespace('', 'https://w3id.org/my-github/disease-model/')


# Types

# Class references
class DiseaseId(extended_str):
    pass


@dataclass(repr=False)
class Disease(YAMLRoot):
    """
    表示一種疾病實體
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://w3id.org/my-github/disease-model/Disease")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "Disease"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/my-github/disease-model/Disease")

    id: Union[str, DiseaseId] = None
    name: str = None
    symptoms: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DiseaseId):
            self.id = DiseaseId(self.id)

        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if not isinstance(self.symptoms, list):
            self.symptoms = [self.symptoms] if self.symptoms is not None else []
        self.symptoms = [v if isinstance(v, str) else str(v) for v in self.symptoms]

        super().__post_init__(**kwargs)


# Enumerations


# Slots
class slots:
    pass

slots.disease__id = Slot(uri=DEFAULT_.id, name="disease__id", curie=DEFAULT_.curie('id'),
                   model_uri=DEFAULT_.disease__id, domain=None, range=URIRef)

slots.disease__name = Slot(uri=DEFAULT_.name, name="disease__name", curie=DEFAULT_.curie('name'),
                   model_uri=DEFAULT_.disease__name, domain=None, range=str)

slots.disease__symptoms = Slot(uri=DEFAULT_.symptoms, name="disease__symptoms", curie=DEFAULT_.curie('symptoms'),
                   model_uri=DEFAULT_.disease__symptoms, domain=None, range=Optional[Union[str, list[str]]])


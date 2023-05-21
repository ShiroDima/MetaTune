from utils.module_utils import get_entities
from tune_regressor.svr import *
from tune_regressor.decision_tree_regressor import *
from tune_regressor.GaussianNB import *
from typing import Iterable, Tuple, Dict, Generator

__all__: Iterable[str] = [
    "tune_regressor.svr",
    "tune_regressor.decision_tree_regressor",
    "tune_regressor.GaussianNB",
]

tuning_entities: Iterable[Iterable[Tuple[str, object]]] = list(map(get_entities, __all__))
tuning_entities: Generator = (i for i in sum(tuning_entities, []))
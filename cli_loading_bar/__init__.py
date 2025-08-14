from .Loading import *  # importa tutte le classi, funzioni, variabili definite in Loading.py
import importlib.metadata
# opzionale: limita ciò che viene esposto con __all__
# Se non lo metti, verrà esposto tutto ciò che non inizia con "_"
from .Loading import __all__ as loading_all
__all__ = loading_all

__version__ = importlib.metadata.version("cli_loading_bar")

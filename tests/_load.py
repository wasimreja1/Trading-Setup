"""Load a script from a skill folder (the folder names have hyphens)."""

import importlib.util
import os

# The fixtures and expected numbers are the US (NYSE) example, so the regression
# suite runs against the US market regardless of the live default (NSE).
os.environ["TRADER_MARKET"] = "US"

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FIX = os.path.join(ROOT, "tests", "fixtures")


def load(folder, name):
    path = os.path.join(ROOT, folder, name + ".py")
    spec = importlib.util.spec_from_file_location("trader_" + name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod

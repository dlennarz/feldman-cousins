from __future__ import annotations

import importlib.metadata

import feldman_cousins as m


def test_version():
    assert importlib.metadata.version("feldman_cousins") == m.__version__

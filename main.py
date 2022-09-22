import pytest


def always_returns_true():
    print("Is this working?")
    return True


def test_always_returns_true():
    assert always_returns_true()

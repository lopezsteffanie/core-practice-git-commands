import pytest


def always_returns_true():
    print("Hi Stevie!")
    return False


def test_always_returns_true():
    assert always_returns_true()

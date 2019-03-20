import pytest
import asyncio
import random
import sys
from sleepsort import sleepsort


@pytest.fixture
def random_integers(maxlen=10, maxint=5):
    length = random.randint(1, maxlen)
    return [random.randint(0, maxint) for i in range(length)]


def test_sleepsort(capsys, random_integers):
    asyncio.run(sleepsort(random_integers))
    actual = [int(i)
              for i in capsys.readouterr().out.split(" ")
              if len(i.strip())]
    assert actual == sorted(random_integers)

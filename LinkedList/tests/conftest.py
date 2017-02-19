import pytest

from LinkedList import LinkedList

@pytest.fixture
def LinkedList(request):
    return LinkedList()
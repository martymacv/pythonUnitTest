import pytest

from codeExample import Receipt, Item


@pytest.fixture
def receipt(request):
    return Receipt(*request.param)


@pytest.fixture
def item(request):
    return Item(*request.param)

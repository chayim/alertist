from alertist import Alertist
from alertist.targets import Pushover
from alertist.conf import Config
import pytest
import httpx


def test_alert(mocker):
    p = Pushover
    a = Alertist(p)
    with pytest.raises(ValueError):
        a.alert("Hello, World!")

    mocker.patch("httpx.post")
    c = Config()
    c.PUSHOVER_USER = "chayim"
    c.PUSHOVER_API_TOKEN = "token"
    a.alert("Hello, World!")
    httpx.post.assert_called_once()


@pytest.mark.asyncio
async def test_async_alert(mocker):
    try:
        del Config().PUSHOVER_USER
        del Config().PUSHOVER_API_TOKEN
    except AttributeError:
        pass

    p = Pushover
    a = Alertist(p)
    with pytest.raises(ValueError):
        await a.aalert("Hello, World!")

    mocker.patch("httpx.AsyncClient.post")
    c = Config()
    c.PUSHOVER_USER = "chayim"
    c.PUSHOVER_API_TOKEN = "token"
    await a.aalert("Hello, World!")
    httpx.AsyncClient.post.assert_called_once()

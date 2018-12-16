import pytest
from app import create_app
from config import TestConfig


@pytest.yield_fixture
def app():
    my_app = create_app(TestConfig)
    yield my_app


@pytest.fixture
def test_cli(loop, app, test_client):
    return loop.run_until_complete(test_client(app))


async def test_users(test_cli):
    resp = await test_cli.get('/users')
    assert resp.status == 200
    assert (await resp.json()) == {"hello": "world"}

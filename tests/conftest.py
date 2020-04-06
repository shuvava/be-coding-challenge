# -*- coding: utf-8 -*-
import os
from sys import path

import pytest

path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from family_tree.app import create_app


@pytest.fixture(scope='module')
def test_client():
    flask_app = create_app()

    testing_client = flask_app.test_client()

    ctx = flask_app.app_context()
    ctx.push()

    yield testing_client

    ctx.pop()

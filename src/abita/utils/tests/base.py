from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer

import unittest


class AbitaUtilsLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)


FIXTURE = AbitaUtilsLayer()
INTEGRATION_TESTING = IntegrationTesting(
    bases=(FIXTURE,), name="AbitaUtilsLayer:Integration")
FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(FIXTURE,), name="AbitaUtilsLayer:Functional")


class IntegrationTestCase(unittest.TestCase):
    """Base class for integration tests."""

    layer = INTEGRATION_TESTING


class FunctionalTestCase(unittest.TestCase):
    """Base class for functional tests."""

    layer = FUNCTIONAL_TESTING

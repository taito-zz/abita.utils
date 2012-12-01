from Products.CMFCore.utils import getToolByName
from abita.utils.tests.base import IntegrationTestCase


class TestCase(IntegrationTestCase):
    """TestCase for Plone setup."""

    def setUp(self):
        self.portal = self.layer['portal']

    def test_install_packages__one_package(self):
        installer = getToolByName(self.portal, 'portal_quickinstaller')
        installer.uninstallProducts(['plone.app.jquery'])
        self.assertFalse(installer.isProductInstalled('plone.app.jquery'))

        from abita.utils.utils import install_packages
        install_packages(self.portal, 'plone.app.jquery')

        self.assertTrue(installer.isProductInstalled('plone.app.jquery'))

    def test_install_packages__two_packages(self):
        installer = getToolByName(self.portal, 'portal_quickinstaller')
        installer.uninstallProducts(['plone.app.jquery', 'plone.app.collection'])
        self.assertFalse(installer.isProductInstalled('plone.app.jquery'))
        self.assertFalse(installer.isProductInstalled('plone.app.collection'))

        from abita.utils.utils import install_packages
        install_packages(self.portal, ['plone.app.jquery', 'plone.app.collection'])

        self.assertTrue(installer.isProductInstalled('plone.app.jquery'))
        self.assertTrue(installer.isProductInstalled('plone.app.collection'))

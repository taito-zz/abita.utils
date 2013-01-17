from Products.CMFCore.utils import getToolByName
from abita.utils.tests.base import IntegrationTestCase

import mock


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

    @mock.patch('abita.utils.utils.getToolByName')
    def test_reimport_profile(self, getToolByName):
        from abita.utils.utils import reimport_profile
        reimport_profile(self.portal, 'PROFILE', 'NAME')
        getToolByName().runImportStepFromProfile.assert_called_with(
            'PROFILE', 'NAME', run_dependencies=False, purge_old=False)

    def test_get_css_resource(self):
        from abita.utils.utils import get_css_resource
        self.assertIsNotNone(get_css_resource(self.portal, 'member.css'))

    def test_get_record(self):
        from abita.utils.utils import get_record
        self.assertIsNotNone(get_record('plone.app.discussion.interfaces.IDiscussionSettings.anonymous_comments'))

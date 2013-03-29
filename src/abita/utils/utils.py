from Products.CMFCore.utils import getToolByName
from plone.registry.interfaces import IRegistry
from zope.component import getUtility

import logging


logger = logging.getLogger(__name__)


def install_packages(context, names):
    """Installs package(s)."""
    installer = getToolByName(context, 'portal_quickinstaller')
    if not isinstance(names, list):
        names = [names]
    for name in names:
        logger.info('Installing {}.'.format(name))
        installer.installProduct(name)


def reimport_profile(context, profile, name):
    setup = getToolByName(context, 'portal_setup')
    logger.info('Reimporting {} with profile: {}.'.format(name, profile))
    setup.runImportStepFromProfile(profile, name, run_dependencies=False, purge_old=False)


def get_css_resource(context, name):
    return getToolByName(context, 'portal_css').getResource(name)


def get_record(name):
    return getUtility(IRegistry).records.get(name)


def get_roles(context, permission):
    return sorted([item['name'] for item in context.rolesOfPermission(permission) if item['selected'] == 'SELECTED'])


def get_workflow(context, name):
    workflow = getToolByName(context, 'portal_workflow')
    return workflow[name]

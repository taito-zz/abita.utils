from Products.CMFCore.utils import getToolByName

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

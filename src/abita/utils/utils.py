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

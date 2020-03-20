# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).

import logging
from odoo import api, SUPERUSER_ID


def migrate(cr, version):
    """Now that everything has been loaded, compute the value of
    channel_method_name.
    """

    if not version:
        return
    env = api.Environment(cr, SUPERUSER_ID, {})
    logger = logging.getLogger('odoo.addons.connector.migrations')
    checkpoints = env['connector.checkpoint'].search([])
    for checkpoint in checkpoints:
        try:
            checkpoint._compute_company()
        except KeyError as e:
            logger.warn(e)

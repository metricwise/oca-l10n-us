from functools import lru_cache
import logging
import re

from odoo import fields, models

_logger = logging.getLogger(__name__)


class Partner(models.Model):
    _inherit = 'res.partner'

    county_id = fields.Many2one('res.country.state.county', ondelete='restrict', domain="[('state_id', '=', state_id)]")

    # Override
    country_id = fields.Many2one(default=lambda self: self.env.ref('base.us').id)

    def _get_county_id(self, name, code):
        code = code[:2].upper()
        name = re.sub(r' County$', '', name)
        return self.__get_county_id(name, code)

    @lru_cache()
    def __get_county_id(self, name, code):
        county = self.env['res.country.state.county'].search([
            ('country_id', '=', self.country_id.id),
            ('name', '=', name),
            ('state_id.code', '=', code)], limit=1)
        if not county.id:
            _logger.warning(f'missing county {name}, {code}')
        return county.id

    @lru_cache()
    def _get_state_id(self, code):
        state = self.env['res.country.state'].search([
            ('country_id', '=', self.country_id.id),
            ('code', '=', code)], limit=1)
        if not state.id:
            _logger.warning(f'missing state {code}')
        return state.id

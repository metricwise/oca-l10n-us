from odoo import models, fields, api


class County(models.Model):
    _name = 'res.country.state.county'
    _description = 'United States County'
    _sql_constraints = [
        ('name_uniq', 'unique(name, state_id)', 'County name must be unique per state!'),
    ]

    name = fields.Char()
    country_id = fields.Many2one('res.country', related='state_id.country_id', readonly=True)
    state_id = fields.Many2one('res.country.state')

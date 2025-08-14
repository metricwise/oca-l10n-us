from odoo import api, fields, models


class Lead(models.Model):
    _inherit = 'crm.lead'

    county_id = fields.Many2one('res.country.state.county', ondelete='restrict', domain="[('state_id', '=', state_id)]")

    @api.onchange('partner_id')
    def _onchange_partner_id(self):
        if self.partner_id.county_id.id:
            self.county_id = self.partner_id.county_id.id

    # Override
    def _prepare_customer_values(self, partner_name, is_company, parent_id=False):
        values = super()._prepare_customer_values(partner_name, is_company, parent_id)
        values['county_id'] = self.county_id.id
        return values

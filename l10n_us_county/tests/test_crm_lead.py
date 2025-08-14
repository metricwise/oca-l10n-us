from odoo.tests import TransactionCase


class TestCrmLead(TransactionCase):
    def test_create_customer(self):
        lead = self.env.ref('crm.crm_case_1')
        lead.county_id = self.env.ref('l10n_us_county.res_country_state_county_1057').id
        customer = lead._create_customer()
        self.assertEqual(customer.county_id, lead.county_id)

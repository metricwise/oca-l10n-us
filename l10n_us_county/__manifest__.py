{
    'name': 'United States - Counties',
    'version': '18.0.0.0.0',
    'category': 'Localization',
    'summary': 'Add United States counties.',
    'description': '''
        Imported from U.S. Census Bureau data.
        https://www.census.gov/library/publications/2011/compendia/usa-counties-2011.html
    ''',

    'author': 'MetricWise, Inc.',
    'license': 'LGPL-3',
    'maintainer': 'Adam Heinz <adam.heinz@metricwise.com>',
    'website': 'https://metricwise.com',

    'depends': [
        'crm',
        'l10n_us',
    ],

    'data': [
        'data/res.country.state.county.csv',
        'security/ir.model.access.csv',
        'views/crm_lead_views.xml',
        'views/partner_views.xml',
    ],
}

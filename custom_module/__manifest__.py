# -*- coding: utf-8 -*-
{
    'name': "CustomModule",

    'summary': """
        This module is used to customise odoo src code to better fit business requirments""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','website','survey','portal'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/account_inherit.xml',
        'views/homepage.xml',
        'views/survey_init_inherit.xml',
        'views/portal_my_home_inherit.xml',
        
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

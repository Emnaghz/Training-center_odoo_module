# -*- coding: utf-8 -*-
{
    'name': "training_center",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'sequence': 1,
    'website': "https://www.odoo.com/fr_FR/app/sales",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', "mail", "auth_signup", "mail", "contacts"],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/level.xml',
        'views/teacher.xml',
        'views/registration.xml',
        'views/claim.xml',
        'security/security.xml',
        'data/data.xml',
        'views/module.xml',
        'views/menu.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    
    'installable': True,
    'auto_install': False,
    'application': True,
}

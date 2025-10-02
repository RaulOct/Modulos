# -*- coding: utf-8 -*-
{
    'name': "utm_ideas_p",

    'summary': "Módulo para realizar tracking de usuarios con el modelo UTM.",

    'description': """
        
    """,

    'author': "Octupus",
    'website': "https://Octupus.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'CRM',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['crm'],

    # always loaded
    'data': [
        # Archivo de inicialización de datos
        'data/utm_medium_data.xml',
        'security/ir.model.access.csv',
        'views/pipes.xml',
        'views/campaign.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

# -*- coding: utf-8 -*-
{
    'name': "um_tree_planting",
    'version': "14.0.1.0.0",
    'summary': """
        Tree Planting""",

    'description': """
        Tree Planting
    """,

    'author': "Digisool",
    'website': "https://digisool.com",
    'license': "AGPL-3",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Tutorials',

    # any module necessary for this one to work correctly
    'depends': ['base', 'mail', 'website'],

    # always loaded
    'data': [

        'security/security.xml',
        'security/ir.model.access.csv',
        # 'views/entitas_views.xml',
        'views/partner_views.xml',
        'views/update_views.xml',
        'views/sequence_data.xml',
        'views/target_views.xml',
        'views/tanam_views.xml',
        'views/views.xml',
        'views/menuitem_views.xml',
        'views/templates.xml',

    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'application': True,
}

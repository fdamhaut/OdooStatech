# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'StatTech',
    'version': '1.0',
    'category': '',
    'sequence': 1,
    'description': """

    """,
    'depends': ['base', 'uom'],
    'data': [
        'security/ir.model.access.csv',
        'views/item.xml',
        'views/item_move.xml',
        'views/machine.xml',
        'views/menu.xml',
    ],
    'application': True,
    'license': 'LGPL-3',
}

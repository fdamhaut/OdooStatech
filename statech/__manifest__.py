# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'StaTech',
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
        'report/item_move_report.xml',
        'views/menu.xml',
    ],
    'application': True,
    'license': 'LGPL-3',
}

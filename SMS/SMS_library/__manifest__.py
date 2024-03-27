# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.


{
    'name': 'Library Management',
    'version': '1.0.0',
    'category': 'education',
    'author': 'techtrios',
    'sequence': -100,
    'summary': 'Educational Module',
    'description': """This is a educational Modules can be used by school""",
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'data/sequence.xml',
        'views/menu_view.xml',
        'views/library_book_view.xml',
        # 'views/library_bookreservation_view.xml',
        'views/library_libarian_view.xml',
        'views/practice.xml',
        'views/library_reservation.xml',
            ],

    'demo': [],
    'application': True,
    'auto_install': False,
    'assets': {},
    'license': 'GPL-3',
}

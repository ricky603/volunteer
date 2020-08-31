# -*- coding: utf-8 -*-
# Part of TigernixERP. See LICENSE file for full copyright and licensing details.
{
    'name' : 'Volunteer Registration',
    'version' : '1.1',
    'summary': 'volunteer Registration form',
    'sequence': 30,
    'description': """
volunteer Registration form.
    """,
    'category': 'Accounting',
    'website': 'https://www.tigernix.com/page/billing',
    'images' : ['images/accounts.jpeg','images/bank_statement.jpeg','images/cash_register.jpeg','images/chart_of_accounts.jpeg','images/customer_invoice.jpeg','images/journal_entries.jpeg'],
    'depends' : ['website'],
    'data': [
        'volunteer.xml',
        'volunteerMenu.xml',
        'data/data.xml'
    ],
    'demo':[],
    'installable': True,
    'application': True,
    'auto_install': False,
}
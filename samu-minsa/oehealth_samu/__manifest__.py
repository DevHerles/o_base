# -*- coding: utf-8 -*-

{
    'name': u'Oehealth SAMU',
    'version': '1.0.0',
    'author': 'Yojana Vilca Aranda',
    'website': 'http://www.arandasf.pe',
    'category': 'Medical',
    'description': u'SAMU',
    'depends': [
        'hr',
        'consultadatos',
        'oehealth',
        'oehealth_emergency',
    ],
    'data': [
        'security/ir.model.access.csv',
        'security/oehealth_samu_security.xml',
        'views/oehealth_samu_mobileunit_views.xml',
        'views/oehealth_samu_schedule_views.xml',
        'views/oehealth_samu_emergency_views.xml',
        'wizard/oehealth_samu_emergency_wizard_views.xml',
        'data/oehealth_samu_emergency_data.xml',
    ],
    'active': False,
    'installable': True
}

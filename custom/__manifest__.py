{
    'name': 'custom',
    'version': '1.0',
    'category': 'Tools',
    'summary': 'custom',
    'depends': ['base', 'sale'],
    'application': True,

    'data': [
        'security/ir.model.access.csv',
        'wizard/update_custom_view.xml',
        'view/custom_view.xml',

    ],
}



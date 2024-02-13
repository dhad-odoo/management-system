{
    'name': "bdonation",
    'depends':[
        'base'
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/bdonation_donor_views.xml',
        'views/bdonation_menus.xml'
    ],
    'installable': True,
    'autoinstall':False,
    'application': True,
}
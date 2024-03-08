{
    'name': "bdonation",
    'depends':[
        'base',
        'event'
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/bdonation_blood_group_views.xml',
        'views/bdonation_blood_request_views.xml',
        'views/bdonation_donor_views.xml',
        'views/bdonation_menus.xml',
        'views/bdonation_inventory_views.xml',
        'views/bdonation_record_views.xml'
    ],
    'installable': True,
    'autoinstall':False,
    'application': True,
}
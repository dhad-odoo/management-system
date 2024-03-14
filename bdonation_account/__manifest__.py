{
    'name': "bdonation_account",
    'depends':[
        'bdonation',
        'account'
    ],
    'data':[
        'views/inherited_bdonation_blood_request_views.xml',
        'views/inherited_account_move_views.xml'
    ],
    'installable': True,
    'autoinstall':False,
    'application': True,
}
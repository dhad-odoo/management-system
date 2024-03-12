{
    'name': "bdonation",
    'depends':[
        'base',
        'event'
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/bdonation_blood_sample_test_views.xml',
        'views/bdonation_converted_blood_components_views.xml',

        'views/bdonation_blood_sample_test_views_result.xml',
        'views/bdonation_blood_group_views.xml',
        'views/bdonation_blood_request_views.xml',
        'views/bdonation_donor_views.xml',
        'views/bdonation_inventory_views.xml',
        'views/bdonation_record_views.xml',
        'views/bdonation_menus.xml',
    ],
    'installable': True,
    'autoinstall':False,
    'application': True,
}
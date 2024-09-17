{ 
'name': 'ILO Farming Perspective', 
'version': '1.0', 
    'depends': [
        'base',
        'sale',
        'stock',
        'project',
        'hr',
        'mrp',
        'web',
        'contacts',
    ],
'author': 'Ali Shidqie Al Faruqi', 
'data':[
    # 'security/ir.model.access.csv',
    'views\ilo_assets_views.xml',
    'views\ilo_farming_menus.xml',
    'views\inherited_custom_views.xml',
    'views\ilo_dashboard_views.xml',
    'views/qr_code_views.xml',
    'views/transactional_views.xml',
    'views\produksi_views.xml',
    'views\ilo_farmer_views.xml',
],
'installable': True, 
'application': True 
} 

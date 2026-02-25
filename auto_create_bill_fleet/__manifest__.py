{
    'name': "Auto Create Vendor Bill from Fleet Services",
    'summary': "Automatically generates vendor bills from fleet vehicle log services when they are completed.",
    'description': """
        Fleet Vehicle Log Services to Vendor Bill Automation
        =====================================================
        This module streamlines the workflow between Fleet management and Accounting.

        Key Features:
        -------------
        *   **Automatic Bill Creation**: Automatically generates a Vendor Bill (account.move) when a Fleet Service log is set to 'Done' state.
        *   **Reference Linking**: Links the generated Vendor Bill directly to the Fleet Service log for easy tracking.
        *   **Smart Navigation**: Adds a button to the Fleet Service form to quickly view the related Vendor Bill.
        *   **Dynamic Descriptions**: Automatically populates bill line descriptions using service type and vehicle information.
        *   **Vendor Validation**: Ensures a vendor is assigned to the service before attempting to create a bill.

        Coming soon: Automatic analytic account mapping

    """,

    'author': "azizbeco",
    'website': "https://uic.group",
    'category': 'Fleet/Accounting',
    'version': '1.0',
    'license': 'LGPL-3',

    'depends': ['fleet', 'account'],

    'data': [
        'views/fleet_vehicle_log_services.xml',
    ],
    'images': ['static/description/main_screenshot.png'],
    'installable': True,
    'application': False,
    'auto_install': False,
}


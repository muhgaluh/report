{
    "name": "Account Custom Report",
    "depends": ["account", "base_custom_report"], # TANPA TIER VALIDATION
    "data": [
        "views/account_move_views.xml",
        "report/account_report_actions.xml",
        "report/bill_template.xml",
    ],
    "installable": True,
}

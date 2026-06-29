{
    "name": "Sale Custom Report",
    "depends": ["sale_management", "base_custom_report", "base_custom_report_tier_validation"],
    "data": [
        "views/sale_order_views.xml",
        "report/sale_report_actions.xml",
        "report/sale_template.xml",
    ],
    "installable": True,
}

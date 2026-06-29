{
    "name": "Purchase Custom Report",
    "summary": "Custom report layout and preview for Purchase Order",
    "version": "16.0.1.0.0",
    "category": "Reporting",
    "author": "DPS-2025",
    "depends": [
        "purchase",
        "purchase_tier_validation",
        "base_custom_report",
        "base_custom_report_tier_validation",
    ],
    "data": [
        "views/res_partner_views.xml",
        "views/purchase_order_views.xml",
        "report/purchase_report.xml",
        "report/purchase_template.xml",
    ],
    "installable": True,
    "auto_install": False,
}

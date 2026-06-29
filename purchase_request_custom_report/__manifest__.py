{
    "name": "Purchase Request Custom Report",
    "summary": "Custom report layout, preview, and dynamic signature for PR",
    "version": "16.0.1.0.0",
    "category": "Reporting",
    "author": "DPS-2025",
    "depends": [
        "purchase_request", 
        "base_custom_report", 
        "base_custom_report_tier_validation"
    ],
    "data": [
        "views/purchase_request_views.xml",
        "report/purchase_request_report.xml",
        "report/purchase_request_template.xml",
    ],
    "installable": True,
    "auto_install": False,
}
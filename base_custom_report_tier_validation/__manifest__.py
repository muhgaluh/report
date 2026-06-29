{
    "name": "Base Custom Report - Tier Validation Bridge",
    "summary": "Membawa logic tier validation ke dalam custom report.",
    "version": "16.0.1.1.0",
    "category": "Reporting",
    "author": "DPS-2025",
    "depends": ["base_custom_report", "base_tier_validation"],
    "data": [
        "views/res_users_views.xml",
        "views/tier_definition_views.xml",
        "report/dynamic_signature_template.xml",
        "report/watermark_template.xml",
    ],
    "installable": True,
    "auto_install": False,
}

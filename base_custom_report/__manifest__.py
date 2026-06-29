{
    "name": "Base Custom Report",
    "summary": "Core framework and universal preview for custom reports.",
    "version": "16.0.1.0.0",
    "category": "Reporting",
    "author": "DPS-2025",
    "depends": ["base", "web"],
    "data": [
        "security/ir.model.access.csv",
        "data/paperformat.xml",
        "views/res_company_views.xml",
        "views/report_preview_wizard_view.xml",
        "report/report_layouts.xml",
    ],
    "installable": True,
    "application": False,
}
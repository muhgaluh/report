{
    "name": "Stock Custom Report",
    "summary": "Dynamic custom reports for Picking and Delivery Orders",
    "version": "16.0.1.0.0",
    "category": "Inventory",
    "author": "DPS-2025",
    "depends": [
        "stock", 
        "base_custom_report", 
        "base_custom_report_tier_validation" # Jika suatu saat gudang butuh tier validation
    ],
    "data": [
        "views/stock_picking_type_views.xml",
        "views/stock_picking_views.xml",
        "report/stock_report_actions.xml",
        "report/picking_template.xml",
        "report/delivery_template.xml",
    ],
    "installable": True,
    "auto_install": False,
}
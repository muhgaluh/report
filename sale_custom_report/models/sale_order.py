from odoo import models


class SaleOrder(models.Model):
    _name = "sale.order"
    _inherit = ["sale.order", "custom.report.mixin"]

    def _get_preview_report_xml_id(self):
        return "sale_custom_report.template_sale_order_custom"

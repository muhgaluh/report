from odoo import models


class StockPicking(models.Model):
    _name = "stock.picking"
    _inherit = ["stock.picking", "custom.report.mixin"]

    def _get_preview_report_xml_id(self):
        # Jika tipe operasinya adalah Delivery Order (keluar)
        if self.picking_type_id.code == "outgoing":
            return "stock_custom_report.template_delivery_custom"

        # Jika tipe operasinya Receipt (masuk) atau Internal Transfer
        return "stock_custom_report.template_picking_custom"

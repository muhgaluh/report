from odoo import models


class PurchaseRequest(models.Model):
    # Meng-inherit model asli PR dan mixin engine report kita
    _name = "purchase.request"
    _inherit = ["purchase.request", "custom.report.mixin"]

    def _get_preview_report_xml_id(self):
        return "purchase_request_custom_report.template_purchase_request_custom"

from odoo import models


class AccountMove(models.Model):
    _name = "account.move"
    _inherit = ["account.move", "custom.report.mixin"]

    def _get_preview_report_xml_id(self):
        return "account_custom_report.template_bill_custom"

from odoo import models, fields, api

class PurchaseOrder(models.Model):
    _name = 'purchase.order'
    _inherit = ['purchase.order', 'custom.report.mixin']

    sequence = fields.Integer(string="Sequence", copy=False, readonly=True, index=True)

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if 'company_id' in vals:
                vals['sequence'] = self.env['ir.sequence'].with_company(vals['company_id']).next_by_code('purchase.order.custom.seq') or 0
            else:
                vals['sequence'] = self.env['ir.sequence'].next_by_code('purchase.order.custom.seq') or 0
        return super(PurchaseOrder, self).create(vals_list)

    def _get_preview_report_xml_id(self):
        # PERBAIKAN: Gunakan nama template QWeb, bukan nama Action
        return 'purchase_custom_report.template_purchase_order_custom'

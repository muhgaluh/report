import base64
from odoo import models, api, _
from odoo.exceptions import UserError

class CustomReportMixin(models.AbstractModel):
    _name = 'custom.report.mixin'
    _description = 'Custom Report Mixin & Preview Engine'

    @api.model
    def _get_preview_report_xml_id(self):
        """
        OVERRIDE method ini di model spesifik untuk mereturn nama template Qweb.
        Contoh: return 'purchase_custom_report.template_purchase_order_custom'
        """
        raise NotImplementedError(_("Definisikan _get_preview_report_xml_id() di model turunan!"))

    def action_preview_report(self):
        self.ensure_one()
        report_name = self._get_preview_report_xml_id()

        # Cari action report berdasarkan nama templatenya
        report_action = self.env['ir.actions.report']._get_report_from_name(report_name)

        if not report_action:
            raise UserError(_("Report Action untuk template '%s' tidak ditemukan.", report_name))

        # PERBAIKAN: Kita panggil dari env dan secara spesifik mendefinisikan parameter res_ids=self.ids
        pdf_content, report_type = self.env['ir.actions.report']._render_qweb_pdf(
            report_ref=report_action.id,
            res_ids=self.ids
        )

        pdf_base64 = base64.b64encode(pdf_content)

        # Buat Transient record untuk wizard
        wizard = self.env['report.preview.wizard'].create({
            'name': f"Preview - {self.display_name or 'Document'}",
            'pdf_file': pdf_base64,
        })

        return {
            'name': _('Report Preview'),
            'type': 'ir.actions.act_window',
            'res_model': 'report.preview.wizard',
            'res_id': wizard.id,
            'view_mode': 'form',
            'target': 'new',
        }

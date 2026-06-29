from odoo import models, fields, api

class CustomReportMixinTier(models.AbstractModel):
    _inherit = 'custom.report.mixin'

    # PERBAIKAN: Kita ubah menjadi field komputasi (Computed Field)
    is_report_draft_status = fields.Boolean(
        string="Is Report Draft?",
        compute='_compute_is_report_draft_status'
    )

    def _compute_is_report_draft_status(self):
        for rec in self:
            status = False
            # Cek apakah modul memiliki fitur validasi tier
            if hasattr(rec, 'validated') and hasattr(rec, 'review_ids'):
                if rec.review_ids and not rec.validated:
                    status = True
            rec.is_report_draft_status = status

    # (Fungsi penarikan data tanda tangan tetap dipertahankan sebagai method publik)
    def get_tier_signature_data(self):
        self.ensure_one()
        signatures = []
        if hasattr(self, 'review_ids'):
            approved_reviews = self.review_ids.filtered(lambda r: r.status == 'approved').sorted(key=lambda r: r.id)
            for review in approved_reviews:
                sig_image = False
                if hasattr(review.done_by, 'sign_signature') and review.done_by.sign_signature:
                    sig_image = review.done_by.sign_signature

                label = 'Approved by:'
                if hasattr(review, 'definition_id') and review.definition_id and hasattr(review.definition_id, 'signature_label'):
                    if review.definition_id.signature_label:
                        label = review.definition_id.signature_label

                signatures.append({
                    'title': label,
                    'name': review.done_by.name,
                    'date': review.reviewed_date,
                    'signature': sig_image,
                })
        return signatures

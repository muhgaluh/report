from odoo import models, fields

class TierDefinition(models.Model):
    _inherit = 'tier.definition'

    signature_label = fields.Char(
        string="Printed Signature Label",
        default="Approved by:",
        help="Label posisi yang akan dicetak di PDF. Contoh: 'Mengetahui,', 'Dibuat Oleh,', 'Disetujui Oleh,'"
    )

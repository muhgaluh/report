from odoo import fields, models


class ResPartner(models.Model):
    _inherit = "res.partner"

    # Menambahkan field PIC baru
    pic = fields.Char(
        string="PIC (Person In Charge)",
        help="Nama PIC (Person In Charge) untuk Vendor/Customer ini.",
    )

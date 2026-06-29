from odoo import models, fields

class ResUsers(models.Model):
    _inherit = 'res.users'

    # Menyimpan file gambar tanda tangan, tipe Binary
    sign_signature = fields.Binary(string="Digital Signature", attachment=True)

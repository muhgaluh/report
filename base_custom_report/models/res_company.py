from odoo import models, fields

class ResCompany(models.Model):
    _inherit = 'res.company'

    iso_logo_1 = fields.Binary(string="ISO Logo 1")
    iso_logo_2 = fields.Binary(string="ISO Logo 2")
    iso_logo_3 = fields.Binary(string="ISO Logo 3")
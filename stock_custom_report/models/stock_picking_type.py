from odoo import models, fields

class StockPickingType(models.Model):
    _inherit = 'stock.picking.type'

    custom_report_title = fields.Char(
        string="Printed Report Title", 
        help="Judul yang akan tercetak di PDF (Misal: SURAT JALAN, SURAT PERMINTAAN BAHAN). Jika kosong, sistem akan memakai nama default."
    )
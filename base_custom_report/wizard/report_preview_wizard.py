from odoo import models, fields

class ReportPreviewWizard(models.TransientModel):
    _name = 'report.preview.wizard'
    _description = 'Universal Report Preview Wizard'

    name = fields.Char(string="Title", readonly=True)
    pdf_file = fields.Binary(string="PDF Content", readonly=True)
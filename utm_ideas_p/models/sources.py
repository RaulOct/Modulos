from odoo import models, fields

class Source(models.Model):
    _name = 'utm.sources'
    _res_name = _name
    _description = 'Fuente de campaña'

    name = fields.Char('Fuente', required=True)
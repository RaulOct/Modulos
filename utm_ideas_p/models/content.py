from odoo import fields, models

class Content(models.Model):
    _name = "utm.content"
    _description = "Contenido de Campaña"

    name = fields.Char(string="Nombre del contenido", required=True)
    traffic = fields.Integer('Tráfico')

    # Relación N-1: muchos contenidos pueden pertenecer a una campaña
    campaign_id = fields.Many2one(
        comodel_name="utm.campaign",
        string="Campaña",
        ondelete="cascade"   # elimina los contenidos si se borra la campaña
    )
    def increase_traffic(self):
        self.traffic += 1

from odoo import models, fields, api

class HidePipes(models.Model):
    _name = "utm.hide.pipes"
    _description = "Tabla paralela a pipes para desplegables dinámicos"

    source_id = fields.Many2one("utm.sources","Fuente", required=True)
    medium_id = fields.Many2one("utm.mediums", "Medio", required=True)

    # CAMPO CALCULADO para obtener el tráfico total de las tuplas
    total_traffic = fields.Float(
        string='Tráfico Total Acumulado',
        compute='_compute_total_traffic',
        store=True  # Calcular al vuelo o almacenar si es muy grande
    )

    # Campo 'name' para que Odoo muestre correctamente en los Many2one
    name = fields.Char(compute='_compute_name', store=True)

    @api.model
    def validar(self, source_id, medium_id):
        """Verifica si la combinación existe usando los IDs."""

        # Búsqueda eficiente usando IDs directamente
        return self.search([
            ("source_id", "=", source_id.id),
            ("medium_id", "=", medium_id.id)
        ], limit=1).exists()
    #Almacena el tráfico de este pipe en todas las campañas
    def _compute_total_traffic(self):
        for record in self:
            for pipe in self.env["utm.pipe"].search([("source_id","=", self.source_id.id),("medium_id","=", self.medium_id.id)]):
                record.total_traffic += pipe.traffic








from odoo import fields, models, api


class Campaign(models.Model):
    _name = 'utm.campaign'
    _description = 'Modelo de campaña'

    name = fields.Char('Nombre', required=True)
    start_date = fields.Datetime('Fecha de inicio', required=True)
    end_date = fields.Datetime('Fecha de termino')
    budget = fields.Float('Presupuesto')

    # Campo calculado. El 'compute' debe usar el nombre del método (sin paréntesis).
    traffic = fields.Integer('Traffic', compute='_compute_total_traffic', store=True)

    # Relación 1-N: una campaña tiene muchos contenidos
    content_ids = fields.One2many(
        comodel_name="utm.content",  # modelo al que apunta
        inverse_name="campaign_id",  # campo Many2one en utm.content
        string="Contenidos"
    )

    # Relación One2many con pipes
    pipe_ids = fields.One2many(
        comodel_name='utm.pipe',
        inverse_name='campaign_id',
        string='Pipes'
    )

    # 🚨 MÉTODO DE CÓMPUTO CORREGIDO 🚨
    # 1. Renombrado a _compute_total_traffic (convención de Odoo).
    # 2. Uso de @api.depends para rastrear cambios en pipe_ids.
    # 3. Iteración sobre self y asignación al campo del registro.

    @api.depends('pipe_ids.traffic')
    def _compute_total_traffic(self):
        for record in self:
            # Suma de la lista de valores del campo 'traffic' en todos los pipe_ids relacionados
            record.traffic = sum(record.pipe_ids.mapped('traffic'))



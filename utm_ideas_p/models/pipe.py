from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Pipe(models.Model):
    _name = 'utm.pipe'
    _description = 'Canal de Comunicación de Campaña'

    # --- Campos ---
    source_id = fields.Many2one('utm.sources', string='Fuente', required=True)
    medium_id = fields.Many2one('utm.mediums', string='Medio', required=True)

    traffic = fields.Integer('Traffic', default=0)
    campaign_id = fields.Many2one('utm.campaign', string='Campaña')

    # --- Campos computados para dominios dinámicos ---
    available_source_ids = fields.Many2many(
        'utm.sources', compute='_compute_available_sources', store=True
    )
    available_medium_ids = fields.Many2many(
        'utm.mediums', compute='_compute_available_mediums', store=True
    )

    @api.depends('medium_id')
    def _compute_available_sources(self):
        hide_pipes = self.env['utm.hide.pipes']
        for rec in self:
            if rec.medium_id:
                hide_records = hide_pipes.search([('medium_id', '=', rec.medium_id.id)])
                rec.available_source_ids = hide_records.mapped('source_id')
            else:
                rec.available_source_ids = self.env['utm.sources'].search([])

    @api.depends('source_id')
    def _compute_available_mediums(self):
        hide_pipes = self.env['utm.hide.pipes']
        for rec in self:
            if rec.source_id:
                hide_records = hide_pipes.search([('source_id', '=', rec.source_id.id)])
                rec.available_medium_ids = hide_records.mapped('medium_id')
            else:
                rec.available_medium_ids = self.env['utm.mediums'].search([])

    # --- Validador final ---
    @api.constrains('source_id', 'medium_id')
    def _check_valid_combination(self):
        hide_pipes = self.env["utm.hide.pipes"]
        for record in self:
            if not hide_pipes.validar(record.source_id, record.medium_id):
                raise ValidationError(
                    f"La combinación de Fuente ({record.source_id.name}) y Medio ({record.medium_id.name}) "
                    "no está permitida según la tabla de validaciones."
                )

    def increase_traffic(self):
        self.ensure_one()
        self.traffic += 1




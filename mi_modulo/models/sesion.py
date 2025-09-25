from odoo import models, fields


class Sesion(models.Model):
    _name = "mi.sesion"
    _description = "Sesión de Entrenamiento"

    name = fields.Char(string="Título de la sesión", required=True)

    trainer_id = fields.Many2one(
        "res.partner",
        string="Instructor",
        domain=[("instructor", "=", True)],  # solo partners con instructor = True
        required=True
    )

    attendee_ids = fields.Many2many(
        "res.partner",
        "mi_sesion_partner_rel", # tabla relacional
        "sesion_id",
        "partner_id",
        string="Asistentes"
    )

    start_datetime = fields.Datetime(
        string="Fecha y hora de inicio",
        required=True,
        default=fields.Datetime.now
    )

    duration = fields.Float(
        string="Duración (horas)",
        default=1.0
    )
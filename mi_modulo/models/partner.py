from odoo import models, fields

class ResPartner(models.Model):
    _inherit = "res.partner"

    instructor = fields.Boolean(
        string="Instructor",
        help="Indica si este contacto es un instructor."
    )

    session_ids = fields.Many2many(
        "mi.sesion",         # 👈 Modelo de sesiones (cámbialo si tiene otro nombre en tu módulo)
        "session_partner_rel",     # 👈 Nombre de la tabla relacional
        "partner_id",              # 👈 Columna que apunta a res.partner
        "session_id",              # 👈 Columna que apunta a session.session
        string="Sesiones"
    )




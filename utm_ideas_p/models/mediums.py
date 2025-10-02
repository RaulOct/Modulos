from odoo import models, fields, api, exceptions


class Medium(models.Model):
    _name = 'utm.mediums'
    _description = 'Medios fijos para las campañas'
    _rec_name = 'name'

    name = fields.Char('Nombre del Medio', required=True, copy=False)


    # Lista de medios que deben existir
    FIXED_MEDIUMS = [
        'organic', 'ppc', 'display', 'social', 'social_paid',
        'referral', 'email', 'newsletter', 'sms', 'push'
    ]

    @api.model
    def _initialize_fixed_mediums(self):
        # 2. Crear medios
        existing_names = self.search([]).mapped('name')
        for medio_name in self.FIXED_MEDIUMS:
            if medio_name not in existing_names:
                self.create({'name': medio_name})

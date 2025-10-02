from urllib.parse import urlparse, parse_qs
from odoo import models, fields, api
from odoo.addons.test_convert.tests.test_env import record


class UTM(models.Model):
    _name = 'utm.utm'
    _description = 'Modelo de la informacion contenida por utm'

    source = fields.Char('Source', required=True)
    medium = fields.Char('Medium', required=True)
    campaign = fields.Text('campaign', required=True)
    term = fields.Char('Term')
    content = fields.Text('Content')

    @api.model
    def create_from_url(self, url):
        """
        Recibe una URL con parámetros UTM y crea un registro en utm.utm
        """
        parsed_url = urlparse(url)
        params = parse_qs(parsed_url.query)

        # Extrae los parámetros UTM (pueden venir como lista en parse_qs)
        values = {
            'source': params.get('utm_source', [''])[0].lower().strip(),
            'medium': params.get('utm_medium', [''])[0].lower().strip(),
            'campaign': params.get('utm_campaign', [''])[0].lower().strip(),
            'term': params.get('utm_term', [''])[0].lower().strip(),
            'content': params.get('utm_content', [''])[0].lower().strip(),
        }

        record = self.env['utm.pipe'].search([
            ('source', '=', values['source']),
            ('medium', '=', values['medium']),
            ('campaign_id.name', '=', values['campaign'])  # Asumiendo que values['campaign'] es el nombre de la campaña
        ], limit=1)
        record.increase_traffic()

        # Crea el registro
        return self.create(values)






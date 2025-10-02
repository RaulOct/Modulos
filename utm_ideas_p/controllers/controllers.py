# -*- coding: utf-8 -*-
from odoo import http


class MiModulo2(http.Controller):
    @http.route('/utm_ideas_p/utm_ideas_p', auth='public')
    def index(self, **kw):
        return "Hello, world"

    @http.route('/utm_ideas_p/utm_ideas_p/objects', auth='public')
    def list(self, **kw):
        return http.request.render('utm_ideas_p.listing', {
            'root': '/utm_ideas_p/utm_ideas_p',
            'objects': http.request.env['utm_ideas_p.utm_ideas_p'].search([]),
        })

    @http.route('/utm_ideas_p/utm_ideas_p/objects/<model("utm_ideas_p.utm_ideas_p"):obj>', auth='public')
    def object(self, obj, **kw):
        return http.request.render('utm_ideas_p.object', {
            'object': obj
        })

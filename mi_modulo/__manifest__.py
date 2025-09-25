{
    'name': 'Mi Módulo',
    'version': '16.0.1.0.0',
    'summary': 'Extensión de res.partner',
    'description': 'Módulo personalizado que extiende los contactos de Odoo',
    'author': 'Octupus',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/partner.xml',# ✅ dejamos solo las vistas
        'views/sesion.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',    # ⚠️ evita el warning
}

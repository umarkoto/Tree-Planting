from odoo import api, fields, models

class Partner(models.Model):
    _inherit = 'res.partner'

    nrp = fields.Char(string='NRP')
    entitas = fields.Char(string='Entitas')
from odoo import models, fields, api

class ILOEmployeeFarmer(models.Model):
    _name = 'ilo.employee.farmer'
    _description = 'ILO Farmer'

    actor_code = fields.Char(string='Actor Code')
    actor_type = fields.Selection([
        ('farmer', 'Farmer'),
        ('agent', 'Agent/Koperasi'),
        ('ugreen', 'Ugreen'),
        ('green', 'Green')
    ], string='Actor Type')
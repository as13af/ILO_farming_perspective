from odoo import models, fields, api

class ILOAssets(models.Model):
    _name = 'ilo.assets'
    _description = 'Asset Management for Farmers'
    
    name = fields.Char('Asset Name', required=True)
    employee_id = fields.Many2one('res.partner', string='Employee')
    coordinates = fields.Char(string='Coordinates (Lat,Long)')
    dashboard_id = fields.Many2one('ilo.dashboard', string='Dashboard', ondelete='cascade')
    ownership_status = fields.Selection([
        ('rent', 'Rent'),
        ('self_owned', 'Self-Owned'),
        ('other', 'Other'),
    ], string='Ownership Status')
    area_ha = fields.Float(string='Area (Ha)')
    address = fields.Text(string='Address')
    planting_status = fields.Selection([
        ('proses', 'Process'),
        ('selesai', 'Completed'),
    ], string='Planting Status')
    planting_progress = fields.Float(string='Planting Progress')

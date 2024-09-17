from odoo import models, fields, api

class ILOProduksi(models.Model):
    _name = 'ilo.production'
    _description = 'production Management'

    employee_id = fields.Many2one('res.partner', string='Employee', domain=[('actor_type', '=', 'farmer')], required=True)
    date_planned_start = fields.Datetime(string='Date Planned Start', related='mrp_production_id.date_planned_start')
    date_planned_finished = fields.Datetime(string='Date Planned Finish', related='mrp_production_id.date_planned_finished')
    product_quantity = fields.Float(string='Product Quantity', related='mrp_production_id.product_qty')
    farm_coordinates = fields.Char(string='Farm Coordinates', related='ilo_assets_id.coordinates')
    farm_location = fields.Text(string='Farm Location', related='ilo_assets_id.address')
    mrp_production_id = fields.Many2one('mrp.production', string='Production Order', required=True)
    ilo_assets_id = fields.Many2one('ilo.assets', string='Farm Assets', required=True)
    quality_check_status = fields.Selection([
        ('pending', 'Pending'),
        ('passed', 'Passed'),
        ('failed', 'Failed')
    ], string='Quality Check Status', help="Status of quality checks for the production.")
    

    @api.constrains('employee_id')
    def _check_employee(self):
        if not self.employee_id or self.employee_id.actor_type != 'farmer':
            raise exceptions.ValidationError("Employee must be a farmer.")

    @api.onchange('mrp_production_id')
    def _onchange_production(self):
        if self.mrp_production_id:
            self.date_planned_start = self.mrp_production_id.date_planned_start
            self.date_planned_finished = self.mrp_production_id.date_planned_finished
            self.product_quantity = self.mrp_production_id.product_qty
            # Assuming there's a field that links production to assets
            if self.mrp_production_id.ilo_assets_id:
                self.ilo_assets_id = self.mrp_production_id.ilo_assets_id.id

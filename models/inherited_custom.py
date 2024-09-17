from odoo import models, fields, api

# class ILOSaleOrder(models.Model):
#     _inherit = 'sale.order'
    
    # dashboard_id = fields.Many2one('ilo.dashboard', string='Dashboard', ondelete='cascade')
    # farm_location = fields.Char(string='Farm Location', help="Location of the farm where the products are sold.")
    # production_capacity = fields.Float(string='Production Capacity', help="The maximum production capacity of the farm.")

class ILOEmployee(models.Model):
    _inherit = 'res.partner'

    family_members = fields.Integer(string='Family Members')
    organization_status = fields.Selection([
        ('member', 'Member'),
        ('not_member', 'Not Member')
    ], string='Organization Status')
    organization_name = fields.Char(string='Organization Name')
    employment_contract = fields.Binary(string='Employment Contract')
    contract_file_name = fields.Char(string='Contract File Name')
    type_of_partner = fields.Selection([
        ('cooperative', 'Cooperative'),
        ('not_cooperative', 'Not Cooperative')
    ], string='Type of Partner')
    # ilotes = fields.Char(string='ILO User')
    # partneree_type = fields.Char(string='Organization Name')
    
    # function_code = fields.Char(string='Function Code', compute='_compute_function_code', store=True)
    
    # @api.depends('function')
    # def _compute_function_code(self):
    #     for record in self:
    #         if record.function:
    #             record.function_code = self._generate_code(record.function)
    #         else:
    #             record.function_code = False

    # def _generate_code(self, text):
    #     if not text:
    #         return ''
    #     words = text.split()
    #     if len(words) == 1:
    #         # For single-word text, use the first two letters
    #         return words[0][:2].upper()
    #     else:
    #         # For multi-word text, use the first letter of each word
    #         return ''.join([word[0].upper() for word in words])

    # Overriding create method to generate actor code
    # @api.model
    # def create(self, vals):
    #     if vals.get('actor_code', '/') == '/':
    #         vals['actor_code'] = self._generate_actor_code(vals.get('actor_type'))
    #     return super(ILOEmployee, self).create(vals)

    # # Method to generate actor code
    # def _generate_actor_code(self, actor_type):
    #     """Generates the actor code based on actor type with sequential numbering."""
    #     prefix = {'farmer': 'F', 'agent': 'A', 'ugreen': 'UG', 'green': 'G'}[actor_type]
    #     last_actor = self.search([('actor_type', '=', actor_type)], order="actor_code desc", limit=1)
    #     last_number = int(last_actor.actor_code.replace(prefix, '').lstrip('0')) if last_actor else 0
    #     new_number = last_number + 1
    #     return f"{prefix}{str(new_number).zfill(3)}"  # Codes padded to 3 digits, e.g., F001, A002


class ILOMrp(models.Model):
    _inherit = 'mrp.production'
    
    dashboard_id = fields.Many2one('ilo.dashboard', string='Dashboard', ondelete='cascade')
    production_line = fields.Char(string='Production Line', help="Production line where the manufacturing occurs.")
    ownership_codes = fields.One2many('ownership.code', 'production_id', string='Ownership Codes')
    quality_check_status = fields.Selection([
        ('pending', 'Pending'),
        ('passed', 'Passed'),
        ('failed', 'Failed')
    ], string='Quality Check Status', help="Status of quality checks for the production.")
    

class ILOStock(models.Model):
    _inherit = 'stock.quant'

class ILOInventory(models.Model):
    _inherit = 'stock.inventory'

    dashboard_id = fields.Many2one('ilo.dashboard', string='Dashboard', ondelete='cascade')
    employee_id = fields.Many2one('res.partner', string='Employee')
    assets_id = fields.Many2one('ilo.assets', string='Asset')
    mrp_production_id = fields.Many2one('mrp.production', string='MRP Production')
    planned_start_date = fields.Datetime(related='mrp_production_id.date_planned_start', string='Planned Start Date')
    planned_end_date = fields.Datetime(related='mrp_production_id.date_planned_finished', string='Planned End Date')
    status = fields.Selection([
        ('available', 'Available'),
        ('empty', 'Empty'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
    ], string='Status')
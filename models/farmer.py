from odoo import models, fields, api, exceptions

class ILOFarmer(models.Model):
    _name = 'ilo.farmer'
    _description = 'ILO Farmer'

    farm_id = fields.Char(string='Farm ID', required=True, help="Unique identifier for the farm.")
    province = fields.Char(string='Province', required=True, help="Province where the farm is located.")
    crop_type = fields.Many2one('product.product', string='Crop Type', required=True, help="Link to the product as the crop type.")
    farm_size = fields.Float(string='Farm Size', default=5.0, help="Size of the farm in hectares or acres.")
    farm_location = fields.Char(string='Farm Location', help="Location of the farm.")
    production_capacity = fields.Float(string='Production Capacity', help="The maximum production capacity of the farm.")

    @api.model
    def create(self, vals):
        if not self.env.context.get('bypass_farm_check'):
            partner = self.env['res.partner'].browse(vals.get('partner_id'))
            if not partner or partner.actor_type != 'farmer':
                raise exceptions.ValidationError("Farm ID and Farm Size can only be created for partners with 'Farmer' actor type.")
        return super(ILOFarmer, self).create(vals)

    def _generate_farm_id(self):
        # Province code generation logic
        province_code = self._generate_code(self.province)

        # Crop code generation logic
        crop_code = self._generate_code(self.crop_type.name)  # Ensure you're using the crop type name

        # Sequential number for unique farm ID
        sequence = self.env['ir.sequence'].next_by_code('ilofarmer.sequence')
        
        # Combine the generated codes and the sequence
        return f'{province_code}-{crop_code}-{sequence}'

    def _generate_code(self, text):
        words = text.split()
        if len(words) == 1:
            # For single-word province or crop, use the first two letters
            return words[0][:2].upper()
        else:
            # For multi-word province or crop, use the first letter of each word
            return ''.join([word[0].upper() for word in words])

    @api.onchange('province', 'crop_type')
    def _onchange_province_crop(self):
        if self.province and self.crop_type:
            self.farm_id = self._generate_farm_id()

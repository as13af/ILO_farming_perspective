from odoo import models, fields, api, exceptions

class OwnershipCode(models.Model):
    _name = 'ownership.code'
    _description = 'Ownership Code'

    name = fields.Char(string='Ownership Code', required=True, index=True)
    source_actor = fields.Many2one('res.partner', string='Source Actor', required=True)
    destination_actor = fields.Many2one('res.partner', string='Destination Actor', required=True)
    batch_code_id = fields.Many2one('product.batch', string='Batch Code', required=True)
    quantity = fields.Float(string='Quantity', required=True)
    transaction_number = fields.Integer(string='Transaction Number', required=True)
    product_id = fields.Many2one('product.product', string='Product', related='batch_code_id.product_id', store=True)  # Link crop type to batch
    history = fields.Text(string='History')  # Track historical changes
    production_id = fields.Many2one('mrp.production', string='Production Order')  # Link to MRP Production

    # @api.model
    # def create(self, vals):
    #     # Fetch actor codes
    #     source_code = self.env['res.partner'].browse(vals['source_actor']).function_code
    #     dest_code = self.env['res.partner'].browse(vals['destination_actor']).function_code
    #     batch_code = self.env['product.batch'].browse(vals['batch_code_id']).batch_code
    #     quantity = str(int(vals['quantity']))  # Convert to integer for readability
    #     transaction_num = str(vals['transaction_number']).zfill(2)
        
    #     # Generate Ownership Code
    #     ownership_code = f"{source_code}-{batch_code}-{dest_code}-{quantity}-{transaction_num}"
    #     vals['name'] = ownership_code
        
    #     # Create ownership code record
    #     new_record = super(OwnershipCode, self).create(vals)
        
    #     # Update batch quantity
    #     batch_record = self.env['product.batch'].browse(vals['batch_code_id'])
    #     batch_record.update_quantity(vals['quantity'])
        
    #     # Add history entry
    #     new_record.history = f"Created: {ownership_code} with quantity {quantity}."
        
    #     return new_record

    # @api.constrains('source_actor', 'destination_actor')
    # def _check_source_and_destination(self):
    #     if self.source_actor == self.destination_actor:
    #         raise exceptions.ValidationError("Source and destination actors must be different.")

    # @api.constrains('transaction_number', 'source_actor', 'destination_actor', 'product_id')
    # def _check_unique_transaction_number(self):
    #     existing_transaction = self.search([('source_actor', '=', self.source_actor.id),
    #                                         ('destination_actor', '=', self.destination_actor.id),
    #                                         ('transaction_number', '=', self.transaction_number),
    #                                         ('product_id', '=', self.product_id.id)])
    #     if existing_transaction:
    #         raise exceptions.ValidationError("A transaction with this number already exists between these actors for this product.")

class ProductBatch(models.Model):
    _name = 'product.batch'
    _description = 'Product Batch Tracking'

    product_id = fields.Many2one('product.product', string='Product', required=True)
    batch_code = fields.Char(string='Batch Code', required=True, default='/')
    available_quantity = fields.Float(string='Available Quantity', required=True)
    ownership_codes = fields.One2many('ownership.code', 'batch_code_id', string='Ownership Codes')

    @api.model
    def create(self, vals):
        if vals.get('batch_code', '/') == '/':
            vals['batch_code'] = self._generate_batch_code(vals.get('product_id'))
        return super(ProductBatch, self).create(vals)

    def _generate_batch_code(self, product_id):
        """Generate batch code based on product name."""
        product = self.env['product.product'].browse(product_id)
        product_name = product.name
        return self._generate_code(product_name)

    def _generate_code(self, text):
        """Generate code by taking first letters of words or first two letters."""
        words = text.split()
        if len(words) == 1:
            return words[0][:2].upper()
        else:
            return ''.join([word[0].upper() for word in words])



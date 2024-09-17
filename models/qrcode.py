from odoo import models, fields, api
import qrcode
from io import BytesIO
import base64

class ILOQRCode(models.Model):
    _name = 'qr.code'
    _description = 'QR Code Management'

    # Name of the QR code record
    name = fields.Char(string='Name', required=True)
    
    # Data to encode in the QR code
    data = fields.Text(string='Data', required=True)
    
    # Field to store the QR code image
    qr_code = fields.Binary(string='QR Code Image', attachment=True)
    
    # Field to store the image filename
    qr_code_filename = fields.Char(string='QR Code Filename')

    @api.model
    def create(self, vals):
        # Check if 'data' is in vals and is not empty before generating QR code
        if vals.get('data'):
            vals['qr_code'] = self._generate_qr_code(vals['data'])
            vals['qr_code_filename'] = 'qrcode.png'
        return super(ILOQRCode, self).create(vals)

    def write(self, vals):
        # Regenerate QR code if 'data' is updated and not empty
        if vals.get('data'):
            vals['qr_code'] = self._generate_qr_code(vals['data'])
            vals['qr_code_filename'] = 'qrcode.png'
        return super(ILOQRCode, self).write(vals)

    def _generate_qr_code(self, data):
        """
        Generate a QR code from the provided data and return it as base64-encoded PNG.
        """
        qr = qrcode.QRCode(version=1, box_size=10, border=4)
        qr.add_data(data)
        qr.make(fit=True)

        img = qr.make_image(fill='black', back_color='white')
        
        # Save image to a BytesIO stream
        img_io = BytesIO()
        img.save(img_io, 'PNG')
        img_io.seek(0)

        # Encode the image to base64
        qr_code_base64 = base64.b64encode(img_io.read())
        return qr_code_base64.decode('ascii')

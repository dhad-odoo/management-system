# models.py

from odoo import models, fields

class BloodInventory(models.Model):
    _name = 'bdonation.inventory'
    _description = 'Blood Bank Inventory'

    blood_type = fields.Selection([
        ('A+', 'A+'),
        ('B+', 'B+'),
        ('AB+', 'AB+'),
        ('O+', 'O+'),
        ('A-', 'A-'),
        ('B-', 'B-'),
        ('AB-', 'AB-'),
        ('O-', 'O-'),
    ], string='Blood Type', required=True)
    quantity = fields.Float(string='Quantity(in ml)', default=0.0)
    expiration_date = fields.Date(string='Expiration Date')
    is_expired = fields.Boolean(compute="_compute_expiration_date")

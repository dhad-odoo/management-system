# models.py

from odoo import models, fields

class BloodInventory(models.Model):
    _name = 'bdonation.inventory'
    _description = 'Blood Bank Inventory'

    component_type = fields.Selection([
        ('A+', 'A+'),
        ('B+', 'B+'),
        ('AB+', 'AB+'),
        ('O+', 'O+'),
        ('A-', 'A-'),
        ('B-', 'B-'),
        ('AB-', 'AB-'),
        ('O-', 'O-'),
    ], string='Component Type', required=True)
    quantity = fields.Float(string='Quantity(in ml)', default=0.0)

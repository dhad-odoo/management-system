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
        ('plasma', 'Plasma'),
        ('rbc', 'Red Blood Cells (RBC)'),
        ('platelets', 'Platelets')
    ], string='Component Type', required=True)
    quantity = fields.Float(string='Quantity(in ml)', default=0.0)
    status = fields.Selection([
        ('inventory','Inventory'),
        ('sold', 'Sold'),
        ('expired','Expired')
    ], string ='Status', required=True, default='inventory')
    request_id= fields.Many2one('bdonation.blood.request', string= 'Record assigned to Request', readonly=True)

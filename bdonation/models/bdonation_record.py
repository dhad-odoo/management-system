from odoo import models, fields

class BloodDonationRecord(models.Model):
    _name = 'bdonation.record'
    _description = 'Blood Donation Record'

    donor_id = fields.Many2one('bdonation.donor', string='Donor', required=True)
    donation_date = fields.Date(string='Donation Date', default=fields.Date.today())
    quantity_donated = fields.Float(string='Quantity Donated(in ml)', default=0.0)
    status = fields.Selection([
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('rejected', 'Rejected'),
    ], string='Status', default='pending')
    notes = fields.Text(string='Notes')
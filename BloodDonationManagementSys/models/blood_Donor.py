from odoo import models, fields

class bloodDonor(models.Model):
    _name = 'blood.donor'
    _description = 'Blood Donor'

    name = fields.Char(string='Name', required=True)
    contact_number = fields.Char(string='Contact Number')
    blood_type = fields.Selection([
        ('A+', 'A+'),
        ('B+', 'B+'),
        ('AB+', 'AB+'),
        ('O+', 'O+'),
        ('A-', 'A-'),
        ('B-', 'B-'),
        ('AB-', 'AB-'),
        ('O-', 'O-'),
    ], string='Blood Type')
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ], string='Gender')
    date_of_birth = fields.Date(string='Date of Birth')
    last_donation_date = fields.Date(string='Last Donation Date')
    notes = fields.Text(string='Notes')

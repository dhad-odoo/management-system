from odoo import models, fields, api

class bdonationDonor(models.Model):
    _name = 'bdonation.donor'
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
    donation_interval = fields.Integer(compute='_compute_last_doantion_interval', string='Last Donation Interval (in Days)')
    notes = fields.Text(string='Notes')
    donation_ids =fields.One2many('bdonation.record', 'donor_id', string ='Donation History')
    age = fields.Integer(compute='_compute_age', string="Age(in years)", store="True")
    can_donate = fields.Boolean(compute='_compute_can_donate', string="Can Doante")

    @api.depends('donation_interval','age')
    def _compute_can_donate(self):
        today = fields.Date.today()
        for donor in self:
            # Check if the donor is within the eligible age range (e.g., 18 to 60 years)
            age_eligible = 18 <= donor.age <= 60

            # Check if the last donation was more than a predefined interval (e.g., 60 days) ago
            donation_interval_eligible = donor.donation_interval >= 60

            donor.can_donate = age_eligible and donation_interval_eligible




    @api.depends('donation_ids')
    def _compute_last_doantion_interval(self):
        for donor in self:
            if donor.donation_ids:
                last_don = fields.Date.today()
                for donation  in donor.donation_ids:
                    if donation.donation_date < last_don:
                        last_don = donation.donation_date
                donor.donation_interval = (fields.Date.today() - last_don).days
            
            else:
                 donor.donation_interval=0
                

    @api.depends('date_of_birth')
    def _compute_age(self):
        today = fields.Date.today()
        for donor in self:
            donor.age =int( today.year - donor.date_of_birth.year) - int((today.month, today.day) < (donor.date_of_birth.month, donor.date_of_birth.day))




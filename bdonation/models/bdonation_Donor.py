from odoo import models, fields, api

from odoo.exceptions import UserError, ValidationError

from datetime import datetime, timedelta

class bdonationDonor(models.Model):
    _name = 'bdonation.donor'
    _description = 'Blood Donor Details'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Name', required=True)
    contact_number = fields.Char(string='Contact Number')
    date_of_birth = fields.Date(string='Date of Birth', default=fields.Date.today())
    age = fields.Integer( compute='_compute_age',string="Age(in years)", store="True")
    marital_status = fields.Char(string="Marital Status")
    donor_image = fields.Image(string="Donor's Picture", max_width=150, max_height=150)
    
    donation_interval = fields.Integer(compute='_compute_last_doantion_interval', string='Last Donation Interval (in Days)')
    bmi = fields.Float(compute='_compute_bmi',string= "Body Mass Index")
    height = fields.Float(string= "Height(cm)")
    weight = fields.Float(string= "Weight(Kg)")
    gender = fields.Selection(
        string="Gender",
        selection= [
            ('male','Male'),
            ('female','Female'),
            ('other','Other')
        ]
    )
    occupation = fields.Char(string="Occupation")
    email_address = fields.Char(string="Email Address")
    blood_group_id  = fields.Many2one('bdonation.blood.group', string='Blood Group')
    haemoglobin_levels = fields.Float(string='Haemoglobin levels (gms/hundred ml)')
    notes = fields.Text(string='Notes')
    donation_ids =fields.One2many('bdonation.record', 'donor_id', string ='Donation History')
    
    can_donate = fields.Boolean(compute='_compute_can_donate', string="Can Doante")
    event_ids = fields.Many2many('event.event', string='Attended Events', help='Events attended by the donor')

    @api.depends('donation_interval','age')
    def _compute_can_donate(self):
        today = fields.Date.today()
        for donor in self:
            # Check if the donor is within the eligible age range (e.g., 18 to 60 years)
            age_eligible = 18 <= donor.age <= 60

            # Check if the last donation was more than a predefined interval (e.g., 60 days) ago
            donation_interval_eligible = donor.donation_interval >= 60

            if age_eligible and donation_interval_eligible:
                donor.can_donate = True
            else:
                donor.can_donate = False
    
    @api.depends('height','weight')
    def _compute_bmi(self):
        if self.height and self.weight:
            height_in_meter = self.height/100
            self.bmi = self.weight/(height_in_meter * height_in_meter)



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
        today = datetime.today().date()
        for donor in self:
            donor.age =int( today.year - donor.date_of_birth.year) - int((today.month, today.day) < (donor.date_of_birth.month, donor.date_of_birth.day))
    

    @api.onchange('donation_interval',"age","bmi")
    def onchange_donation_delay_days_age_bmi(self):
        if self and self.donation_interval and self.age and self.bmi:
            if self.donation_interval > 120 and self.age >=18 and self.age <=65 and self.bmi >18.5:
                self.can_donate = 1
            else:
                self.can_donate = 0
    

    def action_can_donate(self):
        today = fields.Date.today()
        for donor in self:
            # Check if the donor is within the eligible age range (e.g., 18 to 60 years)
            age_eligible = 18 <= donor.age <= 60

            # Check if the last donation was more than a predefined interval (e.g., 60 days) ago
            if donor.donation_ids:
                donation_interval_eligible = donor.donation_interval >= 60
            else :
                donation_interval_eligible = True

            if age_eligible and donation_interval_eligible:
                donor.can_donate = True
                raise UserError("Eligible for donating blood.")
            else:
                donor.can_donate = False
                raise UserError("Not Eligible for donating blood.")
    



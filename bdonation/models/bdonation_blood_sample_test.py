from odoo import models, fields

class BloodSampleTestResult(models.Model):
    _name = 'bdonation.blood.sample.test'
    _description = 'Blood Donation Test'

    name = fields.Char(string='Test Name')

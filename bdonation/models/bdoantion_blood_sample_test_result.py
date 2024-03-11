from odoo import models, fields

class BloodSampleTestResult(models.Model):
    _name = 'bdonation.blood.sample.test.result'
    _description = 'Blood Donation Test Result'

    donation_record_id = fields.Many2one('bdonation.record', string='Donation Record')
    test_name = fields.Many2one('bdonation.blood.sample.test')
    result = fields.Selection([('pass', 'Pass'), ('fail', 'Fail')], string='Result')

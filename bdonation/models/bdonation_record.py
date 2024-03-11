from odoo import models, fields
import datetime
import uuid

class BloodDonationRecord(models.Model):
    _name = 'bdonation.record'
    _description = 'Blood Donation Record'

    donor_id = fields.Many2one('bdonation.donor', string='Donor', required=True)
    donation_date = fields.Date(string='Donation Date', default=fields.Date.today())
    quantity_donated = fields.Float(string='Quantity Donated(in ml)', default=0.0)
    status = fields.Selection([
        ('pending', 'Pending'),
        ('collected', 'Collected'),
        ('testing', 'Testing'),
        ('completed', 'Completed'),
        ('rejected', 'Rejected'),
    ], string='Status', default='pending')
    notes = fields.Text(string='Notes')
    tests_results = fields.One2many('bdonation.blood.sample.test.result', 'donation_record_id', string='Test Results')
    barcode = fields.Char(string='Barcode')

    def action_collect_blood(self):
        timestamp = int(datetime.datetime.now().timestamp())
        unique_id = str(uuid.uuid4().hex)[:8]  # Use the first 8 characters of a UUID
        barcode = f'BD{timestamp}-{unique_id}'
        self.write({'status': 'collected', 'barcode': barcode})

    def action_reject(self):
        self.write({'status': 'rejected'})
    
    def action_move_to_tesing_blood(self):
        self.write({'status': 'testing'})

        
    def action_pass_test_blood(self):
        self.write({'status': 'completed'})




# first record is in pending state - at this point 2 buttons are visible in header , 'collect blood' and 'reject'
# After clicking 'collect blood' button,  record goes to 'testing' state

# In testing state- there are 2 buttons , 'pass-testing state' and 'fail-tesing state /reject'
# After clicking  'pass-testing state', pop up dialog box appears with list of tests, user has to mark all tests as pass or fail then if all tests pass ,then move record to 'testing complected ' state 

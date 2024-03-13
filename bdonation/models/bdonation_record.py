from odoo import models, fields
import datetime
import uuid

class BloodDonationRecord(models.Model):
    _name = 'bdonation.record'
    _description = 'Blood Donation Record'

    donor_id = fields.Many2one('bdonation.donor', string='Donor', required=True)
    donation_date = fields.Date(string='Donation Date', default=fields.Date.today())
    quantity_donated = fields.Float(string='Quantity Donated(in ml)', default=470.0, readonly=True)
    status = fields.Selection([
        ('pending', 'Pending'),
        ('collected', 'Collected'),
        ('testing', 'Testing'),
        ('completed', 'Completed'),
        ('converted', 'Converted'),
        ('add_to_inventory','Add to Inventory'),
        ('rejected', 'Rejected'),
    ], string='Status', default='pending')
    notes = fields.Text(string='Notes')
    tests_results = fields.One2many('bdonation.blood.sample.test.result', 'donation_record_id', string='Test Results')
    barcode = fields.Char(string='Barcode')
    converted_component_ids= fields.One2many('bdonation.converted.blood.component', 'record_id', string ='Converted Components')
    inventory_id= fields.Many2one('bdonation.inventory', string= 'Added to inventory at : ', readonly=True)


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

    

    def action_convert_to_components(self):
        if self.status == 'completed':
            total_quantity = self.quantity_donated 
            plasma_quantity = total_quantity * 0.54
            rbc_quantity = total_quantity * 0.45
            platelets_quantity = total_quantity * 0.01

            converted_components_data = [
                { 'record_id': self.id,'blood_component_type': 'plasma', 'quantity': plasma_quantity},
                { 'record_id': self.id,'blood_component_type': 'rbc', 'quantity': rbc_quantity},
                { 'record_id': self.id, 'blood_component_type': 'platelets','quantity': platelets_quantity},
            ]

            converted_components = self.env['bdonation.converted.blood.component'].create(converted_components_data)

            self.converted_component_ids = converted_components

            self.write({'status': 'converted'})

    
    def action_add_to_inventory(self):
        if self.status == 'completed':

            inventory_data = [
                { 'component_type': self.donor_id.blood_group, 'quantity': self.quantity_donated}
            ]

            print(inventory_data)

            inventory_record = self.env['bdonation.inventory'].create(inventory_data)
            self.inventory_id=inventory_record
            self.write({'status': 'add_to_inventory'})



    




# first record is in pending state - at this point 2 buttons are visible in header , 'collect blood' and 'reject'
# After clicking 'collect blood' button,  record goes to 'testing' state

# In testing state- there are 2 buttons , 'pass-testing state' and 'fail-tesing state /reject'
# After clicking  'pass-testing state', pop up dialog box appears with list of tests, user has to mark all tests as pass or fail then if all tests pass ,then move record to 'testing complected ' state 

# as a blood bank have whole blood, now i can convert some whole blood into blood components like RBC , WBC, Platlates etc, 

# now as i have 4 things that i can sell (whole blood, plasma, RBC, platelates) , 
# customers come make  request for any one of the 4 products. then 
# if whole blood is selected then show all available products for whole blood
# similarly for plasma and platelates and RBC
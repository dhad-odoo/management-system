
from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError
from datetime import datetime
from datetime import timedelta
from dateutil.relativedelta import relativedelta



class ConvertedBloodComponent(models.Model):
    _name = 'bdonation.converted.blood.component'
    _description = 'Converted Blood Component'

    record_id = fields.Many2one('bdonation.record', string='Record used for this componet\'s extraction', required =True)
    blood_component_type = fields.Selection([
        ('plasma', 'Plasma'),
        ('rbc', 'Red Blood Cells (RBC)'),
        ('platelets', 'Platelets')
    ], string='Blood Component Type',required=True)
    status=fields.Selection(
        [
            ('new','New'),
            ('add_to_inventory','Add to inventory')
        ], default='new',)
    quantity = fields.Float(string='Quantity (in ml)')
    inventory_id= fields.Many2one('bdonation.inventory', string= 'Added to inventory at : ', readonly=True)





    def action_add_to_inventory(self):
        if self.status == 'new':

            inventory_data = [
                { 'component_type': self.blood_component_type, 'quantity': self.quantity}
            ]

            inventory_record = self.env['bdonation.inventory'].create(inventory_data)
            self.inventory_id=inventory_record

            self.write({'status': 'add_to_inventory'})


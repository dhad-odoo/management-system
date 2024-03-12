
from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError
from datetime import datetime
from datetime import timedelta
from dateutil.relativedelta import relativedelta



class ConvertedBloodComponent(models.Model):
    _name = 'bdonation.converted.blood.component'
    _description = 'Converted Blood Component'

    record_id = fields.Many2one('bdonation.record', string='Record used for this componet extraction', required =True)
    blood_component_type = fields.Selection([
        ('plasma', 'Plasma'),
        ('rbc', 'Red Blood Cells (RBC)'),
        ('platelates', 'Platelates')
    ], string='Blood Component Type',required=True)
    quantity = fields.Float(string='Quantity (in ml)')

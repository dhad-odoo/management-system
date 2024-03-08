
from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError
from datetime import datetime
from datetime import timedelta
from dateutil.relativedelta import relativedelta


class BloodGroup(models.Model):
    _name = "bdonation.blood.group"
    _description = "Donor Blood Group"
    _rec_name = 'name'

    name = fields.Char(string = "Blood Group")

    donor_ids = fields.One2many('bdonation.donor', 'blood_group_id', string="Donors")
    
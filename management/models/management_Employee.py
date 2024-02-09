from odoo import models, fields


class managementEmployee(models.Model):
    _name = "management.employee"
    _description = "This is the employee's details"

    name = fields.Char(required=True)
    department=fields.Char(required=True)
    age=fields.Integer(required=True)
    positon = fields.Selection(
        selection=[('doctor', 'Doctor'), ('wardAssistant', 'Ward Assistant'), ('receptionist ', 'Receptionist')]
    )
    gender = fields.Selection(
        selection=[('male', 'Male'), ('female', 'Female'), ('other','Other')]
    )

    
    
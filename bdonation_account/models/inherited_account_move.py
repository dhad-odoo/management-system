from odoo import models, fields


class InheritedAccountMove(models.Model):
    _inherit ="account.move"

    patient_name = fields.Char(string="Patient Name", related="blood_request_id.patient_name", readonly=True)

    blood_request_id = fields.Many2one('bdonation.blood.request', string='Blood Request')

    def action_view_blood_request(self):
        return {
            "type": "ir.actions.act_window",
            "name": "Blood Request",
            "res_model": "bdonation.blood.request",
            "res_id": self.blood_request_id.id,
            "view_mode": "form",
            "target": "current",
        }



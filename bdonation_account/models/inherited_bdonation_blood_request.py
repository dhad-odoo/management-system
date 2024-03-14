from odoo import models, Command,fields


class InheritedBdonationBloodRequest(models.Model):
    _inherit ="bdonation.blood.request"

    invoice_id=fields.Many2one("account.move", string ="Related Invoice")


    def action_create_invoice(self):


        invoice=self.env["account.move"].sudo().create(
                {
                    "blood_request_id":self.id,
                    "partner_id":self.hospital_id.id,
                    "move_type":"out_invoice",
                    "invoice_line_ids":[
                        Command.create(
                            { 
                                "name" : self.component_type,
                                "quantity": self.num_records_requested,
                                "price_unit": 1000 
                            }
                        ),
                        Command.create(
                            {
                                "name" : "Administrative Fees",
                                "quantity": 1.0,
                                "price_unit": 100.0 
                            
                            }
                        )
                    ]

                }
            )
        self.invoice_id=invoice

        return {
            "type": "ir.actions.act_window",
            "name": "Invoices",
            "res_model": "account.move",
            "res_id": invoice.id,
            "view_mode": "form",
            "target": "current",
        }


    def action_open_related_invoice(self):
        return {
            "type": "ir.actions.act_window",
            "name": "Invoices",
            "res_model": "account.move",
            "res_id": self.invoice_id.id,
            "view_mode": "form",
            "target": "current",
        }



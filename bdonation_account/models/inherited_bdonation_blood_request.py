from odoo import models, Command


class InheritedBdonationBloodRequest(models.Model):
    _inherit ="bdonation.blood.request"


    def action_create_invoice(self):

        for request in self:
           request.env["account.move"].sudo().create(
                {
                    
                    "move_type":"out_invoice",
                    "invoice_line_ids":[
                        Command.create(
                            { 
                                "name" : request.component_type,
                                "quantity": request.num_records_requested,
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

        return True



from odoo import fields, models

class bdonationBloodRequest(models.Model):
    _name = "bdonation.blood.request"
    _description = "Request Blood"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = "hospital"

    patient_name = fields.Char(required=True, string="Patient Name")
    blood_group_id  = fields.Many2one('bdonation.blood.group', string='Blood Group')
    hospital = fields.Char(required=True, string="Hospital's Name")
    urgency = fields.Selection(
        [
        ('urgent', 'Urgent'),
        ('normal', 'Normal'),
        ('month_later', 'After a month')
        ],
        string='Urgency', default='normal'
    )
#     state = fields.Selection([
#         ('new', 'New'),
#         ('approved', 'Approved'),
#         ('assign_record_to_request', 'Assign Record to Request'),
#         ('complete_request', 'Complete Request'),
#     ], string='Status', default='new')

    quantity_req = fields.Float(string="Blood Quantity Required (ml)", required=True)
#     product_type = fields.Selection([
#         ('whole_blood', 'Whole Blood'),
#         ('plasma', 'Plasma'),
#         ('rbc', 'Red Blood Cells (RBC)'),
#         ('platelets', 'Platelets'),
#     ], string='Product Type', required=True)
#     num_records_requested = fields.Integer(string='Number of Records Requested', required=True)
    




#     from odoo import models, fields, api

# class BloodProductRequest(models.Model):
#     _name = 'bdonation.product.request'
#     _description = 'Blood Product Request'

#     customer_name = fields.Char(string='Customer Name', required=True)
#     contact_number = fields.Char(string='Contact Number', required=True)
#     email_address = fields.Char(string='Email Address')
#     product_type = fields.Selection([
#         ('whole_blood', 'Whole Blood'),
#         ('plasma', 'Plasma'),
#         ('rbc', 'Red Blood Cells (RBC)'),
#         ('platelets', 'Platelets'),
#     ], string='Product Type', required=True)
#     num_records_requested = fields.Integer(string='Number of Records Requested', required=True)
#     request_date = fields.Datetime(string='Request Date', default=fields.Datetime.now)
#     state = fields.Selection([
#         ('new', 'New'),
#         ('approved', 'Approved'),
#         ('assign_record_to_ship', 'Assign Record to Ship'),
#         ('complete_request', 'Complete Request'),
#     ], string='Status', default='new')

#     # Add a Many2many field to link the request with selected records
#     selected_records = fields.Many2many('bdonation.record', string='Selected Records')

#     # ... other fields and methods ...
















    # def generate_quotation(self):
    #     if not self.category_id:
    #         return

    #     quotation_values = {
    #         "partner_id": self.customer_id.id,
    #         "partner_invoice_id": self.customer_id.id,
    #         "partner_shipping_id": self.customer_id.id,
    #         "order_line": [
    #             (
    #                 0,
    #                 0,
    #                 {
    #                     "product_id": self.category_id.id,
    #                     "name": self.category_id.name,
    #                     "price_unit": self.category_id.price,
    #                     "product_uom_qty": 1,
    #                     "display_type": None,
    #                 },
    #             )
    #         ],
    #     }

    #     quotation = self.env["sale.order"].create(quotation_values)

    #     return {
    #         "type": "ir.actions.act_window",
    #         "name": "Quotation",
    #         "res_model": "sale.order",
    #         "res_id": quotation.id,
    #         "view_mode": "form",
    #         "target": "current",
    #     }


        # def action_confirm_request(self):
        #     for request in self:
        #     # Ensure the request is in a pending state before confirming
        #     if request.request_status == 'pending':
        #         # Update the request status to approved
        #         request.write({'request_status': 'approved'})

        #         # Create a sales order
        #         sale_order = self.env['sale.order'].create({
        #             'partner_id': self.env.user.partner_id.id,  # Replace with the actual partner ID
        #             'order_line': [(0, 0, {
        #                 'product_id': request.blood_group_id.product_id.id,  # Replace with the actual product ID
        #                 'product_uom_qty': request.quantity_required,
        #                 'price_unit': 0.0,  # You can set the price accordingly
        #             })]
        #         })

        #         # Link the sales order to the blood donation request
        #         request.write({'order_id': sale_order.id})

        #         # Open the sales order view
        #         action = self.env.ref('sale.action_orders').read()[0]
        #         action['views'] = [(self.env.ref('sale.view_order_form').id, 'form')]
        #         action['res_id'] = sale_order.id
        #         return action
        #     else:
        #         raise UserError('The request is not in a pending state.')

        # return True


        



        # def action_confirm_request(self):
        #     for request in self:
        #         # Ensure the request is in a pending state before confirming
        #         if request.request_status == 'pending':
        #             # Update the request status to approved
        #             request.write({'request_status': 'approved'})
        
        #             # Create a sales order
        #             sale_order = self.env['sale.order'].create({
        #                 'partner_id': self.env.user.partner_id.id,  # Replace with the actual partner ID
        #                 'order_line': [(0, 0, {
        #                     'product_id': request.blood_group_id.product_id.id,  # Replace with the actual product ID
        #                     'product_uom_qty': request.quantity_required,
        #                     'price_unit': 0.0,  # You can set the price accordingly
        #                 })]
        #             })
        
        #             # Link the sales order to the blood donation request
        #             request.write({'order_id': sale_order.id})
        
        #             # Open the sales order view
        #             action = self.env.ref('sale.action_orders').read()[0]
        #             action['views'] = [(self.env.ref('sale.view_order_form').id, 'form')]
        #             action['res_id'] = sale_order.id
        #             return action
        #         else:
        #             raise UserError('The request is not in a pending state.')
        
        #     return self.env['bdonation.blood.request'].browse(self._context.get('active_ids')).action_view_sales_order()
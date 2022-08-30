# from odoo import models, fields, api
#
# class ActionCustom(models.TransientModel):
#     _name = "action.custom"
#     _description = "Action Custom"
#
#     action_id = fields.Many2one('update.custom')
#     prod_id = fields.Many2one('product.template', string='Product')
#     quant = fields.Float(string='Quantity')
#     price_unit = fields.Float(string='Unit Price')
#     tax_ids = fields.Many2many(string='Taxes')
#     price_subtotal = fields.Float(string='Subtotal')
#
#     # def my_button(self):
#     #     return {
#     #         'name': "Done",
#     #         'type': 'ir.actions.act_window',
#     #         'view_type': 'form',
#     #         'view_mode': 'form',
#     #         'res_model': 'object',
#     #         'view_id': self.env.ref('custom.update_custom_form').id,
#     #         'target': 'new',
#     #         'context': {'default_product_id': self.prod_id, 'default_quantity': self.quant, 'default_price_unit': self.price_unit,
#     #                     'default_tax_ids': self.tax_ids, 'default_price_subtotal': self.price_subtotal}
#     #     }
#
#     # @api.onchange(''):
#     # def _onchange_product(self):
#     #     self.

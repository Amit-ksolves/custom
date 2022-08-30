from odoo import models, fields, api


class SaleOrder(models.Model):
    _inherit = "sale.order"

    custom_lines = fields.One2many('custom.order.line', 'custom_id')
    partner_id = fields.Many2one('res.partner')

    # sample_lines = fields.One2many('wiz.sale.order.line', 'sample_id')

    def action_confirm(self):
        for rec in self:
            # company = self.env['sale.order'].search([])
            # print('companies---', company)
            #
            # browse_result = self.env['sale.order'].browse
            # print('browse_result---', browse_result)
            # # if browse_result.exists():
            #     print("Existing")
            # else:
            #     print("NOOOOOO")
            vals = {
                'name': 'S03687',
                'partner_id': '8542'}
            create_record = self.env['sale.order'].create(vals)
            print('create_record---', create_record)

class CustomOrderLine(models.Model):
    _name = "custom.order.line"
    _description = "Custom Order Line"

    # @api.model
    # def default_get_order(self, fields):
    #     res = super(CustomOrderLine, self).default_get_order(fields)
    #     active_id = self._context.get('active_id')
    #
    #     if active_id:
    #         sale_id = self.env['wiz.sale.order'].browse(active_id)
    #         lst = []
    #
    #         for rec in sale_id.wiz_sale_lines:
    #             lst.append((0, 0, {'product_id': rec.product_id.id, 'name': rec.name, 'quantity': rec.quantity,
    #                                'price_unit': rec.price_unit}))
    #
    #         res['custom_lines'] = lst
    #     return res

    name = fields.Text(string='Description')
    custom_id = fields.Many2one('sale.order')

    sample_ids = fields.One2many('wiz.sale.order.line', 'sample_id')

    product_id = fields.Many2one('product.template', string='Product')
    quantity = fields.Float(string='Quantity')
    price_unit = fields.Float(string='Unit Price')
    tax_ids = fields.Many2many('account.tax', string='Taxes')
    price_subtotal = fields.Float(string='Subtotal')

    # sample_lines = fields.One2many('wiz.sale.order.line', 'sample_id')

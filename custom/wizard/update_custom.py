from odoo import models, fields, api


class WizSaleOrder(models.TransientModel):
    _name = "wiz.sale.order"
    _description = "Wiz Sale Order"

    wiz_sale_lines = fields.One2many('wiz.sale.order.line', 'wize_sale_order_id', string='Lines')
    state = fields.Selection([('done', 'Sales Done'), ('cancel', 'Cancelled')], string='Status', readonly=True)

    @api.model
    def default_get(self, fields):
        res = super(WizSaleOrder, self).default_get(fields)
        active_id = self._context.get('active_id')

        if active_id:
            sale_id = self.env['sale.order'].browse(active_id)
            lst = []

            for rec in sale_id.order_line:
                lst.append((0, 0, {'product_id': rec.product_id.id, 'name': rec.name, 'quantity': rec.product_uom_qty,
                                   'price_unit': rec.price_unit}))

            res['wiz_sale_lines'] = lst
        return res



    def action_done(self):
        for order in self:
            tx = order.sudo().wiz_sale_lines
            # print(order.wiz_sale_lines, "---------------------")
            active_id = self._context.get('active_id')
            if active_id:
                sale_id = self.env['wiz.sale.order'].browse(active_id)
                lst = []
                # print("---tttt", sale_id)

                for rec in order.wiz_sale_lines:
                    lst.append(
                        (0, 0, {'product_id': rec.product_id.id, 'name': rec.name, 'quantity': rec.quantity,
                                'price_unit': rec.price_unit}))

                # res['custom_lines'] = lst
        return self.write({'state': 'done'})

    def action_cancel(self):
        self.state = 'cancel'

class WizSaleOrderLine(models.TransientModel):
    _name = "wiz.sale.order.line"
    _description = "Wiz Sale Order Line"

    name = fields.Text(string='Description')
    wize_sale_order_id = fields.Many2one('wiz.sale.order')

    sample_id = fields.Many2one('custom.order.line')
    product_id = fields.Many2one('product.template', string='Product')
    quantity = fields.Integer(string='Quantity')
    price_unit = fields.Float(string='Unit Price')
    tax_ids = fields.Many2many('account.tax', string='Taxes')
    price_subtotal = fields.Float(string='Subtotal')


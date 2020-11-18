# -*- coding: utf-8 -*-

from odoo import models, fields, api

class StockQuant(models.Model):
    _inherit = 'stock.quant'

    stock_min = fields.Float(
        string='Stock Mínimo',related="product_id.product_tmpl_id.reordering_min_qty",store=True,
        required=False)
    stock_max = fields.Float(
        string='Stock Máximo',related="product_id.product_tmpl_id.reordering_max_qty",store=True,
        required=False)
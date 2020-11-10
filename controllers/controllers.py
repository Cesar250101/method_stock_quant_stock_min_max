# -*- coding: utf-8 -*-
from odoo import http

# class Extra-addons/methodStockQuantStockMinMax(http.Controller):
#     @http.route('/extra-addons/method_stock_quant_stock_min_max/extra-addons/method_stock_quant_stock_min_max/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/extra-addons/method_stock_quant_stock_min_max/extra-addons/method_stock_quant_stock_min_max/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('extra-addons/method_stock_quant_stock_min_max.listing', {
#             'root': '/extra-addons/method_stock_quant_stock_min_max/extra-addons/method_stock_quant_stock_min_max',
#             'objects': http.request.env['extra-addons/method_stock_quant_stock_min_max.extra-addons/method_stock_quant_stock_min_max'].search([]),
#         })

#     @http.route('/extra-addons/method_stock_quant_stock_min_max/extra-addons/method_stock_quant_stock_min_max/objects/<model("extra-addons/method_stock_quant_stock_min_max.extra-addons/method_stock_quant_stock_min_max"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('extra-addons/method_stock_quant_stock_min_max.object', {
#             'object': obj
#         })
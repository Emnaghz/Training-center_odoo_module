# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request


# class Signup(http.Controller):
#     @http.route('/signup', auth='public', website=True)
#     def test_controller(self, **kw):
#         # return "Hello, world"
#         return http.request.render('test_module.signup_layout', {})

#     @http.route('/claim', auth='public', website=True)
#     def navigate_to_another_page(self, **kw):
#         # return "Hello, world"
#         return http.request.render('test_module.signup_layout', {})

# class TestModule(http.Controller):
#     @http.route('/test_module/test_module', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/test_module/test_module/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('test_module.listing', {
#             'root': '/test_module/test_module',
#             'objects': http.request.env['test_module.test_module'].search([]),
#         })

#     @http.route('/test_module/test_module/objects/<model("test_module.test_module"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('test_module.object', {
#             'object': obj
#         })

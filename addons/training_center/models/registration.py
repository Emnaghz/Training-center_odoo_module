from odoo import fields, models

class Registration(models.Model):
    _name = 'registration.registration'
    _description = 'Registration'

    name = fields.Char(string="Full Name")
    email = fields.Char(string="Email")
    phone = fields.Char(string="Phone Number")
    cin = fields.Char(string="CIN")
    start_date = fields.Date(string="Start Date")
    end_date = fields.Date(string="End Date")

    # Fix Many2one reference (should be singular)
    module_id = fields.Many2one("module.module", string="Registered Module")

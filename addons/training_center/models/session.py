from odoo import fields, models, api


class Session(models.Model):
    _name = 'session.session'
    _description = 'Session'

    name = fields.Char(string="name")
    code = fields.Char(string="code")
    start_date = fields.Date(string="Start Date")
    end_date = fields.Date(string="End Date")
    description = fields.Text(sring="Description")

    year_id = fields.Many2one("year.year", string="Year", required=False, )

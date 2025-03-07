from odoo import fields, models, api
from datetime import datetime

from odoo.exceptions import UserError


class Claim(models.Model):
    _name = 'claim.claim'
    _description = 'Claims'
    _inherit = ["mail.thread"]

    name = fields.Char(string="Subject", tracking=True, default="Claim")
    code = fields.Char(string="code", tracking=True, default = lambda x:x.env['ir.sequence'].get('claim.claim'))
    start_date = fields.Date(string="Created at", tracking=True)
    end_date = fields.Date(string="Close Date", tracking=True)
    state = fields.Selection([('new', "Nouvelle"), ('draft', "Corbeille"), ('valid', "Validé"), ('done', "Done"),("cancel", "Annulé")], default='new')
    description = fields.Text(sring="Description", tracking=True)
    user_id = fields.Many2one("res.users", string="Created By", default=lambda self: self.env.user)
    priority = fields.Selection([('0', 'Normal'), ('1', 'Low'), ('2', 'Hight'), ('3', 'Very Hight')], string='Priorité')
    module_id = fields.Many2one("module.module", string="Is the claim related to any module? if YES select it:")

    @api.model
    def create(self, values):
        values["user_id"] = self.env.user.id
        values["start_date"] = fields.Date.today()
        return super().create(values)
    
    @api.model
    def _search(self, args, offset=0, limit=None, order=None, count=False):
        user = self.env.user
        if user.is_teacher:
            args.append(('user_id', '=', user.id))
        return super(Claim, self)._search(args, offset, limit, order, count)


    def unlink(self):
        for record in self:
            if record.state in 'done,cancel':
                raise UserError('You cannot delete records in done state.')
        res = super(Claim, self).unlink()
        return res

    def action_validate(self, values):
        print("button clicked")
        self.state = 'valid'

    def action_done(self, values):
        values["end_date"] = datetime.today()
        self.state = 'done'

    def action_cancel(self):
        self.state = 'cancel'

    def action_draft(self):
        self.state = 'draft'
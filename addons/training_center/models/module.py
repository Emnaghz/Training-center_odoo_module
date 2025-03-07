from odoo import fields, models, api

class Module(models.Model):
    _name = 'module.module'
    _description = 'Modules'

    name = fields.Char(string="Name")
    code = fields.Char(
        string="Code",
        tracking=True,
        default=lambda x: x.env['ir.sequence'].next_by_code('module.module')
    )
    description = fields.Text(string="Description")
    level_id = fields.Many2one("level.level", string="Level")  # Correct Many2one relation
    teacher_id = fields.Many2one(
        "res.users",
        string="Teacher",
        domain=[('is_teacher', '=', True)]
    )
    nbr_hour = fields.Integer(string="Number of Hours")
    active = fields.Boolean(string="Active", default=True)

    registrations = fields.One2many("registration.registration", "module_id", string="Associated Registrations")
    nbr_registrations = fields.Integer(compute="_compute_registration", string="# Registrations")

    claim_ids = fields.One2many("claim.claim", "module_id", string="Related Claims")
    nbr_claims = fields.Integer(compute="_compute_claim", string="# Claims")

    @api.depends('claim_ids')
    def _compute_claim(self):
        for module in self:
            module.nbr_claims = len(module.claim_ids)

    @api.depends('registrations')
    def _compute_registration(self):
        for module in self:
            module.nbr_registrations = len(module.registrations)

    def action_open_registrations(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Registrations',
            'res_model': 'registration.registration',
            'domain': [('module_id', 'in', self.ids)],  # Fixed domain for batch processing
            'view_mode': 'tree,form',
            'target': 'current',
        }

    def action_open_claims(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Claims',
            'res_model': 'claim.claim',
            'domain': [('module_id', 'in', self.ids)],  # Fixed domain for batch processing
            'view_mode': 'tree,form',
            'target': 'current',
        }
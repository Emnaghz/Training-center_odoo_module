from odoo import fields, models, api

class Level(models.Model):
    _name = 'level.level'
    _description = 'Levels'

    name = fields.Char(string="Name")
    code = fields.Char(string="Code", tracking=True, default=lambda x: x.env['ir.sequence'].next_by_code('level.level'))
    description = fields.Text(string="Description")  # Fixed typo
    module_ids = fields.One2many("module.module", "level_id", string="Modules")
    nbr_modules = fields.Integer(compute="_compute_modules", string="# Modules")

    @api.depends('module_ids')
    def _compute_modules(self):
        for level in self:
            level.nbr_modules = len(level.module_ids)

    def action_open_modules(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Modules',
            'res_model': 'module.module',  # Fixed model name
            'domain': [('level_id', '=', self.id)],  # Fixed domain filter
            'view_mode': 'tree,form',
            'target': 'current',
        }
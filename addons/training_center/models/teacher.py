from odoo import fields, models, api, _
from odoo.exceptions import ValidationError, UserError
import string
import random


class Teachers(models.Model):
    _inherit = 'res.users'
    _description = 'Description'

    is_teacher = fields.Boolean(string="Is a Teacher", default=False)

    @api.model
    def create(self, vals):
        """Automatically set is_teacher to True if a teacher is being created."""
        if vals.get('is_teacher', False):
            vals['is_teacher'] = True
        return super(Teachers, self).create(vals)
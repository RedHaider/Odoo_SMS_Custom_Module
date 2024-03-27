from odoo import api, fields, models, _
from odoo.exceptions import ValidationError

class SchoolRoom(models.Model):
    _name = 'school.room'
    _description = 'School Information'

    name = fields.Char(string='Room Number', required=True)
    room_id = fields.Char(string='Room Id', readonly= True, copy=False)
    capacity = fields.Integer(string='Capacity')

    @api.model
    def create(self, vals):
        if vals.get('room_id', _('New')) == _('New'):
            vals['room_id'] = self.env['ir.sequence'].next_by_code('school.room.sequence') or _('New')
        return super(SchoolRoom, self).create(vals)
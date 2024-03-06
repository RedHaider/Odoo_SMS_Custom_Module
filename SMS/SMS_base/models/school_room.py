from odoo import api, fields, models, _
from odoo.exceptions import ValidationError

class SchoolRoom(models.Model):
    _name = 'school.room'
    _description = 'School Information'

    name = fields.Char(string='Room Number', required=True)
    room_id = fields.Char(string='Room Id')
    capacity = fields.Integer(string='Capacity')
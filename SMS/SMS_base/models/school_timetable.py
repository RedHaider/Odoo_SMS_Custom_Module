from odoo import api, fields, models, _
from odoo.exceptions import ValidationError

class SchoolTimeTable(models.Model):
    _name = 'school.time_table'
    _description = 'School Time Table'

    name = fields.Char(string='Period Name', required=True)
    time_table_id = fields.Char(string='Time Table ID', required=True)
    start_time = fields.Char(string='From', required=True)
    end_time = fields.Char(string='To', required=True)
    duration = fields.Float(string='Duration', required=True)
    am_pm = fields.Selection([
        ('AM', 'AM'),
        ('PM', 'PM')
    ], string='AM/PM', default='AM', required=True)

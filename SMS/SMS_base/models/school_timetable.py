from odoo import api, fields, models, _
from odoo.exceptions import ValidationError

class SchoolTimeTable(models.Model):
    _name = 'school.time_table'
    _description = 'School Time Table'

    name = fields.Char(string='Period Name', required=True)
    time_table_id = fields.Char(string='Time Table ID',copy=False, readonly=True)
    start_time = fields.Char(string="From" , required=True)
    end_time = fields.Char(string='To', required=True)
    time_table = fields.Char(string='Time',readonly=True, compute='_compute_name', store=True )




    #this field is hidden from xml
    duration = fields.Float(string='Duration')
    am_pm = fields.Selection([
        ('AM', 'AM'),
        ('PM', 'PM')
    ], string='AM/PM', default='AM')

    @api.depends('start_time', 'end_time')
    def _compute_name(self):
        for time in self:
            time.time_table = "%s - %s" % (time.start_time, time.end_time)

    @api.model
    def create(self, vals):
        if vals.get('time_table_id', _('New')) == _('New'):
            vals['time_table_id'] = self.env['ir.sequence'].next_by_code('school.time.sequence') or _('New')
        return super(SchoolTimeTable, self).create(vals)
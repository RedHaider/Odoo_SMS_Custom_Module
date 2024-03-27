from odoo import api, fields, models, _
from odoo.exceptions import ValidationError

class SchoolSection(models.Model):
    _name = "school.section"
    _description = "Section Information"

    name = fields.Char(string='Section Name', required=True)
    section_id = fields.Char(string="Section ID", readonly=True, copy=False) 
    class_id = fields.Many2one('school.class', string="Class Name") 
    room_id = fields.Many2one('school.room', string="Room Number") 
    teacher_id = fields.Many2one('school.teacher',string="Class Teacher") 
    student_count = fields.Integer(string='Student Number') #Need to calculate the total numbe of students form the system

    sunday_line_ids = fields.Many2many('school.section.line', 'class_line_rel','section_id','line_id', string='Sunday')
    monday_line_ids = fields.Many2many('school.section.line', 'class_line_rel','section_id','line_id', string='Monday')
    tuesday_line_ids = fields.Many2many('school.section.line', 'class_line_rel','section_id','line_id', string='Tuesday')
    wednesday_line_ids = fields.Many2many('school.section.line', 'class_line_rel','section_id','line_id', string='Wednesday')
    thursday_line_ids = fields.Many2many('school.section.line', 'class_line_rel','section_id','line_id', string='Thursday')
    friday_line_ids = fields.Many2many('school.section.line', 'class_line_rel','section_id','line_id', string='Friday')
    saturday_line_ids = fields.Many2many('school.section.line', 'class_line_rel','section_id','line_id', string='Saturday')

    @api.model
    def create(self, vals):
        if vals.get('section_id', _('New')) == _('New'):
            vals['section_id'] = self.env['ir.sequence'].next_by_code('school.section.sequence') or _('New')
        return super(SchoolSection, self).create(vals)

    #this field is not being used
    section_line_ids = fields.One2many('school.section.line', 'section_id', string='Class Lines')    

class SchoolClassLine(models.Model):
    _name = "school.section.line"
    _description = "Routine"

    name = fields.Char(string='Period Name', required=True)
    teacher_id = fields.Many2one('school.teacher', string='Subject Teacher')
    subject_id = fields.Many2one('school.subject', string='Subject Name')
    time = fields.Many2one('school.time_table', string='Time', required=True)

    #this field is not used
    week_id = fields.Char(string='subject_list_id', )
    section_id = fields.Many2one('school.section', string='Section')
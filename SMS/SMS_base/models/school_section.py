from odoo import api, fields, models, _
from odoo.exceptions import ValidationError

class SchoolSection(models.Model):
    _name = "school.section"
    _description = "Section Information"

    name = fields.Char(string='Section Name', required=True)
    section_id = fields.Char(string="Section ID") 
    class_id = fields.Char(string="Class Name") #need to change many  to one with school.class
    room_id = fields.Char(string="Room Number") #need to make room table
    teacher_id = fields.Char(string="Teacher Name") #Need to change many to one with school.teacher
    student_count = fields.Integer(string='Student Number') #Need to calculate the total numbe of students form the system



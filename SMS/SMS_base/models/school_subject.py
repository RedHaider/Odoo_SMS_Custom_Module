from odoo import api, fields, models, _
from odoo.exceptions import ValidationError

class SchoolSubject(models.Model):
    _name = 'school.subject'
    _description = 'Schoool Information'

    name = fields.Char(string="Subject Name")
    subject_id = fields.Char(string='Subject Id') #need to figure out for making it automated
    description = fields.Char(string='Book Description')
    class_id = fields.Char(string='Class Name') #need to make it many2one with class
    book_id = fields.Char(string='Book Name') #Need to make it many to one with school.book
    subject_type = fields.Selection([
        ('theory', 'Theory'),
        ('practical', 'Practical')
    ], string='Type', default='theory')
    active = fields.Boolean(string='Active' , default=True)
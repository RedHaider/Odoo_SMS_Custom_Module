from odoo import api, fields, models, _
from odoo.exceptions import ValidationError

class SchoolSection(models.Model):
    _name = "school.class"
    _description = "Class Information"

    name = fields.Char(string='Class Name', required=True)
    class_id = fields.Char(string="Class ID")
    grade = fields.Char(string="Grade")
    active = fields.Boolean(string='Active', default=True)
    admin_id = fields.Char(string = 'Admin Of the Class') #Need to figure out this

    
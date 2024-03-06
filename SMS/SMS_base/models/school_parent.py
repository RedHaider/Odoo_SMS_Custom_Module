from odoo import api, fields, models, _
from odoo.exceptions import ValidationError

class SchoolParent(models.Model):
    _name = 'school.parent'
    _description = 'Parent Information'

    name = fields.Char(string= 'Parent Name', required=True)
    parent_image = fields.Binary(string='Parent Image')

    name = fields.Char(string='Name')
    parent_image = fields.Binary(string='parent Image')
    parent_id = fields.Char(string='Parent Id')
    first_name = fields.Char(string='First Name')
    last_name = fields.Char(string='Lst Name')
    nid_number = fields.Char(string='NID Number')
    relation = fields.Char(string='Relation')
    dob = fields.Date(string='Date of Birth')
    contact_number = fields.Char(string='Contact Number')
    student_id = fields.Char(string='Student Name') #need to be many to many to one with schood.student
    language = fields.Char(string='Language')
    gender = fields.Selection([('male','Male'),('female','Female'),('other','Other')], string='Gender')
    address = fields.Text(string='Address')
    nationality = fields.Char(string='Nationality')
    email = fields.Char(string='Email')
    partner_user = fields.Char(string='Partner Id') #needs to be configure later
    
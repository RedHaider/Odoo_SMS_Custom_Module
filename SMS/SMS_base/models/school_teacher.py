from odoo import api, fields, models, _
from odoo.exceptions import ValidationError

class SchoolTeacher(models.Model):
    _name = 'school.teacher'
    _description = 'Teacher Information'

    name = fields.Char(string='Teacher Name', required=True)
    teacher_image = fields.Binary(string='Teacher Image')
    teacher_id = fields.Char(string='Teacher ID')
    first_name = fields.Char(string='First Name')
    last_name = fields.Char(string='Last Name')
    id_card_number = fields.Char(string='ID Card Number')
    active = fields.Boolean(string='Active', default=True)
    language = fields.Char(string='Language')
    gender = fields.Selection([('male', 'Male'), ('female', 'Female'), ('other', 'Other')],
                              string='Gender')
    dob = fields.Date(string='Date of Birth')
    section_id = fields.Char(string='Section') #needed to be many to one with section table
    specialization = fields.Char(string='Specialization')
    contact_number = fields.Char(string='Contact Number')
    address = fields.Text(string='Address')
    email = fields.Char(string='Email')
    nationality = fields.Char(string='Nationality')
    emergency_contact = fields.Char(string='Emergency Contact')
    relation = fields.Char(string='Relation')
    partner_user = fields.Char( string='Partner User') #configured next

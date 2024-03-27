from odoo import models, fields

class Librarian(models.Model):
    _name = "library.librarian"
    _description = "Librarian Information"

    name = fields.Char(string='Name', required=True)
    librarian_image = fields.Binary(string='Librarian Image')
    lib_id = fields.Char(string='Library ID', required=True)
    first_name = fields.Char(string='First Name')
    last_name = fields.Char(string='Last Name')
    nid_number = fields.Char(string='NID Number')
    is_student = fields.Boolean(string='Is Student')
    dob = fields.Date(string='Date of Birth')
    gender = fields.Selection([('male', 'Male'), ('female', 'Female'), ('other', 'Other')], string='Gender')
    address = fields.Text(string='Address')
    nationality = fields.Char(string='Nationality')
    contact_number = fields.Char(string='Contact Number')
    partner_user = fields.Many2one('res.users', string='User')

from odoo import api, fields, models, _
from odoo.exceptions import ValidationError

class SchoolTeacher(models.Model):
    _name = 'school.teacher'
    _description = 'Teacher Information'

    name = fields.Char(string='Teacher Name',readonly=True, compute='_compute_name', store=True )
    teacher_image = fields.Binary(string='Teacher Image')
    teacher_id = fields.Char(string='Teacher ID', copy=False, readonly=True)
    first_name = fields.Char(string='First Name')
    last_name = fields.Char(string='Last Name')
    id_card_number = fields.Char(string='ID Card Number')
    active = fields.Boolean(string='Active', default=True)
    language = fields.Char(string='Language')
    gender = fields.Selection([('male', 'Male'), ('female', 'Female'), ('other', 'Other')],
                              string='Gender')
    dob = fields.Date(string='Date of Birth')
    section_id = fields.Many2one('school.section', string='Section')
    specialization = fields.Char(string='Specialization')
    contact_number = fields.Char(string='Contact Number')
    address = fields.Text(string='Address')
    email = fields.Char(string='Email')
    nationality = fields.Char(string='Nationality')
    emergency_contact = fields.Char(string='Emergency Contact')
    relation = fields.Char(string='Relation')
    partner_user = fields.Many2one('res.partner', string='Partner User') #configured next

    @api.depends('first_name','last_name')
    def _compute_name(self):
        for teacher in self:
            teacher.name = "%s %s" % (teacher.first_name, teacher.last_name)
    
    @api.model
    def create(self, vals):
        if vals.get('teacher_id', _('New')) == _('New'):
            vals['teacher_id'] = self.env['ir.sequence'].next_by_code('school.teacher.sequence') or _('New')
        return super(SchoolTeacher, self).create(vals)
from odoo import api, fields, models, _
from odoo.exceptions import ValidationError

class SchoolStudent(models.Model):
    _name = "school.student"
    _description = "Student Information"

    name = fields.Char(string="Student Name", compute='_compute_name', store=True)
    student_image = fields.Binary(string="Student Image", attachment=True)
    student_id = fields.Char(string="Student Id" , readonly=True, copy=False)
    first_name = fields.Char(string="First Name")
    last_name = fields.Char(string="Last Name")
    id_card_number = fields.Char(string="ID Card Number")
    active = fields.Boolean(string='Active', default=True)
    language = fields.Char(string="Language")
    gender = fields.Selection([('make','Male'),('female','Female'),('other','Other')],string = 'Gender')
    roll_no = fields.Char(string="Roll Number")
    dob =  fields.Date(string='Date of Birth')
    class_id = fields.Many2one('school.class',string="Class") 
    section_id = fields.Many2one('school.section',string="Section") 
    address = fields.Text(string="Address")
    contact_number = fields.Char(string="Contact Number")
    parent_id = fields.Many2one('school.parent',string="Parent Name") 
    nationality = fields.Char(string = "Nationality")
    email = fields.Char(string="Email")
    category = fields.Char(string="Category") #needed to be figured out
    emergency_contact = fields.Char(string = "Emergency Contact")
    partner_user = fields.Many2one('res.partner',string="Partner User") #can be configured through chat gtp, check saves codes
    

    @api.depends('first_name','last_name')
    def _compute_name(self):
        for student in self:
            student.name = "%s %s" % (student.first_name, student.last_name)
    
    @api.model
    def create(self, vals):
        if vals.get('student_id', _('New')) == _('New'):
            vals['student_id'] = self.env['ir.sequence'].next_by_code('school.student.sequence') or _('New')
        return super(SchoolStudent, self).create(vals)

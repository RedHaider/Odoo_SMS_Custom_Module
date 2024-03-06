from odoo import api, fields, models, _
from odoo.exceptions import ValidationError

class SchoolStudent(models.Model):
    _name = "school.student"
    _description = "Student Information"

    name = fields.Char(string="Student Name", compute='_compute_name', store=True)
    student_image = fields.Binary(string="Student Image", attachment=True)
    student_id = fields.Char(string="Student Id")
    student_image = fields.Binary(string="Student Image", attachment=True)
    first_name = fields.Char(string="First Name")
    last_name = fields.Char(string="Last Name")
    id_card_number = fields.Char(string="ID Card Number")
    active = fields.Boolean(string='Active', default=True)
    language = fields.Char(string="Language")
    gender = fields.Selection([('make','Male'),('female','Female'),('other','Other')],string = 'Gender')
    roll_no = fields.Char(string="Roll Number")
    dob =  fields.Date(string='Date of Birth')
    class_id = fields.Char(string="Class") #should be many to one with class model
    section_id = fields.Char(string="Section") #should be many to one with section model
    address = fields.Text(string="Address")
    contact_number = fields.Char(string="Contact Number")
    parent_id = fields.Char(string="Parent Name") #shoudl be many to one with parent class
    nationality = fields.Char(string = "Nationality")
    email = fields.Char(string="Email")
    category = fields.Char(string="Category") #needed to be figured out
    emergency_contact = fields.Char(string = "Emergency Contact")
    partner_user = fields.Char(string="Partner User") #can be configured through chat gtp, check saves codes
    
 
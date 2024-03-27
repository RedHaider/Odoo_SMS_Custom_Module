from odoo import api, fields, models, _
from odoo.exceptions import ValidationError

class SchoolClass(models.Model):
    _name = "school.class"
    _description = "Class Information"

    name = fields.Char(string='Class Name', required=True)
    class_id = fields.Char(string="Class ID", readonly=True, copy=False)
    grade = fields.Char(string="Grade")
    active = fields.Boolean(string='Active', default=True)
    admin_id = fields.Char(string = 'Class Admin') #Need to figure out this

    class_line_ids = fields.One2many('school.class.line', 'class_id' , string='Class Lines')
 
    @api.model
    def create(self, vals):
        if vals.get('class_id', _('New')) == _('New'):
            vals['class_id'] = self.env['ir.sequence'].next_by_code('school.class.sequence') or _('New')
        return super(SchoolClass, self).create(vals)    

class SchoolClassLine(models.Model):
    _name = "school.class.line"
    _description = "Class Line Information"

    name = fields.Many2one('school.subject' , string='Subject', required=True)
    suject_list_id = fields.Char(string='ID', required=True)
    book_id = fields.Many2one('library.book',string='Book')
    subject_type = fields.Char(string = 'Type' )
    book_image = fields.Binary(string='Image Book')

    class_id = fields.Many2one('school.class', string='Class')
    
    
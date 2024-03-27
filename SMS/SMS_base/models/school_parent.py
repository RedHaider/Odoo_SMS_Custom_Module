from odoo import api, fields, models, _
from odoo.exceptions import ValidationError

class SchoolParent(models.Model):
    _name = 'school.parent'
    _description = 'Parent Information'

    name = fields.Char(string='Name', compute='_compute_name', store=True , readonly=False )
    parent_image = fields.Binary(string='parent Image')
    parent_id = fields.Char(string='Parent Id', readonly=True, copy=False)
    first_name = fields.Char(string='First Name')
    last_name = fields.Char(string='Lst Name')
    nid_number = fields.Char(string='NID Number')
    relation = fields.Char(string='Relation')
    dob = fields.Date(string='Date of Birth')
    contact_number = fields.Char(string='Contact Number')
    student_id = fields.Many2one('school.student',string='Student Name') #need to be many to many to one with schood.student
    language = fields.Char(string='Language')
    gender = fields.Selection([('male','Male'),('female','Female'),('other','Other')], string='Gender')
    address = fields.Text(string='Address')
    nationality = fields.Char(string='Nationality')
    email = fields.Char(string='Email')
    partner_user = fields.Many2one('res.partner', string='Partner Id') #needs to be configure later
    
    @api.depends('first_name','last_name')
    def _compute_name(self):
        for parent in self:
            parent.name = "%s %s" % (parent.first_name, parent.last_name)
    
    @api.model
    def create(self, vals):
        if vals.get('parent_id', _('New')) == _('New'):
            vals['parent_id'] = self.env['ir.sequence'].next_by_code('school.parent.sequence') or _('New')
        return super(SchoolParent, self).create(vals)
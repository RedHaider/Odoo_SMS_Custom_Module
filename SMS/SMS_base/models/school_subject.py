from odoo import api, fields, models, _
from odoo.exceptions import ValidationError

class SchoolSubject(models.Model):
    _name = 'school.subject'
    _description = 'Schoool Information'

    name = fields.Char(string="Subject Name")
    subject_id = fields.Char(string='Subject Id', readonly=True, copy=False) 
    description = fields.Char(string='Book Description')
    class_id = fields.Many2one('school.class' , string='Class Name') 
    book_id = fields.Many2one('library.book' , string='Book Name') 
    subject_type = fields.Selection([
        ('theory', 'Theory'),
        ('practical', 'Practical')
    ], string='Type', default='theory')
    active = fields.Boolean(string='Active' , default=True)

    @api.model
    def create(self, vals):
        if vals.get('subject_id', _('New')) == _('New'):
            vals['subject_id'] = self.env['ir.sequence'].next_by_code('school.subject.sequence') or _('New')
        return super(SchoolSubject, self).create(vals)
from odoo import api, fields, models, _

class StudentBook(models.Model):
    _name = "library.book"
    _description = "Book Information"

    name = fields.Char(string='Book Name', required=True)
    book_image = fields.Binary(string='Book Image')
    book_id = fields.Char(string='Book Id', copy=False, readonly=True)
    location = fields.Char(string='Location')
    purchased_date = fields.Date(string='Purchased Date')
    active = fields.Boolean(string='Active', default=True)
    book_price = fields.Float(string='Book Price')
    publisher_details = fields.Text(string='Publisher Details')
    edition_details = fields.Char(string='Edition Details')
    language = fields.Char(string='Language')
    penalty_per_day = fields.Float(string='Penalty Per Day')
    academic = fields.Boolean(string='Academic')
    class_id = fields.Many2one('school.class', string='Class')
    available = fields.Boolean(string='Available', default=True)

    @api.model
    def create(self, vals):
        if vals.get('book_id', _('New')) == _('New'):
            vals['book_id'] = self.env['ir.sequence'].next_by_code('library.book.sequence') or _('New')
        return super(StudentBook, self).create(vals)
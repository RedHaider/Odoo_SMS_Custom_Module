from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


class LibraryPractice(models.Model):
    _name = "library.practice"
    _description = "Practice"

    name = fields.Char(string="My Name")
    book_pull = fields.Many2one('library.book', string='Book Name')
    book_image = fields.Binary(string='Book Image', compute='_compute_book_image_new', readonly=True)

    @api.depends('book_pull')
    def _compute_book_image_new(self):
        for record in self:
            if record.book_pull and record.book_pull.book_image:
                record.book_image = record.book_pull.book_image
            else:
                record.book_image = False  


    # @api.onchange('name')
    # def _compute_book_image(self):
    #     for record in self:
    #         if record.name and record.name.book_image:
    #             record.book_image = record.name.book_image
    #         else:
    #             record.book_image = False   
    

 

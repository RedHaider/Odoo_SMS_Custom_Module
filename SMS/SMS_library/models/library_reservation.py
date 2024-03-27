from odoo import api, fields, models, _
from odoo.exceptions import ValidationError
from datetime import timedelta
from datetime import datetime, timedelta


class ReservationBook(models.Model):
    _name = "library.reservation_book"
    _description = "Book Reservation Information"

    name = fields.Char(string="Book Name", readonly=True, compute='_compute_book_name')
    Select_Book = fields.Many2one('library.book', string='Select Book', required=True)
    bookreservation_id = fields.Char(string='Reservation ID', readonly=True, copy=False)
    reserve_book_id = fields.Char(string='Book Id', copy=False, readonly=True, compute='_compute_book_id' )
    book_image = fields.Binary(string='Book Image',compute='_compute_book_image',readonly=True, store=True)
    issue_date = fields.Date(string='Issue Date')
    return_date = fields.Date(string='Return Date')
    actual_return_date = fields.Date(string='Due Date')
    penalty = fields.Float(string='Penalty', compute='_compute_penalty')
    location = fields.Char(string='Location', compute='_compute_location', store=True)
    student_id = fields.Many2one('school.student', string='Student')
    student_id_card = fields.Char(string='Student ID Card', compute='_compute_student_id_card', store=True)
    librarian = fields.Many2one('res.users',string="Librarian",default=lambda self: self.env.user, readonly=True)
    state = fields.Selection([
        ('available', 'Available'),
        ('issue', 'Issue'),
    ], string='State', default='available')

    #assigning the user i librarian
    # @api.model
    # def create(self, vals):
    #     vals['librarian'] = self.env.user.id
    #     return super(BookReservation, self).create(vals)

    #penalty calculation
    @api.depends('return_date','actual_return_date','Select_Book')
    def _compute_penalty(self):
        for record in self:
            if record.return_date and record.actual_return_date:
                if record.return_date > record.actual_return_date:
                    #calculating the penalty
                    days_diff = (record.return_date - record.actual_return_date).days
                    penalty_amount = days_diff*(record.Select_Book.penalty_per_day)
                    record.penalty = penalty_amount
                else:
                    record.penalty = 0.0
            else:
                record.penalty = 0.0

    #this functipn takes student id to auto read student id card
    @api.depends('student_id')
    def _compute_student_id_card(self):
        for record in self:
            record.student_id_card = record.student_id.id_card_number if record.student_id else False
   
    @api.depends('Select_Book')
    def _compute_book_image(self):
        for record in self:
            if record.Select_Book and record.Select_Book.book_image:
                record.book_image = record.Select_Book.book_image
            else:
                record.book_image = False   
       
    @api.depends('Select_Book')
    def _compute_book_name(self):
        for record in self:
            if record.Select_Book and record.Select_Book.name:
                record.name = record.Select_Book.name
            else:
                record.name = False   
    
    @api.depends('Select_Book')
    def _compute_book_id(self):
        for record in self:
            if record.Select_Book and record.Select_Book.book_id:
                record.reserve_book_id = record.Select_Book.book_id
            else:
                record.reserve_book_id = False

    #this function takes book_selection to auto store book location
    @api.depends('Select_Book')
    def _compute_location(self):
        for record in self:
            record.location = record.Select_Book.location if record.Select_Book else False

    #this function generates the bookreservation sequence number automatically  
    @api.model
    def create(self, vals):
        if vals.get('bookreservation_id', _('New')) == _('New'):
            vals['bookreservation_id'] = self.env['ir.sequence'].next_by_code('library.book_reservation.sequence') or _('New')
        return super(ReservationBook, self).create(vals)
    
    def button_current_date_issue(self):
        self.issue_date = fields.Date.today()
        return_date = fields.Date.today()+timedelta(days=3)
        self.actual_return_date = return_date

        # change the state to 'issue'
        self.state='issue'
        if self.Select_Book:
            self.Select_Book.available = False
    
    def button_current_return_date(self):
        self.return_date = fields.Date.today()

        # changing back to availbale
        self.state='available'
        if self.Select_Book:
            self.Select_Book.available = True


 

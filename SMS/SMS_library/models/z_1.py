from odoo import api, fields, models, _
from odoo.exceptions import ValidationError
from datetime import timedelta
from datetime import datetime, timedelta


class BookReservation(models.Model):
    _name = "library.book_reservation"
    _description = "Book Reservation Information"

    name = fields.Many2one('library.book', string='Book Name', required=True)
    #useless field below
    book_selection = fields.Integer( string='Select Your Book', required= False)
    bookreservation_id = fields.Char(string='Reservation ID', readonly=True, copy=False)
    reserve_book_id = fields.Char(string='Book Id', copy=False, readonly=True, compute='_compute_book_id' )
    book_image = fields.Binary(string='Book Image',readonly=False, store=True)
    issue_date = fields.Date(string='Issue Date')
    return_date = fields.Date(string='Return Date')
    actual_return_date = fields.Date(string='Due Date')
    penalty = fields.Float(string='Penalty', compute='_compute_penalty')
    location = fields.Char(string='Location', compute='_compute_location', store=True)
    student_id = fields.Many2one('school.student', string='Student')
    student_id_card = fields.Char(string='Student ID Card', compute='_compute_student_id_card', store=True)
    librarian = fields.Char( string='Librarian')
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
    @api.depends('return_date','actual_return_date','name')
    def _compute_penalty(self):
        for record in self:
            if record.return_date and record.actual_return_date:
                if record.return_date > record.actual_return_date:
                    #calculating the penalty
                    days_diff = (record.return_date - record.actual_return_date).days
                    penalty_amount = days_diff*(record.name.penalty_per_day)
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
   
    @api.depends('name')
    def _compute_book_image(self):
        for record in self:
            if record.name and record.name.book_image:
                record.book_image = record.name.book_image
            else:
                record.book_image = False   
    
    @api.depends('name')
    def _compute_book_id(self):
        for record in self:
            if record.name and record.name.book_id:
                record.reserve_book_id = record.name.book_id
            else:
                record.reserve_book_id = False

    #this function takes book_selection to auto store book location
    @api.depends('name')
    def _compute_location(self):
        for record in self:
            record.location = record.name.location if record.name else False

    #this function generates the bookreservation sequence number automatically  
    @api.model
    def create(self, vals):
        if vals.get('bookreservation_id', _('New')) == _('New'):
            vals['bookreservation_id'] = self.env['ir.sequence'].next_by_code('library.book_reservation.sequence') or _('New')
        return super(BookReservation, self).create(vals)
    
    def button_current_date_issue(self):
        self.issue_date = fields.Date.today()
        return_date = fields.Date.today()+timedelta(days=3)
        self.actual_return_date = return_date

        # change the state to 'issue'
        self.state='issue'
        if self.name:
            self.name.available = False
    
    def button_current_return_date(self):
        self.return_date = fields.Date.today()

        # changing back to availbale
        self.state='available'
        if self.name:
            self.name.available = True


 

from enum import auto
import string
from textwrap import fill
from odoo import api, fields, models


class Workorder(models.Model):
    _name = 'booking.workorder'
    _description = 'object work order'

    booking_order_reference = fields.Many2many(
        comodel_name='sale.order',
        string='Booking Order Reference')
    booking_order_reference = fields.Many2one(
        comodel_name='sale.order',
        string='Booking Order Reference',
        readonly=True)  # auto filled belom
    team_id = fields.Many2one(
        comodel_name='booking.service_team',
        string='Team', required=True)
    team_leader = fields.Many2one(
        comodel_name='res.users',
        string='Team Leader',
        required=True, )
    team_member = fields.Many2many(
        comodel_name='res.users',
        string='Team Member')
    planned_start = fields.Datetime(
        string='Planned Start',
        required=True)
    planned_end = fields.Datetime(
        string='Planned End',
        required=True)
    date_start = fields.Datetime(
        string='Date Start',
        readonly=True)
    date_end = fields.Datetime(
        string='Date End',
        required=True)
    state = fields.Selection(
        string='State',
        selection=[
            ('pending', 'Pending'),
            ('in progress', 'In Progress'),
            ('done', 'Done'),
            ('cancelled', 'Cancelled')])
    notes = fields.Text(string='Notes')

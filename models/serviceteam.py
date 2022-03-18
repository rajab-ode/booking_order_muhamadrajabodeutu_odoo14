from odoo import api, fields, models


class ServiceTeam(models.Model):
    _name = 'booking.serviceteam'
    _description = 'class object service_team'

    team_name = fields.Char(
        string='Team Name',
        required=True)
    team_leader = fields.Many2one(
        comodel_name='res.users',
        string='Team Leader',
        required=True)
    team_member = fields.Many2many(
        comodel_name='res.users',
        string='Team Member')

from odoo import models, fields

class MachineTag(models.Model):
    _name = 'machine.tag'

    name = fields.Char('Name')
    color = fields.Integer('Color Index')


class Machine(models.Model):
    _name = 'machine'

    name = fields.Char('Name')
    tags = fields.Many2many('item.tag', string='Tags')

    overclock = fields.Integer('Overclock')
    amount = fields.Integer('Amount')

    # Recipe
    input = fields.Many2one('item.move', 'Input')
    output = fields.Many2one('item.move', 'Output')
    basetime = fields.Integer('Base time')

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
    input = fields.One2many('item.move', 'machine_input', string='Input')
    output = fields.One2many('item.move', 'machine_output', string='Output')
    basetime = fields.Integer('Base time')

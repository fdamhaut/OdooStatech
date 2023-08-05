from odoo import models, fields

class MachineTag(models.Model):
    _name = 'machine.tag'

    name = fields.Char('Name')
    color = fields.Integer('Color Index')


class Machine(models.Model):
    _name = 'machine'

    name = fields.Char('Name')
    tag_ids = fields.Many2many('item.tag', string='Tags')
    planned = fields.Boolean('Planned', default=False)

    overclock = fields.Integer('Overclock')
    amount = fields.Integer('Amount', default=1)

    # Recipe
    input_ids = fields.One2many('item.move', 'machine_id', 'Inputs')
    output_ids = fields.One2many('item.move', 'machine_id', 'Outputs')
    basetime = fields.Integer('Base time')

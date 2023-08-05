from odoo import models, fields, api

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
    input_ids = fields.One2many('item.move', 'machine_input_id', 'Inputs')
    output_ids = fields.One2many('item.move', 'machine_output_id', 'Outputs')
    basetime = fields.Integer('Base time')

    input_ids_str = fields.Char(compute='_compute_input_ids_str', string='Inputs')
    output_ids_str = fields.Char(compute='_compute_output_ids_str', string='Outputs')

    @api.depends('input_ids')
    def _compute_input_ids_str(self):
        for machine in self:
            machine.input_ids_str = ', '.join(machine.input_ids.mapped('name'))

    @api.depends('output_ids')
    def _compute_output_ids_str(self):
        for machine in self:
            machine.output_ids_str = ', '.join(machine.output_ids.mapped('name'))

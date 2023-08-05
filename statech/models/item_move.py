from odoo import models, fields, api

class ItemMove(models.Model):
    _name = 'item.move'

    item = fields.Many2one('item', 'Item')
    amount = fields.Float('Amount')
    chance = fields.Integer('% Chance')

    machine_input = fields.Many2one('machine', string='Machine')
    machine_output = fields.Many2one('machine', string='Machine')

    # Computed
    real_amount = fields.Float(compute='_compute_real_amount', store=True)

    @api.depends('amount', 'chance')
    def _compute_real_amount(self):
        for im in self:
            im.real_amount = im.amount * im.chance / 100
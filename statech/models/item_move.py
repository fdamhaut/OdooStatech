from odoo import models, fields, api

class ItemMove(models.Model):
    _name = 'item.move'

    machine_id = fields.Many2one('machine')
    item_id = fields.Many2one('item', 'Item')
    amount = fields.Float('Amount')
    chance = fields.Integer('% Chance', default=100)

    # Computed
    real_amount = fields.Float(compute='_compute_real_amount', store=True)

    @api.depends('amount', 'chance')
    def _compute_real_amount(self):
        for im in self:
            im.real_amount = im.amount * im.chance / 100

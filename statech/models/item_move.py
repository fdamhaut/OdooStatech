from odoo import models, fields, api

class ItemMove(models.Model):
    _name = 'item.move'

    item = fields.Many2one('item', 'Item')
    uom = fields.Many2one('uom.uom', 'Unit')
    amount = fields.Float('Amount')
    chance = fields.Integer('% Chance')

    # Computed
    real_amount = fields.Float(compute='_compute_real_amount', store=True)

    @api.depends('amount', 'chance')
    def _compute_real_amount(self):
        for im in self:
            im.real_amount = im.amount * im.chance
from odoo import models, fields, api

class ItemMove(models.Model):
    _name = 'item.move'


    item_id = fields.Many2one('item', 'Item')
    amount = fields.Float('Amount', default=1)
    chance = fields.Integer('% Chance', default=100)
    machine_input_id = fields.Many2one('machine')
    machine_output_id = fields.Many2one('machine')

    # Computed
    real_amount = fields.Float(compute='_compute_real_amount', store=True)
    name = fields.Char(compute="_compute_name")

    @api.depends('amount', 'chance')
    def _compute_real_amount(self):
        for im in self:
            im.real_amount = im.amount * im.chance / 100

    @api.depends('amount', 'chance', 'item_id')
    def _compute_name(self):
        for im in self:
            chance = f'{im.chance}% of ' if im.chance < 100 else ''
            im.name = f'{chance}{im.amount} {im.item_id.name}'

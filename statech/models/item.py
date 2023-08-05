from odoo import models, fields

class ItemTag(models.Model):
    _name = 'item.tag'

    name = fields.Char('Name')
    color = fields.Integer('Color Index')


class Item(models.Model):
    _name = 'item'

    name = fields.Char('Name')
    tag_ids = fields.Many2many('item.tag', string='Tags')

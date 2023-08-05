from odoo import models, fields

class ItemUsageReport(models.Model):
    _name = "item.move.report"
    _description = "Item Usage"
    _order = ''
    _auto = False

    item_id = fields.Many2one('item', string="Item", readonly=True)

    gross_output = fields.Float(string="Gross Output", readonly=True)
    net_output = fields.Float(string="Net Output", readonly=True)
    qty_used = fields.Float(string="Qty Used", readonly=True)


    def _with(self):
        return """
        (
            SELECT  item,
                    real_amount * (machine_input IS NOT NULL)::int AS input
                    real_amount * (machine_output IS NOT NULL)::int AS output
            FROM item_move
        ) AS item_io
        """

    def _select(self):
        return """
            item AS item_id
            SUM(output) AS gross_output
            SUM(input) AS qty_used
            SUM(output) - SUM(input) AS net_output
        """

    def _from(self):
        return """
            item_io
        """

    def _group_by(self):
        return """
            item
        """

    @property
    def _table_query(self):
        return self._query()

    def _query(self):
        return f"""
              WITH {self._with()}
            SELECT {self._select()}
              FROM {self._from()}
          GROUP BY {self._group_by()}
        """
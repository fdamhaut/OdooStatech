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
    planned_gross_output = fields.Float(string="Planned Gross Output", readonly=True)
    planned_net_output = fields.Float(string="Planned Net Output", readonly=True)
    planned_qty_used = fields.Float(string="Planned Quantity Used", readonly=True)


    def _with(self):
        return """
        item_io AS (
            SELECT  item_id,
                    real_amount * (machine_input_id IS NOT NULL)::int AS input,
                    real_amount * (machine_output_id IS NOT NULL)::int AS output,
                    COALSESCE(machine_input_id, machine_output_id) AS machine_id
            FROM item_move
        ),
        machine_time AS (
            SELECT  id,
                    base_time * base_cost / overclock as time,
                    planned
            FROM machine
        ),
        item_io_time AS (
            SELECT  ii.item_id          AS item_id,
                    ii.output / mt.time AS output,
                    ii.input / mt.time  AS input,
                    mt.planned          AS planned,
            FROM item_io ii
            JOIN machine_time mt ON ii.machine_id = mt.id 
        )
        """

    def _select(self):
        return """
            item_id AS id,
            item_id AS item_id,
            SUM(output * (NOT planned)::int) AS gross_output,
            SUM(output) AS planned_gross_output,
            SUM(input * (NOT planned)::int) AS qty_used,
            SUM(input) AS planned_qty_used,
            SUM(output * (NOT planned)::int) - SUM(input * (NOT planned)::int) AS net_output,
            SUM(output) - SUM(input) AS net_output
        """

    def _from(self):
        return """
            item_io_time iit
        """

    def _group_by(self):
        return """
            item_id
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
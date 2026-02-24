from odoo import models, fields, api


class FleetVehicleLogServices(models.Model):
    _inherit = 'fleet.vehicle.log.services'

    bill_id = fields.Many2one('account.move', string="Vendor Bill", readonly=True)
    bill_count = fields.Integer(string="Bill Count", compute="_compute_bill_count")

    def _compute_bill_count(self):
        for record in self:
            record.bill_count = 1 if record.bill_id else 0

    def write(self, vals):
        # 1. First write data to database (via super)
        res = super(FleetVehicleLogServices, self).write(vals)

        # 2. Then check: if state has changed to 'done'
        if vals.get('state') == 'done':
            for record in self:
                if not record.bill_id:
                    record._create_vendor_bill()
        return res

    def _create_vendor_bill(self):
        # self is a single record here (called within a loop)
        self.ensure_one()

        # Must check if Vendor (partner_id) exists, otherwise it will error
        if not self.vendor_id:
            return
        reference = f"Service: {self.vehicle_id.name}"
        if self.service_type_id:
            reference = f"{self.service_type_id.name} - {self.vehicle_id.name}"
        bill_vals = {
            'move_type': 'in_invoice',
            'partner_id': self.vendor_id.id,
            'invoice_date': fields.Date.today(),
            'ref': reference,
            'invoice_line_ids': [(0, 0, {
                'name': f"Service: {self.description or self.service_type_id.name} - {self.vehicle_id.name}",
                'price_unit': self.amount,
                'quantity': 1.0,
            })],
        }
        bill = self.env['account.move'].create(bill_vals)
        self.bill_id = bill.id

    def action_view_bill(self):
        self.ensure_one()
        if self.bill_id:
            return {
                'type': 'ir.actions.act_window',
                'res_model': 'account.move',
                'view_mode': 'form',
                'res_id': self.bill_id.id,
                'target': 'current',
            }
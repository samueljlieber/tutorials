from odoo import fields, models
from odoo.tools import date_utils

class RealEstateOffer(models.Model):
    _name = "real.estate.offer"
    _description = "Real estate offer."

    amount = fields.Float(
        string="Amount",
        required=True
    )
    buyer_id = fields.Many2one(
        string="Buyer",
        comodel_name="res.partner",
        required=True
    )
    date = fields.Date(
        string="Date",
        default=fields.Date.today(),
        required=True
    )
    validity = fields.Integer(
        string="Validity",
        default=7,
        required=True
    )
    state = fields.Selection(
        string="State",
        required=True,
        default="waiting",
        selection=[
            ("waiting","Waiting"),
            ("accepted","Accepted"),
            ("refused","Refused")
        ]
    )
    property_id = fields.Many2one(
        string="Property",
        comodel_name="real.estate.property",
    )

from odoo import fields, models
from odoo.tools import date_utils

class RealEstateTag(models.Model):
    _name = "real.estate.tag"
    _description = "Real estate tag."

    name = fields.Char(
        string="Name",
        required=True
    )
    color = fields.Integer(
        string="Color",
    )
    property_ids = fields.Many2many(
        string="Property",
        comodel_name="real.estate.property"
    )

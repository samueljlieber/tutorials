from odoo import fields, models
from odoo.tools import date_utils

class RealEstatePropertyType(models.Model):
    _name = "real.estate.property.type"
    _description = "Real estate property types."

    name = fields.Char(
        string="Name"
    )


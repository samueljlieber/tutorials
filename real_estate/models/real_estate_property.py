from odoo import fields, models
from odoo.tools import date_utils

class RealEstateProperty(models.Model):
    _name = "real.estate.property"
    _description = "Real estate property management system"

    name = fields.Char(
        string="Title",
        required=True
    )
    description = fields.Text(
        string="Description"
    )
    image = fields.Image(
        string="Image",
        max_width = 600,
        max_height = 400
    )
    active = fields.Boolean(
        string="Active",
        default=True
    )
    state = fields.Selection(
        string="State",
        required=True,
        default="new",
        selection=[
            ("new","New"),
            ("received","Offer Received"),
            ("review","In Review"),
            ("accepted","Accepted")
        ]
    )
    type_id = fields.Many2one(
        string="Type",
        comodel_name="real.estate.property.type",
        ondelete='restrict',
        required=True
    )
    selling_price = fields.Float(
        string="Selling Price",
        required=True,
        help="The price of the property at the time of selling."
    )
    availability_date = fields.Date(
        string="Availability Date",
        default=date_utils.add(fields.Date.today(), months=2)
    )
    floor_area = fields.Float(
        string="Floor Area (sq m)",
        help="The total floor area of the property in square meteres."
    )
    bedrooms = fields.Integer(
        string="Bedrooms",
        default=2
    )
    garden = fields.Boolean(
        string="Garden",
        default=False
    )
    garage = fields.Boolean(
        string="Garage",
        default=False
    )
    seller_id = fields.Many2one(
        string="Seller",
        comodel_name="res.partner",
        default="",
        required=True
    )
    salesperson_id = fields.Many2one(
        string="Salesperson",
        comodel_name="res.users"
    )
    offer_ids = fields.One2many(
        string="Offers",
        comodel_name="real.estate.offer",
        inverse_name="property_id",
    )
    tag_ids = fields.Many2many(
        string="Tags",
        comodel_name="real.estate.tag"
    )

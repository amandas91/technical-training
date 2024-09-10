from odoo import fields, models
from datetime import datetime
from dateutil.relativedelta import relativedelta

class TestModel(models.Model):
    _name = "test.model"
    _description = "Estate Model"

    title = fields.Char(required=True)
    description = fields.Text()
    post_code = fields.Char()
    expected_price = fields.Float()
    bedrooms = fields.Integer(default=2)
    facades = fields.Integer()
    garden = fields.Boolean()
    garden_area = fields.Float()
    active = fields.Boolean(default=False)
    selling_price = fields.Float(default=1000.00, readonly=True, copy=False)
    available_from = fields.Datetime("Avaliable", default=fields.Date.today() + relativedelta(months=3), copy=False)
    living_area = fields.Integer()
    garage = fields.Boolean()
    status = fields.Char()
    
    buyer = fields.Many2one('res.users', copy=False)

    real_estate_property_type_id = fields.Many2one('real.estate.propety.type', string="Property Types")
    res_partner_id = fields.Many2one('res.partner', string="Salesperson")
    tag_ids = fields.Many2many('real.estate.propety.tags', string="Property Tags")

    offer_ids = fields.Many2many('real.estate.propety.offer', string="Property Offers")

class RealEstatePropertyType (models.Model):
    _name = "real.estate.propety.type"
    _description = "the Real Estate Property Type table"

    name = fields.Char(required=True)

class RealEstatePropertyTags (models.Model):
    _name = "real.estate.propety.tags"
    _description = "The Real Estate Property Tags table"

    name = fields.Char(required=True)

class RealEstatePropertyOffer (models.Model):
    _name = "real.estate.propety.offer"
    _description = "The Real Estate Property Offer table"

    price = fields.Float(required=True)

    def _get_estados(self):
        return [
            ('accepted', 'Accepted'),
            ('refused', 'Refused')
        ]

    status = fields.Selection(
        selection='_get_estados', 
        string="Status", 
        default='accepted'
    )
    
    partner_id = fields.Many2one('res.partner', string="Partner")
    property_id = fields.Many2one('test.model', string="Estate Model")
    

    
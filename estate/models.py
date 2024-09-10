from odoo import api, fields, models
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
    garden_orientation = fields.Char()
    garden_area = fields.Float(string="Garden area (sqm)")
    active = fields.Boolean(default=False)
    selling_price = fields.Float(default=1000.00, readonly=True, copy=False)
    available_from = fields.Datetime("Avaliable", default=fields.Date.today() + relativedelta(months=3), copy=False)
    living_area = fields.Integer(string="Living area (sqm)")
    garage = fields.Boolean()
    status = fields.Char()
    
    buyer = fields.Many2one('res.users', copy=False)

    real_estate_property_type_id = fields.Many2one('real.estate.propety.type', string="Property Types")
    res_partner_id = fields.Many2one('res.partner', string="Salesperson")
    tag_ids = fields.Many2many('real.estate.propety.tags', string="Property Tags")

    offer_ids = fields.Many2many('real.estate.propety.offer', string="Property Offers")

    total_area = fields.Float(compute="_compute_total_area")
    
    @api.depends("living_area","garden_area")
    def _compute_total_area(self):
        for record in self:
            record.total_area = record.garden_area * record.living_area

    @api.onchange("garden")
    def _onchange_garden(self):
        self.garden = 10


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
    validity = fields.Integer(default=7)
    date_deadline = fields.Date(compute="_sum_date_deadline")

    
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
    
    @api.depends("validity")
    def _sum_date_deadline(self):
        for record in self:
            record.date_deadline = record.create_date + relativedelta(days=record.validity)

    def _inverse_date_deadline(self):
        for record in self:
            record.date_deadline = record.date_deadline_from

    
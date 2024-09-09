from odoo import fields, models
class TestModel(models.Model):
    _name = "test_model"
    _description = "Test Model"

    title = fields.Char(required=True)
    description = fields.Char()
    post_code = fields.Char()
    expected_price = fields.Float()
    bedrooms = fields.Integer(default=2)
    facades = fields.Integer()
    garden = fields.Boolean()
    garden_area = fields.Float()
    active = fields.Boolean(default=False)
    selling_price = fields.Float(default=1000.00, readonly=True)
    avaliable_from = fields.Datetime("Avaliable", default=fields.Date.today())
    living_area = fields.Integer()
    garage = fields.Boolean()
    status = fields.Char()
    
    
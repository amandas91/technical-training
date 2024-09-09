from odoo import fields, models

class TestModel(models.Model):
    _name = "test_model"
    _description = "Test Model"

    title = fields.Char()
    description = fields.Char()
    post_code = fields.Char()
    expected_price = fields.Float()
    bedrooms = fields.Integer()
    facades = fields.Integer()
    garder = fields.Boolean()
    
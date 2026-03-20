from odoo import models, fields

class MyModel(models.Model):
    _name = 'my.model'
    _description = 'Mijn model'

    name = fields.Char(string="Naam", required=True)
    description = fields.Text(string="Beschrijving")
{
    "name": "My Test Module",
    "version": "1.0",
    "category": "Custom",
    "summary": "Een voorbeeldmodule voor Odoo 17",
    "depends": ["base"],
    "data": [
        "views/my_model_views.xml",
        "security/ir.model.access.csv"
    ],
    "installable": True,
    "application": True
}
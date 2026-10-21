from odoo import fields, models


class AccountMove(models.Model):
    _inherit = "account.move"

    import_source = fields.Selection(
        [("manual", "Manual"), ("n8n", "Automática")],
        string="Origen",
        default="manual",
        readonly=True,
        copy=False,
    )
    import_channel = fields.Selection(
        [("formulario", "Formulario"), ("correo", "Correo")],
        string="Canal",
        readonly=True,
        copy=False,
    )
    import_sender = fields.Char(string="Remitente", readonly=True, copy=False)
    import_execution = fields.Char(string="Ejecución", readonly=True, copy=False)
    validation_state = fields.Selection(
        [("ok", "Conforme"), ("observada", "Observada")],
        string="Validación",
        readonly=True,
        copy=False,
        tracking=True,
    )
    validation_notes = fields.Text(string="Observaciones", readonly=True, copy=False)

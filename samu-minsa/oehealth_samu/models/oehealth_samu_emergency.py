# -*- coding: utf-8 -*-
from odoo import api, fields, models
from odoo.exceptions import ValidationError


class OehealthSamuEmergency(models.Model):
    '''
    Registro de pacientes de emergencias
    '''
    _name = 'oeh.medical.samu.emergency'
    _inherit = 'oeh.medical.emergency'

    observations = fields.Text('Observaciones')
    line_ids = fields.One2many('oeh.medical.samu.emergency.line', 'line_id', 'Unidades')
    samu_emergency_id = fields.Many2one('oeh.medical.samu.emergency', 'Emergencia')
    samu_obs = fields.Text('Observaciones')
    elapsed_time = fields.Integer('Tiempo transcurrido (minutos)')
    course = fields.Selection(selection=[(0, 'Estacionario'), (1, 'Otro')], string='Curso', required=True)
    priority = fields.Selection(selection=[(1, 'I'), (2, 'II'), (3, 'III')], string='Prioridad', required=True)
    cie10_1 = fields.Many2one('oeh.medical.pathology', u'CIE10 1')
    cie10_2 = fields.Many2one('oeh.medical.pathology', u'CIE10 2')
    cie10_3 = fields.Many2one('oeh.medical.pathology', u'CIE10 3')

    @api.constrains('elapsed_time')
    def _check_elapsed_time(self):
        for field in self:
            if field.elapsed_time and field.elapsed_time < 0:
                raise ValidationError('El tiempo transcurrido debe ser mayor o igual que cero (0)')


class OehealthSamuEmergencyLine(models.Model):
    _name = 'oeh.medical.samu.emergency.line'

    mobileunit_id = fields.Many2one('oehealth.samu.mobileunit', 'Unidad')
    line_id = fields.Many2one('oeh.medical.samu.emergency', 'Unidad')

    @api.multi
    def goto_mobileunity(self):
        self.ensure_one()
        return {
            'name': u'Ver unidad',
            'type': 'ir.actions.act_window',
            'view_mode': 'form',
            'target': 'self',
            'res_model': 'oehealth.samu.mobileunit',
            'view_id': self.env.ref('oehealth_samu.oehealth_samu_unidadesmoviles_view_form').id,
            'context': {
                'default_id': self.mobileunit_id.id,
            },
        }

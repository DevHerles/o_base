# -*- coding: utf-8 -*-
from odoo import api, fields, models
from odoo.exceptions import ValidationError

SELECTION_YES = 1
SELECTION_NO = 0
SELECTION_YES_NO = [
    (SELECTION_YES, 'Si'),
    (SELECTION_NO, 'No')
]
SELECTION_SEX_MALE = '01'
SELECTION_SEX_FEMALE = '02'
SELECTION_SEX = [
    (SELECTION_SEX_MALE, 'Masculino'),
    (SELECTION_SEX_FEMALE, 'Femenino'),
]
SELECTION_DOC_TYPE_DOI = '01'
SELECTION_DOC_TYPE_IMMIGRATION_CARD = '03'
SELECTION_DOC_TYPE = [
    (SELECTION_DOC_TYPE_DOI, 'DNI'),
    (SELECTION_DOC_TYPE_IMMIGRATION_CARD, 'CARNÉ DE EXTRANJERÍA'),
]

STATE_AVAILABLE = 'available'
STATE_BUSSY = 'bussy'
STATE_MAINTENANCE = 'maintenance'

SELECTION_MOBILE_STATE = [
    (STATE_AVAILABLE, 'Disponible'),
    (STATE_BUSSY, 'En servicio'),
    (STATE_MAINTENANCE, 'En mantenimiento'),
]


class OehealthSamuMobileunit(models.Model):
    _name = 'oehealth.samu.mobileunit'

    state = fields.Selection(SELECTION_MOBILE_STATE, 'Estado', readonly=True, default=lambda *e: STATE_AVAILABLE)
    name = fields.Char(string='Unidad movil')
    bodywork_id = fields.Many2one('oehealth.samu.mobileunit.bodywork', u'Carrocería')
    condition_id = fields.Many2one('oehealth.samu.mobileunit.condition', u'Condición')
    has_gps = fields.Boolean(string='¿Tiene GPS?')
    mileage = fields.Integer(string='Kilometraje')
    fuel_id = fields.Many2one('oehealth.samu.mobileunit.fuel', 'Combustible')
    patrimony_code = fields.Char(u'Código patrimonial')
    model_id = fields.Many2one('oehealth.samu.mobileunit.model', 'Modelo')
    mantainance_id = fields.Many2one('oehealth.samu.mobileunit.maintenance', 'Mantenimiento cada')
    license_plate = fields.Char(string='Placa', help='Placa de unidad movil')
    brand_id = fields.Many2one('oehealth.samu.mobileunit.brand', 'Marca de la unidad movil')
    image = fields.Binary('Foto')
    line_ids = fields.One2many('oehealth.samu.mobileunit.line', 'line_id', u'Imágenes')
    state_id = fields.Many2one('res.country.state', u'Región')
    province_id = fields.Many2one('res.country.state', 'Provincia')
    district_id = fields.Many2one('res.country.state', 'Distrito')
    unitytype_id = fields.Many2one('oehealth.samu.mobileunit.unitytype', 'Tipo')

    current_mileage = fields.Integer('Kilometraje actual')
    previous_mileage = fields.Integer('Kilometraje anterior')
    last_mileage_traveled = fields.Integer(u'Último kilometraje recorrido')
    current_fuel = fields.Float('Combustible actual')
    consumed_fuel = fields.Float('Combustible consumido')
    soat_expiration_date = fields.Date('Fecha de caducida de SOAT')
    next_technical_review = fields.Date(u'Próxima fecha de revisión técnica')
    approximate_maintenance_date = fields.Date('Fecha aproximada de mantenimiento')
    mechanical_company_id = fields.Many2one('oehealth.samu.mobileunit.mechanicalcompany', u'Empresa mecánica')

    radiator_water = fields.Selection(SELECTION_YES_NO, 'Agua de radiador')
    battery_water = fields.Selection(SELECTION_YES_NO, u'Agua de batería')
    wiper_water = fields.Selection(SELECTION_YES_NO, 'Agua de limpiaparabrisas')
    siren = fields.Selection(SELECTION_YES_NO, 'Sirena')
    high_light = fields.Selection(SELECTION_YES_NO, 'Luz alta')
    low_light = fields.Selection(SELECTION_YES_NO, 'Luz baja')

    mobile_unit_id = fields.Many2one('oehealth.samu.llamada', 'Llamada')

    @api.constrains('mileage')
    def _check_mileage(self):
        for field in self:
            if field.mileage and field.mileage < 0:
                raise ValidationError('El kilometraje debe ser mayor o igual que cero (0)')


class OehealthSamuMobileunitBodywork(models.Model):
    _name = 'oehealth.samu.mobileunit.bodywork'

    code = fields.Char(u'Código')
    name = fields.Char('Nombre')

    _sql_constraints = [('code_uniq', 'unique(code)', u'El código ya existe, por favor ingrese uno nuevo.')]


class OehealthSamuMobileunitCondition(models.Model):
    _name = 'oehealth.samu.mobileunit.condition'

    code = fields.Char(u'Código')
    name = fields.Char('Nombre')

    _sql_constraints = [('code_uniq', 'unique(code)', u'El código ya existe, por favor ingrese uno nuevo.')]


class OehealthSamuMobileunitFuel(models.Model):
    _name = 'oehealth.samu.mobileunit.fuel'

    code = fields.Char(u'Código')
    name = fields.Char('Nombre')

    _sql_constraints = [('code_uniq', 'unique(code)', u'El código ya existe, por favor ingrese uno nuevo.')]


class OehealthSamuMobileunitModel(models.Model):
    _name = 'oehealth.samu.mobileunit.model'

    code = fields.Char(u'Código')
    name = fields.Char('Nombre')

    _sql_constraints = [('code_uniq', 'unique(code)', u'El código ya existe, por favor ingrese uno nuevo.')]


class OehealthSamuMobileunitMaintenance(models.Model):
    _name = 'oehealth.samu.mobileunit.maintenance'

    code = fields.Char(u'Código')
    name = fields.Char('Nombre')

    _sql_constraints = [('code_uniq', 'unique(code)', u'El código ya existe, por favor ingrese uno nuevo.')]


class OehealthSamuMobileunitBrand(models.Model):
    _name = 'oehealth.samu.mobileunit.brand'

    code = fields.Char(u'Código')
    name = fields.Char('Nombre')

    _sql_constraints = [('code_uniq', 'unique(code)', u'El código ya existe, por favor ingrese uno nuevo.')]


class OehealthSamuMobileunitUnitytype(models.Model):
    _name = 'oehealth.samu.mobileunit.unitytype'

    code = fields.Char(u'Código')
    name = fields.Char('Nombre')

    _sql_constraints = [('code_uniq', 'unique(code)', u'El código ya existe, por favor ingrese uno nuevo.')]


class OehealthSamuMobileunitLine(models.Model):
    _name = 'oehealth.samu.mobileunit.line'

    name = fields.Char('Nombre')
    line_id = fields.Many2one(comodel_name='ir.attachment', inverse_name='res_id', string='Imágenes', help='Help note')
    image = fields.Binary('Foto')


class OehealthSamuMobileUnitMechanicalcompany(models.Model):
    _name = 'oehealth.samu.mobileunit.mechanicalcompany'

    code = fields.Char(u'Código')
    name = fields.Char('Nombre')

    _sql_constraints = [('code_uniq', 'unique(code)', u'El código ya existe, por favor ingrese uno nuevo.')]


class OehealthSamuProfile(models.Model):
    _name = 'oehealth.samu.profile'

    name = fields.Char('Perfil')
    code = fields.Char('Código del perfil')

    _sql_constraints = [('code_uniq', 'unique(code)', u'El código ya existe, por favor ingrese uno nuevo.')]


class OehealthSamuInstruction(models.Model):
    _name = 'oehealth.samu.instruction'

    name = fields.Char('Instrucción', help='Grado de instrucción')
    code = fields.Char('Código', help='Código de grado de instrucción')

    _sql_constraints = [('code_uniq', 'unique(code)', u'El código ya existe, por favor ingrese uno nuevo.')]

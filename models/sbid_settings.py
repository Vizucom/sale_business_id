# -*- coding: utf-8 -*-
from openerp import models, fields, _
from utils import check_vat_country, check_businessid_country


class SbidSettings(models.Model):

    _name = "sale_business_id.settings"

    show_bid_vat_for_affiliates = fields.Boolean('Show business ID and VAT fields for affiliates')

# -*- coding: utf-8 -*-
from openerp import models, fields, api, _


class ResPartner(models.Model):

    _inherit = 'res.partner'

    @api.multi
    @api.onchange('parent_id', 'country_id', 'company_type')
    def _get_shown_bid_vat(self):
        ir_config_model = self.env['ir.config_parameter']
        show_for_affiliates = ir_config_model.get_param("sale_business_id.show_vat_and_bid_for_child_companies")

        country_group_show_vat = self.env.ref('sale_business_id.country_group_show_vat')
        country_group_show_bid = self.env.ref('sale_business_id.country_group_show_bid')

        for partner in self:
            if partner.company_type == 'company' and \
                partner.country_id and \
                partner.country_id.id in [c.id for c in country_group_show_bid.country_ids] and \
                (not partner.parent_id or show_for_affiliates):
                partner.businessid_shown = True
            else:
                partner.businessid_shown = False

            if partner.company_type == 'company' and \
                partner.country_id and \
                partner.country_id.id in [c.id for c in country_group_show_vat.country_ids] and \
                (not partner.parent_id or show_for_affiliates):
                partner.vat_shown = True
            else:
                partner.vat_shown = False

    businessid = fields.Char(string="Business ID", size=20)
    businessid_shown = fields.Boolean(compute=_get_shown_bid_vat, string='Business ID shown', selectable=False)
    vat_shown = fields.Boolean(compute=_get_shown_bid_vat, string='VAT shown', selectable=False)

    _sql_constraints = [
        ('businessid_unique', 'unique(businessid)', _('The business ID already exists for another partner.'))
    ]

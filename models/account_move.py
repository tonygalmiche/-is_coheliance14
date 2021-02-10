# -*- coding: utf-8 -*-
from datetime import datetime, timedelta
import time
from odoo import api, fields, models


class AccountMove(models.Model):
    _inherit = 'account.move'


    @api.depends('invoice_date','amount_total','partner_id')
    def _compute(self):
        for obj in self:
            filter=[
                ('invoice_date', '=' , obj.invoice_date),
                ('amount_total', '=' , obj.amount_total),
                ('partner_id'  , '=' , obj.partner_id.id),
            ]
            invoices = self.env['account.move'].search(filter)
            print('TEST',obj,invoices)
            msg=False
            if len(invoices)>1:
                msg='Attention : Il existe une autre facture du même montant à cette même date et pour ce même fournisseur'
            obj.is_msg_err=msg

    @api.depends('invoice_line_ids','state')
    def _compute_order_id(self):
        for obj in self:
            for line in obj.invoice_line_ids:
                for order in line.sale_line_ids:
                    obj.order_id=order.order_id.id
                    affaire_id = order.order_id.affaire_id.id
                    if affaire_id:
                        obj.is_affaire_id=affaire_id
                        line.is_affaire_id=affaire_id
                    
            for line in obj.invoice_line_ids:
                line.is_affaire_id=obj.is_affaire_id.id


    order_id                 = fields.Many2one('sale.order', 'Commande', compute=_compute_order_id,store=True)
    is_affaire_id            = fields.Many2one('is.affaire', 'Affaire')
    is_refacturable          = fields.Selection([('oui','Oui'),('non','Non')], u"Refacturable")
    is_nom_fournisseur       = fields.Char('Nom du fournisseur')
    is_personne_concernee_id = fields.Many2one('res.users', u'Personne concernée')
    is_msg_err               = fields.Char('Message', compute='_compute', readonly=True)


    def actualiser_affaire_sur_facture_action(self):
        for obj in self:
            if obj.order_id and not obj.is_affaire_id:
                obj.is_affaire_id = obj.order_id.affaire_id


    def actualiser_affaire_sur_ligne_action(self):
        for obj in self:
            if obj.is_affaire_id:
                for line in obj.invoice_line:
                    if not line.is_affaire_id:
                        line.is_affaire_id = obj.is_affaire_id.id


    def voir_facture_fournisseur(self):
        for obj in self:
            res= {
                'name': 'Facture',
                'view_mode': 'form',
                'view_type': 'form',
                'res_model': 'account.move',
                'res_id': obj.id,
                'type': 'ir.actions.act_window',
            }
            return res


    # def name_search(self, cr, user, name='', args=None, operator='ilike', context=None, limit=100):
    #     if not args:
    #         args = []
    #     if name:
    #         filtre=['|',('name','ilike', name),('internal_number','ilike', name)]
    #         ids = self.search(cr, user, filtre, limit=limit, context=context)
    #     else:
    #         ids = self.search(cr, user, args, limit=limit, context=context)


    #     result = self.name_get(cr, user, ids, context=context)
    #     return result


class AccountMoveLine(models.Model):
    _inherit = "account.move.line"

    is_affaire_id = fields.Many2one('is.affaire', 'Affaire')
    is_account_invoice_line_id = fields.Integer('Lien entre account_invoice_line et account_move_line pour la migration')


    # def product_id_change(self, product, uom_id, qty=0, name='', type='out_invoice',
    #         partner_id=False, fposition_id=False, price_unit=False, currency_id=False,
    #         company_id=None, is_affaire_id=False):
    #     res = super(account_invoice_line, self).product_id_change(product, uom_id, qty=qty, name=name, type=type,
    #         partner_id=partner_id, fposition_id=fposition_id, price_unit=price_unit, currency_id=currency_id,
    #         company_id=company_id)
    #     if 'value' in res:
    #         if 'name' in res['value']:
    #             res['value']['name']=False
    #         if is_affaire_id:
    #             res['value']['is_affaire_id']=is_affaire_id
    #     return res




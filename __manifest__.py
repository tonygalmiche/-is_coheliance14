# -*- coding: utf-8 -*-
{
    "name" : "InfoSaône - Module Odoo 14 pour Coheliance",
    "version" : "0.1",
    "author" : "InfoSaône / Tony Galmiche",
    "category" : "InfoSaône",
    "description": """
InfoSaône - Module Odoo 14 pour Coheliance
===================================================

InfoSaône - Module Odoo 14 pour Coheliance
""",
    "maintainer": "InfoSaône",
    "website": "http://www.infosaone.com",
    "depends" : [
        "base",
        "mail",
        "calendar",               # Agenda
        "crm",                    # CRM
#        "account",
#        "account_voucher",        # eFacturation & Règlements
#        "account_accountant",     # Comptabilité et finance
        "sale",                   # Gestion des ventes
        "purchase",               # Gestion des achats
#        "sale_order_dates",       # Ajout de champs dates dans les commandes clients (date demandée)
        "project",                # Gestin de projets
        "hr",                     # Répertoire des employés
#        "hr_timesheet_sheet",     # Feuilles de temps
#        "report",
    ],
    "init_xml" : [],             # Liste des fichiers XML à installer uniquement lors de l"installation du module
    "demo_xml" : [],             # Liste des fichiers XML à installer pour charger les données de démonstration
    "data" : [
        "security/ir.model.access.csv",
        "views/assets.xml",
        "views/product_view.xml", 
        "views/res_partner_view.xml", 
        "views/sale_view.xml",
#        "views/account_invoice_view.xml",
#        "views/account_bank_statement_view.xml",
        "views/is_coheliance_view.xml",
#        "views/is_coheliance_sequence.xml",
        "views/is_suivi_tresorerie_view.xml",
        "views/is_export_compta.xml",
#        "views/is_coheliance_report.xml",
        "views/is_prospective_view.xml",
        "views/is_compte_resultat_view.xml",
        "views/is_bilan_pedagogique_view.xml",
        "views/is_suivi_banque_view.xml",
        "views/is_suivi_caisse_view.xml",
#        "views/layouts.xml",
#        "views/layouts-convention.xml",
#        "views/report_affaire.xml",
#        "views/report_convention.xml",
#        "views/report_convention_st.xml",
#        "views/report_contrat_formation.xml",
#        "views/report_invoice.xml",
#        "views/report_frais.xml",
#        "views/report_fiche_frais.xml",
#        "views/report_compte_resultat.xml",
        "report/is_suivi_facture.xml",
        "report/is_suivi_refacturation_associe.xml",
        "report/is_suivi_intervention.xml",
        "report/is_account_invoice_line.xml",
        "views/menu.xml",
    ],                           # Liste des fichiers XML à installer lors d"une mise à jour du module (ou lord de l"installation)
    "installable": True,         # Si False, ce module sera visible mais non installable (intéret ?)
    "active": False,             # Si True, ce module sera installé automatiquement dés la création de la base de données d"OpenERP
    "application": True,
}


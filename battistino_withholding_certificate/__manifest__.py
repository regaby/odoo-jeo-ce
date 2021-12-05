# Copyright 2021 jeo Software
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    "name": "Battistino Withholdings Certificate",
    "summary": "Certificado de retenciones con la firma de Battistino",
    "version": "13.0.1.0.0",
    "development_status": "Alpha", # "Alpha|Beta|Production/Stable|Mature"
    "category": "Accounting",
    "website": "http://jeosoft.com.ar",
    "author": "jeo Software",
    "maintainers": ["jobiols"],
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "depends": [
        'l10n_ar_account_withholding',
    ],
    "data": [
        'reports/report_withholding_certificate.xml',
    ],
}

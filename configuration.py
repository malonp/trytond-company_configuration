# This file is part of Tryton.  The COPYRIGHT file at the top level of
# this repository contains the full copyright notices and license terms.
from trytond.model import ModelView, ModelSQL, ModelSingleton, fields

try:
    import pytz
    TIMEZONES = [(x, x) for x in pytz.common_timezones]
except ImportError:
    TIMEZONES = []
TIMEZONES += [(None, '')]


__all__ = ['Configuration']


class Configuration(ModelSingleton, ModelSQL, ModelView):
    'Company Configuration'
    __name__ = 'company.configuration'

    company_currency = fields.Property(fields.Many2One('currency.currency',
            'Company Currency', help=('The value set on this field will preset the currency on new '
            'companies')))
    company_timezone = fields.Property(fields.Selection(TIMEZONES, 'Company Timezone', translate=False,
        help=('The value set on this field will preset the timezone on new '
            'companies')))

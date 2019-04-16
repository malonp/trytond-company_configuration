##############################################################################
#
#    GNU Condo: The Free Management Condominium System
#    Copyright (C) 2016- M. Alonso <port02.server@gmail.com>
#
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from trytond.model import ModelView, ModelSQL, ModelSingleton, fields


try:
    import pytz

    TIMEZONES = [(x, x) for x in pytz.common_timezones]
except ImportError:
    TIMEZONES = []
TIMEZONES += [(None, '')]


__all__ = ['Configuration']


class Configuration(ModelSingleton, ModelSQL, ModelView):
    "Company Configuration"
    __name__ = 'company.configuration'

    company_currency = fields.Many2One(
        'currency.currency',
        'Company Currency',
        help=('The value set on this field will preset the currency on new ' 'companies'),
    )
    company_timezone = fields.Selection(
        TIMEZONES,
        'Company Timezone',
        translate=False,
        help=('The value set on this field will preset the timezone on new ' 'companies'),
    )

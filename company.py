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


from trytond.pool import Pool, PoolMeta

__all__ = ['Company']


class Company(metaclass=PoolMeta):
    __name__ = 'company.company'

    @staticmethod
    def default_currency():
        Configuration = Pool().get('company.configuration')
        config = Configuration(1)
        if config.company_currency:
            return config.company_currency.id

    @staticmethod
    def default_timezone():
        Configuration = Pool().get('company.configuration')
        config = Configuration(1)
        if config.company_timezone:
            return config.company_timezone

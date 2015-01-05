# -*- encoding: utf-8 -*-

# Odoo, Open Source Management Solution
# Copyright (C) 2014-2015  Grupo ESOC <www.grupoesoc.es>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

{
    "name": "Partner CNAE",
    "version": "3.0",
    "category": "Customer Relationship Management",
    "summary": "Store CNAE code for your partner",
    "description":
"""
Español
=======

Este módulo añade el campo "CNAE" a las empresas, e importa el listado completo
de CNAE actuales (versión 2009) en una nueva tabla a la que se puede acceder
desde el menú *Ventas > Configuración > Códigos CNAE*.

"CNAE" significa "Clasificación Nacional de Actividades Económicas", y es un
tipo oficial de clasificación que se utiliza para las empresas españolas.

`Más información`__.

__ codes_
.. _codes: http://www.ine.es/jaxi/menu.do?type=pcaxis&path=/t40/clasrev&file=inebase

English
=======

This module adds the "CNAE" field to the partners, and imports the current full
list of CNAE codes (version 2009) in a new table that you can access from
*Sales > Configuration > CNAE Codes*.

CNAE is the Spanish acronym for "Economic Activities National Classification",
and is an official classification that Spanish enterprises use.

`More information`__.

__ codes_
""",
    "author": "Grupo ESOC",
    "website": "http://www.grupoesoc.es",
    "license": "AGPL-3",
    "installable": True,
    "depends": ["crm"],
    "data": [
        "security/ir.model.access.csv",
        "data/l10n_es_partner_cnae.cnae_codes.csv",
        "view/partner.xml",
        "view/cnae.xml",
    ],
}

# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request


class ServiceRequest(http.Controller):
    @http.route(['/tree'], type='http', auth="public", website=True)
    def service_request(self, **post):
        return request.render("um_tree_planting.request_form")

    @http.route(['/customer/form/submit'], type='http', auth="public", website=True)
    def customer_form_submit(self, **post):
        partner = request.env['um.treeplanting'].create({
            'name': post.get('name'),
            'nrp': post.get('nrp'),
            'entitas_id': post.get('entitas_id'),
            'jumlah': post.get('jumlah'),
            'jenis_pohon': post.get('jenis_pohon'),
            'start_date': post.get('start_date'),
            'lokasi': post.get('lokasi'),
            'foto': post.get('foto'),
            'noted': post.get('noted')
        })
        vals = {
            'partner': partner,
        }
        return request.render("um_tree_planting.tmp_customer_form_success", vals)

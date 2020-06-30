# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request
from odoo.addons.portal.controllers.portal import CustomerPortal
from odoo.http import route

class CustomerPortalInherit(CustomerPortal):
    OPTIONAL_BILLING_FIELDS = ["zipcode", "state_id", "vat", "company_name","age"]
    MANDATORY_BILLING_FIELDS = ["name", "phone", "email", "street", "city", "country_id"]
    @route(['/my/account'], type='http', auth='user', website=True)
    def account(self, redirect=None, **post):
        print('---------------*******************************************--------------------------Vola')
        values = self._prepare_portal_layout_values()
        partner = request.env.user.partner_id
        values.update({
            'error': {},
            'error_message': [],
        })

        if post and request.httprequest.method == 'POST':
            error, error_message = self.details_form_validate(post)
            values.update({'error': error, 'error_message': error_message})
            values.update(post)
            if not error:
                values = {key: post[key] for key in self.MANDATORY_BILLING_FIELDS}
                values.update({key: post[key] for key in self.OPTIONAL_BILLING_FIELDS if key in post})
                for field in set(['country_id', 'state_id']) & set(values.keys()):
                    try:
                        values[field] = int(values[field])
                    except:
                        values[field] = False
                values.update({'zip': values.pop('zipcode', '')})
                partner.sudo().write(values)
                if redirect:
                    return request.redirect(redirect)
                return request.redirect('/my/home')

        countries = request.env['res.country'].sudo().search([])
        states = request.env['res.country.state'].sudo().search([])

        values.update({
            'partner': partner,
            'countries': countries,
            'states': states,
            'has_check_vat': hasattr(request.env['res.partner'], 'check_vat'),
            'redirect': redirect,
            'page_name': 'my_details',
        })

        response = request.render("portal.portal_my_details", values)
        response.headers['X-Frame-Options'] = 'DENY'
        return response
    


# class CustomModule(http.Controller):
#     @http.route('/custom_module/custom_module/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/custom_module/custom_module/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('custom_module.listing', {
#             'root': '/custom_module/custom_module',
#             'objects': http.request.env['custom_module.custom_module'].search([]),
#         })

#     @http.route('/custom_module/custom_module/objects/<model("custom_module.custom_module"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('custom_module.object', {
#             'object': obj
#         })

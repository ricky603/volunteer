from odoo import http
from odoo.http import request


class VolunteerForm(http.Controller):
    @http.route('/volunteer_webform', type="http", auth="public", website=True)
    def volunteer_form(self, **post):
        volunteer_degree = request.env['volunteer.degree'].sudo().search([])
        volunteer_area = request.env['volunteer.interest'].sudo().search([])
        return request.render("volunteer.volunteer_registration", {
            'volunteer_degree': volunteer_degree,
            'volunteer_interest': volunteer_area
        })

    @http.route('/create/webvolunteer', type="http", auth="public", website=True)
    def create_volunteer(self, **post):
        print("data", request.httprequest.form.getlist('area_of_interest'))
        request.env['volunteer'].sudo().create({
            'volunteer_name': post.get('volunteer_name'),
            'volunteer_date_of_birth': post.get('volunteer_date_of_birth'),
            'volunteer_gender': post.get('gender'),
            'volunteer_marital': post.get('marital_status'),
            'volunteer_race': post.get('race'),
            'volunteer_religion': post.get('religion'),
            'volunteer_blk': post.get('blk'),
            'volunteer_unit_no': post.get('unit_no'),
            'volunteer_street_name': post.get('street_name'),
            'volunteer_postal_code': post.get('postal_code'),
            'volunteer_citizenship': post.get('citizenship'),
            'volunteer_nationality': post.get('nationality'),
            'volunteer_occupation': post.get('occupation'),
            'volunteer_nric_no': post.get('nric_no'),
			'volunteer_phone_number': post.get('phone_number'),
			'volunteer_email': post.get('email'),
			'volunteer_transportation': post.get('transportation'),
			'volunteer_employer_address': post.get('employer_address'),
			'volunteer_language': post.get('language'),
			'volunteer_degree':int(post.get('degree')),
			'volunteer_experience': post.get('experience'),
			'volunteer_area_of_interest': (0,0)
			})
        return request.render("volunteer.success_form")

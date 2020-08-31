from odoo import models, fields

class VolunteerDegree(models.Model):
	_name = "volunteer.degree"

	name = fields.Char("Degree", required="True")
	sequence = fields.Integer("Sequence", default=1)

class VolunteerAreaOfInterest(models.Model):
	_name = "volunteer.interest"

	name = fields.Char("Area Of Interest", required="True")

class Volunteer(models.Model):
	_name = 'volunteer'
	_description = 'Volunteer Record'

	volunteer_name = fields.Char(string='Name')
	volunteer_date_of_birth = fields.Date(string='Date of Birth')
	volunteer_gender = fields.Selection((('Male', 'Male'), ('Female', 'Female')), 'Gender')
	volunteer_marital = fields.Selection((('Single', 'Single'), ('Married', 'Married'), ('Divorced', 'Divorced'), ('Widowed', 'Widowed')), 'Marital Status')
	volunteer_race = fields.Char(string='Race')
	volunteer_religion = fields.Char(string='Religion')

	volunteer_blk = fields.Char(string='Blk')
	volunteer_unit_no = fields.Char(string='Unit No.')
	volunteer_street_name = fields.Char(string='Street Name')
	volunteer_postal_code = fields.Char(string='Postal Code')

	volunteer_citizenship = fields.Char(string='Citizenship')
	volunteer_nationality = fields.Char(string='Nationality')
	volunteer_occupation = fields.Char(string='Occupation')
	volunteer_nric_no = fields.Char(string='NRIC No.')

	volunteer_phone_number = fields.Char(string='Phone Number')
	volunteer_email = fields.Char(string='Email Address')
	volunteer_transportation = fields.Char(string="Transportation")

	volunteer_employer_name = fields.Char(string='Employer Name')
	volunteer_employer_address = fields.Char(string='Employer Address')

	volunteer_language = fields.Char(string="Language")
	volunteer_degree = fields.Many2one('volunteer.degree', 'Degree')
	volunteer_experience = fields.Text(string="Experience in Volunteer Work / Community Service")
	volunteer_area_of_interest = fields.Many2many('volunteer.interest', string="Area Of Interest")
	

""" Script to be run with `python manage.py runscript create_test_data`

It'll populate the db with some tests studies.
"""
from core.models import (
	Study,
	Region
)


regions = [
	'Sacramento, CA',
	'Mexico City, MX'
]
test_studies = [
	{
		'name': 'Cancer research',
		'region': regions[0],
		'description': 'Find out what causes cancer.'
	},
	{
		'name': 'Smoking study',
		'region': regions[0],
		'description': 'Why do people smoke?.'
	},
	{
		'name': 'PCAR: Effects of Car pollution on Diabetes Prevalance',
		'region': regions[1],
		'description': 'Do cars cause diabetes?'
	},
]


def run():
	for r in regions:
		if not Region.objects.filter(name=r).first():
			Region.objects.create(name=r)

	for study in test_studies:
		region = Region.objects.filter(name=study['region']).first()

		study['region'] = region
		Study.objects.get_or_create(**study)


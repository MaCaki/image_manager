from django.contrib.auth.models import User
from django.test import TestCase

from .models import (
    Grade,
    GradeType,
    GradeEntry,
    GradeField,
    create_grade_field_with_options
)


class GradeEntryTest(TestCase):
    """Ensure that grade entry edits and saves are valid."""

    def setUp(self):
        # Every test needs access to the request factory.
        self.user = User.objects.create_user(
            username='testerson',
            email='test@example.com',
            password='top_secret'
        )
        self.test_grade_type = GradeType(name='test grade type')

    def test_create_grade_field_with_options(self):
        """Should create a grade field with option."""
        options = ['option_1', 'option_2', 'option_3']

        create_grade_field_with_options(
            'test_grade_field',
            'fill in this field.',
            self.test_grade_type,
            options
        )

        # query for the saved grade field and ensure that all expected options
        # are there.
        grade_field = GradeField.objects.filter(
            field_name='test_grade_field'
        ).first()

        gf_options = [o.name for o in grade_field.options]

        for opt in options:
            self.assertIn(opt, gf_options)

    def test_save_with_valid_value(self):
        """Grade entry should only have valid values."""
        # Create some fields
        options = ['option_1', 'option_2', 'option_3']

        field = create_grade_field_with_options(
            'test_grade_field',
            'fill in this field.',
            self.test_grade_type,
            options
        )

        grade = Grade(user=self.user, grade_type=self.test_grade_type)
        grade.save()

        GradeEntry(
            grade=grade, grade_field_type=field, value='option_1'
        ).save()

        saved_entries = grade.grade_entry_set.all()
        self.assertIsNotNone(saved_entries)
        self.assertEqual(saved_entries[0].value, 'option_1')

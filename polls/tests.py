# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime

from django.utils import timezone
from django.test import TestCase

from .models import Question, Choice


class QuestionModelTests(TestCase):

    fixtures = ['polls_testdata.json']

    def test_fixture(self):
        self.assertEqual(Question.objects.all().count(), 1)
        self.assertEqual(Choice.objects.all().count(), 6)

    def test_get_choices(self):
        question_obj = Question.objects.get(pk=2)
        question_choices = question_obj.get_choices()
        self.assertEqual(len(question_choices), 6)

    def test_get_leading_choice(self):
        question_obj = Question.objects.get(pk=2)
        leading_choice = question_obj.get_leading_choice()
        self.assertEqual(leading_choice.choice_text, 'Mickey Mouse')

    def test_get_leading_choice_pct(self):
        question_obj = Question.objects.get(pk=2)
        lead_pct = question_obj.get_leading_choice_pct()
        self.assertEqual(lead_pct, 0.3076923076923077)


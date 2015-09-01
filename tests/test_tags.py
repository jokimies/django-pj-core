#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.test import TestCase
from django.template import Context, Template
from pjcore.templatetags.pjcore_tags import PERCENTAGE_DEFAULT_COLORS

class TagTests(TestCase):

    def tag_test(self, template, context, output):
        t = Template('{% load pjcore_tags %}'+template)
        c = Context(context)
        self.assertEqual(t.render(c), output)

    def test_colorize_percentage_less_than_zero(self):

        template = "{{ value | colorize_percentage}}"
        output = PERCENTAGE_DEFAULT_COLORS[1]
        context = { "value": -1.0 }
        self.tag_test(template, context, output)

    def test_colorize_percentage_greater_than_zero(self):

        template = "{{ value | colorize_percentage}}"
        output = PERCENTAGE_DEFAULT_COLORS[0]
        context = { "value": 1.0 }
        self.tag_test(template, context, output)

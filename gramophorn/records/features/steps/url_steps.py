# -*- coding: utf-8 -*-
from lettuce import step, world
from django.test import Client

@step(u'Given I want to navigate the site')
def given_i_want_to_navigate_the_site(step):
    world.client = Client()

@step(u'When I go to the (.*)')
def when_i_go_to_the_homepage(step, page):
    world.resp = world.client.get(page)


@step(u'Then I should see a working page')
def then_i_should_see_a_working_page(step):
    assert world.resp.status_code == 200, "Pagina nao funcionou %s"% world.resp.status_code


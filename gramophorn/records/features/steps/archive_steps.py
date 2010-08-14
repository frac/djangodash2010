# -*- coding: utf-8 -*-
from lettuce import step, world

@step(u'Given I have (a|an) (.*) model')
def given_i_have_a_model(step, article , model):
    try:
        foo = __import__("gramophorn.records.models", globals(), locals(), [model,], -1)
        real = getattr(foo, model)
        world.this_model = real()
    except ImportError:
        assert False, "Module %s not found"% model
    except AttributeError:
        assert False, "Module %s not found"% model
   
@step(u'And the model has the following attributes')
def and_the_model_has_the_following_attributes(step):
    for foo in step.hashes:
        assert hasattr(world.this_model, foo['attr']), "model has no %s attrubute" % foo['attr']



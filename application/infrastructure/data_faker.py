#!/usr/bin/env python
import random
import datetime

from django_faker import Faker

populator = Faker.getPopulator(locale='en-gb')

from domain.achievement.models import Intention, Measurement

populator.addEntity(Intention, 100,
                    {
                      'action': lambda x: 18,
                      'intention_text': populator.faker.sentence(),
                      'intended_metric': lambda x: random.choice([i for i in range(10, 100)]),
                      'enjoyable_aspects': populator.faker.sentence(),
                      'created_date': datetime.datetime.now(),
                      'updated_date': datetime.datetime.now()
                  })
retval = populator.execute()
print retval

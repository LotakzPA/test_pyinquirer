from __future__ import print_function, unicode_literals
import json
import pprint

from PyInquirer import prompt
from questions import questions

questions = questions

answers = prompt(questions)
pp = pprint.PrettyPrinter(indent=4)
pp.pprint(answers)

with open('text.json', 'w') as file:
    file.write(json.dumps(answers, indent=4))

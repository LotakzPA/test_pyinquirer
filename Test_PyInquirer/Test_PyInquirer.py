from __future__ import print_function, unicode_literals

import pprint

from PyInquirer import prompt
from questions import questions


questions = questions

answers = prompt(questions)
# print(json.dumps(answers, indent=4))  # use the answers as input for your app
# print(answers)
pp = pprint.PrettyPrinter(indent=4)
pp.pprint(answers)

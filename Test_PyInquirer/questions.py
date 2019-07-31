from PyInquirer import Separator
from MyValidators import PhoneNumberValidator


questions = [
    {
        'type': 'input',
        'name': 'first_name',
        'message': 'What\'s your first name',
    },
    {
        'type': 'password',
        'name': 'password',
        'message': 'What\'s your password',
    },
    {
        'type': 'input',
        'name': 'number',
        'message': 'Type your phone number',
        'validate': PhoneNumberValidator
    },
    {
        'type': 'list',
        'name': 'choice',
        'message': "Which is your favorite teacher",
        'choices': ['Gwen', 'Fredi', 'Eric Thomas', 'Veronique'],
    },
    {
        'type': 'checkbox',
        'qmark': '😃',
        'message': 'Why ?',
        'name': 'toppings',
        'choices': [
            Separator('= OS ='),
            {
                'name': 'Linux distro'
            },
            {
                'name': 'Windows'
            },
            {
                'name': 'OS X'
            },
            Separator('= Is/She he smart ? ='),
            {
                'name': 'Yes',
                'checked': True
            },
            {
                'name': 'May be'
            },
            {
                'name': 'No'
            },
            Separator('= Is/She is pretty ? ='),
            {
                'name': 'Yes'
            },
            {
                'name': 'too pretty',
                'disabled': 'Nobody is too pretty'
            },
            {
                'name': 'Non'
            }
        ],
        'validate': lambda answer: 'You must choose at least one topping.' \
            if len(answer) == 0 else True
    }
]

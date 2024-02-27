# Exercise - question and answer system

questions = [
    {
        'Question': '2+2 is equal to?',
        'Options': ['1', '3', '4', '5'],
        'Answer': '4',
    },
    {
        'Question': '5*5 is equal to?',
        'Options': ['25', '55', '10', '51'],
        'Answer': '25',
    },
    {
        'Question': '10/2 is equal to?',
        'Options': ['4', '5', '2', '1'],
        'Answer': '5',
    },
]

correct_questions = 0

for question in questions:
        options = question['Options']
        print(f'Question: {question.get('Question')}')
        for idx, option in enumerate(options):
            print(f'{idx}) - {option}')

        user_input = input('Choose an option: ')

        choice_int = None
        options_qty = len(options)
        correct = False

        if user_input.isdigit():
             choice_int = int(user_input)

        if choice_int is not None:
            if choice_int >= 0 and choice_int < options_qty:
                 if question['Options'][int(user_input)] == question.get('Answer'):                    
                    correct = True

        if correct:
            print('Correct ✅')
            correct_questions += 1
        else:
            print('Wrong ❌')

print(f'You answered {correct_questions} of {len(questions)} questions correctly.')
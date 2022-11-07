import pyperclip

i = 0
text = ''''''
qn = input('Sentences or Text? (S/T) >> ')

try:
    if qn.lower() == 't':
        try:
            inputText = input('type what you want to be copied >> ')
            times = int(input('how many times do you want this to be printed? >> '))
            line = input('do you want to have a line on each repetition? (Y/N) >> ')
        except:
            print('Invalid Input')
        while i < times:
            text += inputText
            text += '\n' if (line.lower() == 'y') else ' '
            i += 1
        pyperclip. copy(text)
        print('copied to clipboard..')

    elif qn.lower() == 's':
        try:
            sentence = input("Enter the sentence and add '???' where you want to replace the words >> ")
        except:
            print('Invalid Input')
        word = ''
        words = []

        while word.lower() != 'done':
            try:
                word = input("Enter the words and enter 'done' when you're done >> ")
            except:
                print("Invalid Input")
            if word.lower() == 'done':
                continue
            words.append(word)

        for w in words:
            text += f'{sentence}\n'
            text = text.replace('???', w)

        pyperclip. copy(text)
        print('copied to clipboard..')

    else:
        print('Invalid Input')
except:
    print("Some Error Occurred!")
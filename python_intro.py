def hi(name, number):
    print(number+ ' Hi ' + name + '!')
girls = ['Rachel', 'Monica', 'Phoebe', 'Sonja', 'Mireia']
for number, name in zip(range(1, 6), girls):
    hi(name, str(number))

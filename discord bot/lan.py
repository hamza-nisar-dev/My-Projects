with open('lan2.py', 'r') as input:
    output = open('example.py', 'w')

    output.write(input.read())
    output.close()

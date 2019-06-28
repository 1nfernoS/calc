import decimal, datetime

def hist():
    with open('history.txt') as f:
        text = f.read()
    print(text)

def logging(res):
    log = open('history.txt', 'a')
    log.write(str(datetime.datetime.utcnow()) + ' | ' + s + ' = ' + str(res) + '\n')
    log.close()
    
def sum(n1,n2):
    res = n1+n2
    if res%1 == 0:
        res = int(res)
    print('{} + {} = {}'.format(n1, n2, res))
    logging(res)
    
def dif(n1,n2):
    res = n1-n2
    if res%1 == 0:
        res = int(res)
    print('{} - {} = {}'.format(n1, n2, res))
    logging(res)
    
def mult(n1,n2):
    res = n1*n2
    if res%1 == 0:
        res = int(res)
    print('{} * {} = {}'.format(n1, n2, res))
    logging(res)
    
def div(n1,n2):
    try:
        res = n1/n2
        if res%1 == 0:
            res = int(res)
        print('{} / {} = {}'.format(n1, n2, round(res, 2)))
        logging(res)
    except ZeroDivisionError:
        print("Can't divide by Zero")

def pow(n1,n2):
    res = n1**n2
    if res%1 == 0:
        res = int(res)
    print('{} ^ {} = {}'.format(n1, n2, res))
    logging(res)

def mod(n1,n2):
    res = n1%n2
    if res%1 == 0:
        res = int(res)
    print('{} % {} = {}'.format(n1, n2, res))
    logging(res)
    
        
def operator(inp):
    if inp[1] == '+':
        sum(inp[0],inp[2])
    elif inp[1] == '-':
        dif(inp[0],inp[2])
    elif inp[1] == '/' or inp[1] == 'div':
        div(inp[0],inp[2])
    elif inp[1] == '^' or inp[1] == 'pow' or inp[1] == '**':
        pow(inp[0],inp[2])
    elif inp[1] == '*':
        mult(inp[0],inp[2])
    elif inp[1] == '%' or inp[1] == 'mod':
        mod(inp[0],inp[2])
    else:
        print('Error')

print('This is simple calculator. Type help, h, -help, --help, /help, ?, /? for help')
while True:
    s = str(input())
    try:
        if s == 'exit' or s == 'ex' or s == 'close' or s == 'quit' or s == 'q' or s == 'e' or s == 'c':
            break
        elif s == 'hist':
            hist()
        elif s == 'help' or s == '/help' or s == '--help' or s == '-help' or s == '?' or s == '/?' or s == 'h':
            print('''This is simple calculator. List of commands:\n
                  +          to sum\n
                  -          to differ\n
                  *          to multiply\n
                  /, div     to divide(round .00)\n
                  **, ^, pow to power\n
                  %, mod     to modulus\n
                  hist       to get history of calculations\n
                  for exit type e, ex, exit, c, close, q, quit
                  for this message type help, h, -help, --help, /help, ?, /?
                  ==========================================================\n''')   
        elif s == 'a' or s == 'about':
            print('''Simple calculator v1.4\n\n\n
                Author: Misha Gaydenko\n\n
                Special thanks to\n\n
                General code partner\n
                Proshin Egor\n\n
                Spectators\n
                Lomaev Aleksei\n
                Kondrat'ev Leon\n\n
                              AND YOU\n\n\n
                For  non-commercial use ONLY!!!\n
                College of Communications №54, 1ISP11-6, 2019''')
        else:
            inp = s.split(' ')
            if inp[0].find('.') != -1:
                inp[0] = float(inp[0])
            else:
                inp[0] = int(inp[0])
            if inp[2].find('.') != -1:
                inp[2] = float(inp[2])
            else:
                inp[2] = int(inp[2])
            operator(inp)
    except ValueError:
        continue

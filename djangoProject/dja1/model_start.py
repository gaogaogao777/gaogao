import os

if __name__ == '__main__':
    f = open('./dja1/output.txt', 'a+')
    f.writelines('new line1112'+os.linesep)

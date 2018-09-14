#Errors and exception handling
#FileNotFoundException
try:
    '''
    This is a DOCSTRING for this try block
    '''
    with open('test_xml.xml', 'r') as f:
        FILE_ROWS = f.readlines()
        for EACH_ROW in FILE_ROWS:
            print(EACH_ROW)
except FileNotFoundError:
    print("Mentioned file doesn't exist")
else:
    print('File Contents Ends here')
finally:
    print('Read file contents program ends here')


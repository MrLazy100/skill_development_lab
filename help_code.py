def read_message():

   quotes = open(r'D:\Java aptech\Jeopardy\src\jeopardy\help_text.txt')
   read_file = quotes.read()
   print(read_file)
   quotes.close()

read_message()
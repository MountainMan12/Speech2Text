#This is a program to convert spoken paragraph to a written paragraph in Python 3
import sys

class Speech2Text:

    def __init__(self):
        self.in_para = ''

    def get_input(self):
        print('Please enter a paragraph:')
        self.in_para = str(input())
        if(not self.in_para):
            print('No input detected. Do you wish to try again? (Yes(Y)/No(N))')
            response = str(input())
            if(response == str('Y')):
                self.get_input()
            elif(response == str('N')):
                sys.exit()
            else:
                print('Invalid Response')
                exit
        else:
            print('You entered:')
            print(self.in_para)   
        

    def Convertpara(self):
        self.my_rules = rules()
        abbr = self.my_rules['text_conv_abbr']
        numbers = self.my_rules['text_conv_numbers']
        repeats = self.my_rules['text_conv_repeats']
        symbols = self.my_rules['text_conv_symbols']

        #Check each element in the paragraph and map to each rule in the dictionary
        #Check for numbers
        #Checking for abbreviations
        pro_para = self.in_para
        for key,value in abbr.items():
            pro_para = pro_para.replace(key,value)
        #Checking for Numbers
        pro_list = pro_para.split()
        i = int(0)
        while i <= len(pro_list)-1:
            for key,value in numbers.items():
                pro_list[i] = pro_list[i].replace(key,value)
            #Checking for repeats
            for key,value in repeats.items():
                pro_list[i] = pro_list[i].replace(key,value)
                if(pro_list[i] == str('3') or pro_list[i] == str('2')):
                    pro_list[i] = int(pro_list[i])
                    pro_list[i] = pro_list[i]*pro_list[i+1]
                    pro_list.remove(pro_list[i+1])
            #Checking for symbols
            for key,value in symbols.items():
                pro_list[i] = pro_list[i].replace(key,value)
                pro_list[i-1], pro_list[i] = pro_list[i], pro_list[i-1]
            
            i += 1
        self.out_para = " "
        self.out_para = self.out_para.join(pro_list)
        print('The output after processing is:')
        print(self.out_para)

#Defining rules to process the spoken paragraph
def rules():
    text_processing = {
        "text_conv_abbr" : {'C M':'CM', 'G K': 'GK', 'I Q': 'IQ'},
        "text_conv_numbers" : {'zero':'0','one':'1','two':'2','three':'3','four':'4','five':'5','six':'6','seven':'7','eight':'8','nine':'9','ten':'10','hundred':'100'},
        "text_conv_repeats" : {'double':'2', 'triple':'3'},
        "text_conv_symbols" : {'dollar':'$','dollars':'$','rupee':'₹','rupees':'₹','euro':'ē','euros':'ē'}
    }
    return text_processing


def sp():
    spoken2text = Speech2Text() #Class Object
    spoken2text.get_input() 
    spoken2text.Convertpara()

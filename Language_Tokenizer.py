from tkinter import *
from tkinter import messagebox
from tkinter import ttk


class Regex:
    def __init__(self,pattern):
        self.pattern = pattern
        self.tokens = []
    def match(self,text):
        if self.pattern=="\w+":
            i=0
            k=0                    
            print(text)
            flag_for_single_quotes=0
            flag_for_double_quotes=0
            while i<len(text):
              

                if text[i]==" " or text[i]=="." or text[i]=="(" or text[i]==")" or text[i]=="=" or text[i]=="+" or text[i]=="-" or text[i]=="*" or text[i]=="/" or text[i]=="%" or text[i]=="&" or text[i]=="|" or text[i]=="^" or text[i]=="~" or text[i]=="!" or text[i]=="<" or text[i]==">" or text[i]=="?" or text[i]==":" or text[i]==";" or text[i]=="," or text[i]=="[" or text[i]=="]" or text[i]=="{" or text[i]=="}" or text[i]=="\\" or text[i]=="'" or text[i]=='"':
                    
                    if  text[i]=='"':
                        while text[i+1]!='"' :
                            i+=1
                        i+=1
                        self.tokens.append(text[k:i+1])
                        if flag_for_double_quotes==1:
                            i+=1
                            k=i
                            flag_for_double_quotes=0
                            continue
                        
                    elif text[i]=="'":
                        while text[i+1]!="'":
                            i+=1
                        i+=1
                        self.tokens.append(text[k:i])
                        if flag_for_single_quotes==1:
                            i+=1
                            k=i
                            flag_for_single_quotes=0
                            continue

                    elif text[i]==".":
                        self.tokens.append(text[k:i])
                        self.tokens.append(".")
                        
                    elif text[i]=="(":
                        self.tokens.append(text[k:i])
                        self.tokens.append("(")
                        
                    elif text[i]==")":
                        self.tokens.append(text[k:i])
                        self.tokens.append(")")
                        
                    elif text[i]=="=":
                        self.tokens.append(text[k:i])
                        self.tokens.append("=")
                        
                    elif text[i]=="+":
                        self.tokens.append(text[k:i])
                        self.tokens.append("+")
                        
                    elif text[i]=="-":
                        self.tokens.append(text[k:i])
                        self.tokens.append("-")
                        
                    elif text[i]=="*":
                        self.tokens.append(text[k:i])
                        self.tokens.append("*")
                        
                    elif text[i]=="/":
                        self.tokens.append(text[k:i])
                        self.tokens.append("/")
                        
                    elif text[i]=="%":
                        self.tokens.append(text[k:i])
                        self.tokens.append("%")
                        
                    elif text[i]=="&":
                        self.tokens.append(text[k:i])
                        self.tokens.append("&")
                        
                    elif text[i]=="|":
                        self.tokens.append(text[k:i])
                        self.tokens.append("|")
                        
                    elif text[i]=="^":
                        self.tokens.append(text[k:i])
                        self.tokens.append("^")
                       
                    elif text[i]=="~":
                        self.tokens.append(text[k:i])
                        self.tokens.append("~")
                        
                    elif text[i]=="!":
                        self.tokens.append(text[k:i])
                        self.tokens.append("!")
                   
                    elif text[i]=="<":
                        self.tokens.append(text[k:i])
                        self.tokens.append("<")
                  
                    elif text[i]==">":
                        self.tokens.append(text[k:i])
                        self.tokens.append(">")
                        #i+=1
                    elif text[i]=="?":
                        self.tokens.append(text[k:i])
                        self.tokens.append("?")
                        #i+=1
                    elif text[i]==":":
                        self.tokens.append(text[k:i])
                        self.tokens.append(":")
                        #i+=1
                    elif text[i]==";":
                        self.tokens.append(text[k:i])
                        self.tokens.append(";")
                        #i+=1
                    elif text[i]==",":
                        self.tokens.append(text[k:i])
                        self.tokens.append(",")
                        #i+=1
                    elif text[i]=="[":
                        self.tokens.append(text[k:i])
                        self.tokens.append("[")
                        #i+=1
                    elif text[i]=="]":
                        self.tokens.append(text[k:i])
                        self.tokens.append("]")
                        #i+=1
                    elif text[i]=="{":
                        self.tokens.append(text[k:i])
                        self.tokens.append("{")
                        #i+=1
                    elif text[i]=="}":
                        self.tokens.append(text[k:i])
                        self.tokens.append("}")
                        #i+=1
                    
                    else:
                        self.tokens.append(text[k:i])
                        
                    k=i+1
                i+=1
                if i==len(text):
                    break
                if(text[i]=='"'):
                    flag_for_double_quotes=1
                    continue
                if(text[i]=="'"):
                    flag_for_single_quotes=1
                    continue
                #i+=1
                

            self.tokens.append(text[k:])
            
        return self.tokens


def formatting_output(new):
    new= [item.strip() for item in new if item]
    new = [item for item in new if item != '\n' or new.count(item) > 1]  # Remove standalone '\n'
    return "\n".join(new)

def is_empty_source_code(source_code):  
  for char in source_code:
    if not char.isspace():  # Efficiently check for non-whitespace characters
      return True
  return False
def tokenize_func():
    button_text = Tokenize_Button.cget("text")
    if button_text=="Clear":
        Source_code_text.delete("1.0", END)  # "1.0" is the first line and "END" is the end
        Source_code_label.configure(text="Source Code:")
        Tokenize_Button.configure(text="Tokenize")
        return

    if combo.get()=="":
        messagebox.showerror(title="Error",message="Select Language to tokenize")
        return
    source_code = Source_code_text.get("1.0", END)  # "1.0" is the first line and "END" is the end
    flag=0
    for i in source_code:
        if i!="\n" or is_empty_source_code(source_code):
            flag=1
            break
    
    if flag:
        new=Regex("\w+").match(source_code)
        new=formatting_output(new)
        Source_code_text.delete("1.0", END)  # "1.0" is the first line and "END" is the end
        Source_code_text.insert(END, new)   
        Source_code_label.configure(text="Tokenized Code:")
        Tokenize_Button.configure(text="Clear")
    else:
        messagebox.showerror(title="Error",message="Enter some source code")

root = Tk()
root.title("Language Tokenizer")
root.geometry("500x500")
root.resizable(False, False)

Title_Label = Label(root, text="Language Tokenizer", font=("Helvetica", 20,"bold"),fg="red").place(x=130, y=10)
SubTitle_Label = Label(root, text="by   22K-4218 , 22K-4547", font=("Helvetica", 15,"bold")).place(x=145, y=50)

Source_code_label = Label(root, text="Source Code:", font=("Helvetica", 15,"bold"))
Source_code_label.place(x=20, y=120)

Source_code_text = Text(root, height=7, width=57)
Source_code_text.place(x=20, y=150)

Language_input_label = Label(root, text="Language Input: ", font=("Helvetica", 15,"bold"))
Language_input_label.place(x=20, y=280)



combo = ttk.Combobox(state="readonly",values=["Python","Urdu"])
combo.place(x=180, y=285)


Tokenize_Button = Button(root, text="Tokenize",command=tokenize_func, font=("Helvetica", 15,"bold"),fg="Green",width=8,height=1)
Tokenize_Button.place(x=220, y=320)

root.mainloop()
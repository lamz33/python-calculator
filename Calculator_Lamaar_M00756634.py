from tkinter import *
import threading
import pygame       #for sound

class Calculator(Tk):
    def __init__(self): #constructor
        super().__init__() #allow access of this class outside of the class
        threading.Thread.__init__(self) #initialising threading
        self.title('Calculator')            #creating the window of the calculator
        self.geometry("225x350")
        self.txt = ('CenturyGothic 17')
        self.config(background="black")
        
        self.label_text = 'Maths Calculator'

        #creating the frames to place the widgets on
        self.border = Frame(self, bd=4, relief=RAISED, bg='black')  
        self.border.pack()

        self.label = Label(self, text=self.label_text, font=self.txt) #to place title
        self.label.pack()

        self.output_box = Entry(self, width=35, borderwidth=5)
        self.output_box.pack()

        self.button_box = LabelFrame(self, relief=RAISED, bg='powderblue', font=self.txt)
        self.button_box.pack()

        #operation buttons
        #lambda is used to call two functions from one button
        self.add = Button(self.button_box, text='+', height=2, width=6, command=lambda:[self.add_func(), self.sound3()], bg='powderblue')
        self.add.grid(column=0,row=0)

        self.minus = Button(self.button_box, text='-', height=2, width=6, command=lambda:[self.subtract_func(), self.sound3()],  bg='powderblue')
        self.minus.grid(column=1,row=0)

        self.multiplication = Button(self.button_box, text='*', height=2, width=6,command=lambda:[self.multiply_func(), self.sound3()],  bg='powderblue')
        self.multiplication.grid(column=2,row=0)

        self.division = Button(self.button_box, text='/', height=2, width=6,command=lambda:[self.divide_func(), self.sound3()], bg='powderblue')
        self.division.grid(column=3,row=0)

        self.squared = Button(self.button_box, text='x^2', height=3, width=6, command=self.squared_func,  bg='powderblue')
        self.squared.grid(column=3,row=1)

        self.cubed = Button(self.button_box, text='x^3', height=3, width=6, command=self.cubed_func, bg='powderblue')
        self.cubed.grid(column=3,row=2)

        self.clear = Button(self.button_box, text='Clear', height=3, width=6, command=self.clear_func, bg='lightyellow')
        self.clear.grid(column=2,row=4)

        self.equal = Button(self.button_box, text='=', height=7, width=6, command=lambda:[self.equal_func(), self.sound2()], bg='powderblue')
        self.equal.grid(column=3,row=3, rowspan=20)

        self.exit = Button(self.button_box, text='exit', height=3, width=6, bg='red', command=self.exit)
        self.exit.grid(column=0,row=4)

        #lambda is used to be able to call two functions at once from button click
    
        #number buttons
        self.one = Button(self.button_box, text='1', height=3, width=6, command=lambda:[self.press(1), self.sound()])
        self.one.grid(column=0,row=1)

        self.two = Button(self.button_box, text='2', height=3, width=6, command=lambda:[self.press(2), self.sound()])
        self.two.grid(column=1,row=1)

        self.three= Button(self.button_box, text='3', height=3, width=6, command=lambda:[self.press(3), self.sound()])
        self.three.grid(column=2,row=1)

        self.four = Button(self.button_box, text='4', height=3, width=6, command=lambda:[self.press(4), self.sound()])
        self.four.grid(column=0,row=2)

        self.five = Button(self.button_box, text='5', height=3, width=6, command=lambda:[self.press(5), self.sound()])
        self.five.grid(column=1,row=2)

        self.six = Button(self.button_box, text='6', height=3, width=6, command=lambda:[self.press(6), self.sound()])
        self.six.grid(column=2,row=2)

        self.seven = Button(self.button_box, text='7', height=3, width=6, command=lambda:[self.press(7), self.sound()])
        self.seven.grid(column=0,row=3)

        self.eight = Button(self.button_box, text='8', height=3, width=6, command=lambda:[self.press(8), self.sound()])
        self.eight.grid(column=1,row=3)

        self.nine = Button(self.button_box, text='9', height=3, width=6, command=lambda:[self.press(9), self.sound()])
        self.nine.grid(column=2,row=3)

        self.zero = Button(self.button_box, text='0', height=3, width=6, command=lambda:[self.press(0), self.sound()])
        self.zero.grid(column=1,row=4)

    #intializes mixer module of pygame to be able to use sound
    pygame.mixer.init()

    #created functions for noise
    def sound(self):
        pygame.mixer.music.load("button.wav")
        pygame.mixer.music.play(loops=0)

    def sound2(self):
        pygame.mixer.music.load("answer.wav")
        pygame.mixer.music.play(loops=0)

    def sound3(self):
        pygame.mixer.music.load("swoosh.wav")
        pygame.mixer.music.play(loops=0)
        
    #function for pressing numbers
    def press(self, number):
        current = self.output_box.get()       #.get() gets the number that is currently in the output box
        self.output_box.delete(0, END)      # means to delete the first to the last character that is in the text box
        self.output_box.insert(0, str(current) + str(number))

    #function to clear the caluclator
    def clear_func(self):
        self.output_box.delete(0 , END)
        
    #this function retrieve the second number entered, clears the box and then 
    #finds the function that has been called and executes its operation
    def equal_func(self):
        digit_two = DoubleVar() #float
        digit_two = self.output_box.get()
        self.output_box.delete(0, END)
        if operation == "addition":
            answer = float(num1) + float(digit_two)
            self.output_box.insert(0, answer)
        elif operation == "subtraction":
            answer = float(num1) - float(digit_two)
            self.output_box.insert(0, answer)
        elif operation == "multiply":
            answer = float(num1) * float(digit_two)
            self.output_box.insert(0, answer)
        elif operation == "divide":
            answer = float(num1) / float(digit_two)
            self.output_box.insert(0, answer)
        elif operation == "squared":
            digit_two = 0
            answer = float(num1) ** 2
            self.output_box.insert(0, answer)
        elif operation == "cubed":
            digit_two = 0
            answer = float(num1) ** 3
            self.output_box.insert(0, answer)

    #function to close calculator and end threads
    def exit(self):
        self.destroy()
        add_thread.join()
        subtract_thread.join()
        multiply_thread.join()
        divide_thread.join()
        squared_thread.join()
        cubed_thread.join()
        print("\nExiting threads")
        print(threading.enumerate())
        
    #each of these functions take the first number and stores it in digit one, it 
    #then clears the output box for the second digit to be entered
    def add_func(self):
        digit_one = DoubleVar()     #states that the digit_one variable is a float(double var)
        digit_one = self.output_box.get()
        global num1     #global command is called so this variable can be used
        global operation
        operation = "addition"
        num1 = digit_one
        self.output_box.delete(0, END)

    def subtract_func(self):
        digit_one = DoubleVar()
        digit_one = self.output_box.get()
        global num1
        global operation
        operation = "subtraction"
        num1 = digit_one
        self.output_box.delete(0, END)

    def multiply_func(self):
        digit_one = DoubleVar()
        digit_one = self.output_box.get()
        global num1
        global operation
        operation = "multiply"
        num1 = digit_one
        self.output_box.delete(0, END)

    def divide_func(self):
        digit_one = DoubleVar()
        digit_one = self.output_box.get()
        global num1
        global operation
        operation = "divide"
        num1 = digit_one
        self.output_box.delete(0, END)
    

    def squared_func(self):
        digit_one = DoubleVar()
        digit_one = self.output_box.get()
        global num1
        global operation
        operation = "squared"
        num1 = digit_one
        self.output_box.delete(0, END)
        

    def cubed_func(self):
        digit_one = DoubleVar()
        digit_one = self.output_box.get()
        global num1
        global operation
        operation = "cubed"
        num1 = digit_one
        self.output_box.delete(0, END)
        
#creates an instance of the Calculator class 
window = Calculator()

#creating the threads
add_thread = threading.Thread(target=window.add_func)
add_thread.start()

subtract_thread = threading.Thread(target=window.subtract_func)
subtract_thread.start()

multiply_thread = threading.Thread(target=window.multiply_func)
multiply_thread.start()

divide_thread = threading.Thread(target=window.divide_func)
divide_thread.start()

squared_thread = threading.Thread(target=window.squared_func)
squared_thread.start()

cubed_thread = threading.Thread(target=window.cubed_func)
cubed_thread.start()



#naming the threads

add_thread.name = "ADD THREAD"
subtract_thread.name = "MINUS THREAD"
multiply_thread.name =  "MULTIPLY THREAD"
divide_thread.name = "DIVIDE THREAD"
squared_thread.name = "SQUARED THREAD"
cubed_thread.name = "CUBED THREAD"



#to display the running threads
print(threading.enumerate())

#runs the calculator
window.mainloop()


    



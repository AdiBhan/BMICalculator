#
# App: BMICalculator
# Version 1.0.2
# Author: Adi Bhan
#

from tkinter import *
from settings import *
import time
from tkinter import messagebox

class App:
    
    def __init__(self, master):
        
        self.master = master
    
        self.header = Label(self.master,
                          text = ('BMICalculator ' + Version),
                          font=('Verdana 15 bold'),
                          background = 'tomato',
                          foreground= 'black',
                          borderwidth= 1, 
                          relief="solid",
                          width = 20,
                          
                          height = 1,
                          )

        self.header.place(x = 90, y = 5)
          
        self.Height_Scale = Scale(
                    from_= 0, 
                    to = 360, 
                    bg = color2, 
                    fg = 'white', 
                    borderwidth= 1, 
                    relief="solid",
                    length = 250, 
                    orient= HORIZONTAL)

        self.Height_Scale.place(x=100, y=60)

        self.Weight_Scale = Scale(
                    from_= 0, 
                    to = 360, 
                    bg = 'Purple', 
                    fg = 'white', 
                    borderwidth= 1, 
                    relief="solid", 
                    length = 250, 
                    orient= HORIZONTAL)

        self.Weight_Scale.place(x=100, y=130)

# Labels to help user identify the height and weight scale

        self.Height_Label = Label(
                    text = "Height (Inches): ", 
                    bg = background_color,
                    fg = 'White',
                    font = (font, text_fontsize),
                    )

        self.Height_Label.place(x = 190, y = 108)

        self.Weight_Label = Label(
                text = "Weight (lbs): ", 
                bg = background_color,
                fg = 'White',
                font = (font, text_fontsize),
                )

        self.Weight_Label.place(x = 190, y = 35)
      
# Submit button runs the BMICalc Function when clicked    
    
        self.Submit = Button(self.master, 
                text = 'Calculate BMI!', 
                width = 13, 
                command = self.BMICalc,
                background = 'black',
                fg = 'White',
                pady = 5
                ).place(x=180, y=180,)

## Close button allows user to exit the GUI

        self.CLOSE_Button = Button(
                self.master, 
                text = 'CLOSE',
                font = (font, 12),
                background = 'Red',
                fg = 'white',
                command = self.master.quit,
                ).place(x = 200 , y = 350)

    
        self.master.title("BMICalculator")
         
        self.master.geometry('500x400') 

        self.master.configure(background = background_color, borderwidth= 5, relief="groove")

        self.master.resizable(False, False)

        self.master.iconbitmap('c:/Testing/BMICALC_ICON.ICO')
 
    def BMICalc(self):
           
    # If user inputs 0 as value for weight or height, program will throw an error message at them     
    
        time.sleep(.2)
        if self.Height_Scale.get() == 0 or self.Weight_Scale.get() == 0:
            messagebox.showwarning("Error 101", "Your height and/or weight value is currently set to 0. Please change it to an appropriate number!")
    
        else:    
    
    # Basic CDC BMI Formula 
    
            Formula = (((float(self.Weight_Scale.get()) / (float(self.Height_Scale.get())) ** 2) ) * 703 )
    
            Label(text = "Your BMI is " + str(round(float(Formula),2)) + "!").place(x=180, y=235,)
    
    ## The formula below calculating the amount of pounds a user needs to obtain an healthy BMI (Reach 25 BMI). 
    ## I solved this by reverse engineering the CDC BMI Formula. This formula assumes that the user's height stays the same (target audience is adults).
    
            BMI_To_Weight_Formula = str(abs(round(float(((((18.5 - Formula ) / 703) * (float(self.Height_Scale.get())) ** 2))),2)))
    
    ## Based on the user's BMI, the program will display special messages telling them what BMI Weight Status they are in and how many pounds they must lose to reach a lower weight status.
    
            Weight_Gain_Message = "You must gain " + BMI_To_Weight_Formula + " pounds to reach a healthy BMI!"
            Weight_Loss_Message =  "You must lose " + BMI_To_Weight_Formula + " pounds to reach a healthy BMI!"
       
    ## User is sent different messages based on their BMI

            if Formula < 18.5:
        
                Label(text = "WARNING: Underweight! Your BMI is below 18.5 and therefore you are underweight.", foreground = 'Blue').place(x=10, y=275,)
                    
                Label(text = Weight_Gain_Message, foreground = 'Blue').place(x=10, y=295,)
                        
            elif 18.5 <= Formula <= 24.9:
        
                Label(text = "CONGRATS: Healthy! You are at a healthy BMI.", foreground = 'Green').place(x=10, y=275,)
            
            elif 25 <= Formula <= 29.9:
        
                Label(text = "WARNING: Overweight! You are overweight.", foreground = 'Red').place(x=10, y=275,)
        
                Label(text = Weight_Loss_Message, foreground = 'Red').place(x=10, y=295,)

            elif Formula >= 30:
        
                Label(text = "SEVERE WARNING: OBESE! You BMI is above 30 and therefore you are obese.", foreground = 'Dark Red').place(x=10, y=275,)
               
                Label(text = Weight_Loss_Message, foreground = 'Dark Red').place(x=10, y=295,)

def main(): 
    
    root = Tk()
    
    GUI = App(root)
    
    root.mainloop()

if __name__ == '__main__':
    main()
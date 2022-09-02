from fileinput import close
from tkinter import messagebox
from tkinter import *

''' Author: Adi Bhan'''
''' Description: Using tkinter, I created a simple GUI that takes the a user's input and displays their BMI along with the number of pounds they must lose to become healthy'''
''' Version: 1.00'''

# Placeholders

Version = '1.0.1'
font = 'Arial'
background_color = 'green'
header_fontsize = 15
text_fontsize = 9

GUI = Tk()

## Setting the size , color, title, logo and border of the GUI

# Title
GUI.title('BMI Calculator')  
 
# Background Size
GUI.geometry('500x350') 

 # Background color and border
GUI.configure(background = background_color, borderwidth= 5, relief="groove")

GUI.resizable(False, False)

# Logo
GUI.iconbitmap('c:/Testing/BMICALC_ICON.ICO')

## Welcome Header

GUI_WelcomeHeader = Label(GUI,
                          text = ('BMICalculator ' + Version),
                          font=(font, header_fontsize),
                          background = 'tomato',
                          foreground= 'black',
                          borderwidth= 1, 
                          relief="solid",
                          ).place(x = 150, y = 5)

# Height and Weight scales 

Height_Scale = Scale(
                    from_= 0, 
                    to = 360, 
                    bg = background_color, 
                    fg = 'white', 
                    borderwidth= 1, 
                    relief="solid",
                    length = 250, 
                    orient= HORIZONTAL)

Height_Scale.place(x=100, y=60)

Weight_Scale = Scale(
                    from_= 0, 
                    to = 360, 
                    bg = background_color, 
                    fg = 'white', 
                    borderwidth= 1, 
                    relief="solid", 
                    length = 250, 
                    orient= HORIZONTAL)

Weight_Scale.place(x=100, y=130)

# Labels to help user identify the height and weight scale

Height_Label = Label(
    text = "Height (Inches): ", 
    bg = background_color,
    fg = 'White',
    font = (font, text_fontsize),
    ).place(x = 190, y = 35)

Weight_Label = Label(
    text = "Weight (lbs): ", 
    bg = background_color,
    fg = 'White',
    font = (font, text_fontsize),
    ).place(x = 190, y = 108)

## Function calculates BMI using the CDC BMI Formula (https://www.cdc.gov/healthyweight/assessing/bmi/adult_bmi/index.html)

def BMICalc():
    
# If user inputs 0 as value for weight or height, program will throw an error message at them
    
    if Height_Scale.get() == 0 or Weight_Scale.get() == 0:
        messagebox.showwarning("Error 101", "Your height and/or weight value is currently set to 0. Please change it to an appropriate number!")
    
    else:    
    
    # Basic CDC BMI Formula 
    
        Formula = (((float(Weight_Scale.get()) / (float(Height_Scale.get())) ** 2) ) * 703 )
    
        Label(text = "Your BMI is " + str(round(float(Formula),2)) + "!").place(x=180, y=215,)
    
    ## The formula below calculating the amount of pounds a user needs to obtain an healthy BMI (Reach 25 BMI). 
    ## I solved this by reverse engineering the CDC BMI Formula. This formula assumes that the user's height stays the same (target audience is adults).
    
        BMI_To_Weight_Formula = str(abs(round(float(((((18.5 - Formula ) / 703) * (float(Height_Scale.get())) ** 2))),2)))
    
    ## Based on the user's BMI, the program will display special messages telling them what BMI Weight Status they are in and how many pounds they must lose to reach a lower weight status.
    
        Weight_Gain_Message = "You must gain " + BMI_To_Weight_Formula + " pounds to reach a healthy BMI!"
        Weight_Loss_Message =  "You must lose " + BMI_To_Weight_Formula + " pounds to reach a healthy BMI!"
       
    ## User is sent different messages based on their BMI

        if Formula < 18.5:
        
            Label(text = "WARNING: Underweight! Your BMI is below 18.5 and therefore you are underweight.", foreground = 'Blue').place(x=10, y=245,)
                    
            Label(text = Weight_Gain_Message, foreground = 'Blue').place(x=10, y=265,)
                        
        elif 18.5 <= Formula <= 24.9:
        
            Label(text = "CONGRATS: Healthy! You are at a healthy BMI.", foreground = 'Green').place(x=10, y=245,)
            
        elif 25 <= Formula <= 29.9:
        
            Label(text = "WARNING: Overweight! You are overweight.", foreground = 'Red').place(x=10, y=245,)
        
            Label(text = Weight_Loss_Message, foreground = 'Red').place(x=10, y=265,)

        elif Formula >= 30:
        
            Label(text = "SEVERE WARNING: OBESE! You BMI is above 30 and therefore you are obese.", foreground = 'Dark Red').place(x=10, y=245,)
               
            Label(text = Weight_Loss_Message, foreground = 'Dark Red').place(x=10, y=265,)
   
# Submit button runs the BMICalc Function when clicked    
    
Submit = Button(GUI, 
                text = 'Calculate BMI!', 
                width = 13, 
                command = BMICalc 
                ).place(x=180, y=180,)

## Close button allows user to exit the GUI

CLOSE_Button = Button(
                      GUI, 
                      text = 'CLOSE',
                      font = (font, 12),
                      background = 'Red',
                      command = GUI.quit, 
                      ).pack(side= BOTTOM)

GUI.mainloop()

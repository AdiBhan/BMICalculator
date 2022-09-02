from fileinput import close
from tkinter import *
from tkinter import messagebox

''' Author: Adi Bhan'''
''' Description: Using tkinter, I created a simple GUI that takes the a user's input and displays their BMI along with the number of pounds they must lose to become healthy'''
''' Version: 1.00'''

# Placeholders

Version = '1.00'
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



## A welcome header that shares the current version with the user

GUI_WelcomeHeader = Label(GUI,
                          text = ('BMICalculator ' + Version),
                          font=(font, header_fontsize),
                          background = 'tomato',
                          foreground= 'black',
                          borderwidth= 1, 
                          relief="solid",
                          ).place(x = 150, y = 5)



# Using scales to get user input for weight and height

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

# Labels for weight and height scale

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

## Function calculates BMI using the CDC BMI Formula

def BMICalc():
    
    # Basic CDC BMI Formula 
    
    Formula = (((float(Weight_Scale.get()) / (float(Height_Scale.get())) ** 2) ) * 703 )
    
    Label(text = "Your BMI is " + str(round(float(Formula),2)) + "!").place(x=180, y=215,)
    
## The formula below calculating the amount of pounds a user needs to obtain an healthy BMI (Reach 25 BMI). 
    ## I solved this by reverse engineering the CDC BMI Formula. This formula assumes that the user's height stays the same (target audience is adults).
    
    BMI_To_Weight_Formula = str(abs(round(float(((((18.5 - Formula ) / 703) * (float(Height_Scale.get())) ** 2))),2)))
    
## Based on the user's BMI, the program will display special messages telling them what BMI Weight Status they are in and how many pounds they must lose to reach a lower weight status.
    
    Weight_Gain_Message = "You must gain " + BMI_To_Weight_Formula + " pounds to reach a healthy BMI!"
    Weight_Loss_Message =  "You must lose " + BMI_To_Weight_Formula + " pounds to reach a healthy BMI!"
    
    
    ## Gives an error message if Height or Weight is 0
    

    
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
        
        
# An submit button which when a user clicks runs the BMICalc Function (Scroll Up)

Submit = Button(GUI, 
                text = 'Calculate BMI!', 
                width = 13, 
                command = BMICalc 
                ).place(x=180, y=180,)

## A close button that allows the user to quit the GUI
CLOSE_Button = Button(
                      GUI, 
                      text = 'CLOSE',
                      font = (font, 12),
                      background = 'Red',
                      command = GUI.quit, 
                      ).pack(side= BOTTOM)

GUI.mainloop()



    


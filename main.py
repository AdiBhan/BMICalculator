'''
 App: BMICalculator 
 Description: Using tkinter, I created a simple GUI that takes the a user's input and displays their BMI along with the number of pounds they must lose to become healthy
 Version 1.0.2
 Author: Adi Bhan 
'''

from tkinter import *
from settings import *
import time
from tkinter import messagebox

class App:
      
    def __init__(self, master):
        
        ''' Initializing GUI, title, size, icon, '''
        
        self.master = master
    
        master.title("BMICalculator")
         
        master.geometry('500x400') 

        master.configure(background = background_color, borderwidth= 5, relief="groove")

        master.resizable(False, False)

        master.iconbitmap('c:/Testing/BMICALC_ICON.ICO')
              
    def Widgets(self):
        
        ''' Widgets object contains all of the widgets (exception - Metric Converter Widget)'''
        
        self.header = Label(self.master,
                          text = ('BMICalculator ' + Version),
                          font=('Verdana 15 bold'),
                          background = 'white',
                          foreground= 'black',
                          borderwidth= 1, 
                          relief="solid",
                          width = 20,
                          
                          height = 1,
                          )

        self.header.place(x = 90, y = 5)
        
# Height and Weight widgets
          
        self.Weight_Scale = Scale(
                    from_= 0, 
                    to = 360, 
                    bg = color2, 
                    fg = 'white', 
                    borderwidth= 1, 
                    relief="solid",
                    length = 250, 
                    orient= HORIZONTAL)

        self.Height_Scale = Scale(
                    from_= 0, 
                    to = 360, 
                    bg = 'Purple', 
                    fg = 'white', 
                    borderwidth= 1, 
                    relief="solid", 
                    length = 250, 
                    orient= HORIZONTAL)

        self.Height_Scale.place(x=100, y=130)
        self.Weight_Scale.place(x=100, y=60)

# Labels to help user identify the height and weight scale

        self.Height_Label = Label(
                    text = "Height (Inches): ", 
                    bg = background_color,
                    fg = 'White',
                    font = (font, text_fontsize),
                    )

        self.Weight_Label = Label(
                text = "Weight (lbs): ", 
                bg = background_color,
                fg = 'White',
                font = (font, text_fontsize),
                )

        self.Height_Label.place(x = 190, y = 108)
        self.Weight_Label.place(x = 190, y = 35)
             
# Submit button when user has selected height and wieght 
    
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

    def BMICalc(self):
        
        ''' Method calculates BMI (Both Metric and Imperial) and displays BMI and how much weight lose/gain needed to reach a healthy BMI'''
                    
    # If user inputs 0 as value for weight or height, program will throw an error message at them     
 
        if self.Height_Scale.get() == 0 or self.Weight_Scale.get() == 0:
            messagebox.showwarning("Error 101", "Your height and/or weight value is currently set to 0. Please change it to an appropriate number!")
    
        else:    
            
            if metric == False:
                
            # Basic Imperial CDC BMI Formula for calculating BMI
    
                Formula = (((float(self.Weight_Scale.get()) / (float(self.Height_Scale.get())) ** 2) ) * 703 )
    
                self.BMIMessage = Label(text = "Your BMI is " + str(round(float(Formula),2)) + "!")
                
                self.BMIMessage.place(x=180, y=235,)
                
                # Destroys message after 4 seconds
                 
                self.BMIMessage.after(delete_delay, self.BMIMessage.destroy )
                
             ## The formula below calculating the amount of pounds a user needs to obtain an healthy BMI (Reach 25 BMI). 
             ## I solved this by reverse engineering the CDC BMI Formula. This formula assumes that the user's height stays the same (target audience is adults).
    
                BMI_To_Weight_Formula = str(abs(round(float(((((18.5 - Formula ) / 703) * (float(self.Height_Scale.get())) ** 2))),2)))
            
            if metric == True:
                
            # Basic Metric CDC BMI Formula for calculating BMI

                 Formula = (((float(self.Weight_Scale.get()) / (float(self.Height_Scale.get() / 100)) ** 2) ) )
                 
                 self.BMIMessage = Label(text = "Your BMI is " + str(round(float(Formula),2)) + "!")
                 
                 self.BMIMessage.place(x=180, y=235,)
                
                 
                # Using the destroy method to delete the text after 4 seconds 
                 
                 self.BMIMessage.after(delete_delay, self.BMIMessage.destroy )
                 
                 BMI_To_Weight_Formula = str(abs(round(float(((((18.5 - Formula )) * (float(self.Height_Scale.get())) ** 2))),2)))
                
    ## Based on the user's BMI, the program will display special messages telling them what BMI Weight Status they are in and how many pounds they must lose to reach a lower weight status.
    
            Weight_Gain_Message = "You must gain " + BMI_To_Weight_Formula + " pounds to reach a healthy BMI!"
            Weight_Loss_Message =  "You must lose " + BMI_To_Weight_Formula + " pounds to reach a healthy BMI!"
       
    ## User is sent different messages based on their BMI
            
            if Formula < 18.5:
        
                self.warninglabel = Label(text = "WARNING: Underweight! Your BMI is below 18.5 and therefore you are underweight.", foreground = 'Blue')
                self.warninglabel.place(x=10, y=275,)

                                     
                self.warninglabel2 = Label(text = Weight_Gain_Message, foreground = 'Blue')
                self.warninglabel2.place(x=10, y=295,)
                
                self.warninglabel.after(delete_delay, self.warninglabel.destroy )
                self.warninglabel2.after(delete_delay, self.warninglabel2.destroy )
                 
            elif 18.5 <= Formula <= 24.9:
        
                self.warninglabel = Label(text = "CONGRATS: Healthy! You are at a healthy BMI.", foreground = 'Green')
                self.warninglabel.place(x=10, y=275,)
                
                self.warninglabel.after(delete_delay, self.warninglabel.destroy)
                self.warninglabel2.after(delete_delay, self.warninglabel2.destroy)
                
                
            elif 25 <= Formula <= 29.9:
        
                self.warninglabel = Label(text = "WARNING: Overweight! You are overweight.", foreground = 'Red')
                self.warninglabel.place(x=10, y=275,)
                
                self.warninglabel2 = Label(text = Weight_Loss_Message, foreground = 'Red')
                self.warninglabel2.place(x=10, y=295,)
                
                self.warninglabel.after(delete_delay, self.warninglabel.destroy)
                self.warninglabel2.after(delete_delay, self.warninglabel2.destroy)
                
            elif Formula >= 30:
        
                self.warninglabel = Label(text = "SEVERE WARNING: OBESE! You BMI is above 30 and therefore you are obese.", foreground = 'Dark Red')
                self.warninglabel.place(x=10, y=275,)
                
                self.warninglabel2 = Label(text = Weight_Loss_Message, foreground = 'Dark Red')
                self.warninglabel2.place(x=10, y=295,)
                
                self.warninglabel.after(delete_delay, self.warninglabel.destroy )
                self.warninglabel2.after(delete_delay, self.warninglabel2.destroy )
                              
    def Converter_To_Metric(self):
                        
            self.Weight_Label.configure(text = 'Weight (Kg): ')
            self.Height_Label.configure(text = 'Height (cm):')
            self.MetricButton.configure(text = 'SWITCH TO IMPERIAL', bg = 'black')

            global metric
            metric = True
            
    def Converter_To_Imperial(self):
            
            self.Weight_Label.configure(text = 'Weight (lbs): ')
            self.Height_Label.configure(text = 'Height (Inches):')
            self.MetricButton.configure(text = 'SWITCH TO METRIC', bg = 'black')
            
            global metric
            metric = False
            
    def Metric(self):
            
            self.MetricButton = Button( 
                text = 'SWITCH TO METRIC', 
                background = 'black',
                fg = 'White',
                pady = 5,
                command = self.Converter_To_Metric if metric == False else self.Converter_To_Imperial(),
                )
            
            self.MetricButton.place(x=350, y=350)    
            
if __name__ == '__main__':
    root = Tk()
    
    GUI = App(root)
    
    GUI.Metric()
    
    GUI.Widgets()
    
    root.mainloop()
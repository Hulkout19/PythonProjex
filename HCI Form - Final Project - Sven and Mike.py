from tkinter import *

import tkinter

#Sven and Michael

class MyGUI:
    def __init__(self):
        
        
        self.screen = tkinter.Tk()
        
        
        def malesel():
            
            #self.prof1.place_forget()
            #self.prof1a.place_forget()
            #self.prof2.place_forget()
            #self.prof2a.place_forget()
            #self.prof3.place_forget()
            #self.prof3a.place_forget()
            #self.prof4.place_forget()
            #self.prof4a.place_forget()
            
            global x
            self.x = 25

            self.male.config(state="disabled")
            self.female.config(state="normal")
            
            self.female.place_forget()

            #Button Init
            self.reset_text = tkinter.Label(self.screen, text = "Unsatisfied? Press below to try again!", fg = "black")
            self.reset_text.place(x = 10, y = 620)
            self.reset = tkinter.Button(self.screen, text = "Reset", width = "25", height = "2", command = reset, bg = "grey")
            self.reset.place(x = 15, y = 650)
            
            #Dessert init
            self.des_text = tkinter.Label(self.screen, text = "Please select the type of flower you prefer: ")
            self.des_text.place(x = 15, y = 130)
            
            self.left1 = tkinter.Button(self.screen, text = "Dicentra", width = "25", height = "2", command = l1, bg = "grey")
            self.left1.place(x = 15, y = 150)

            self.right1 = tkinter.Button(self.screen, text = "Rose", width = "25", height = "2", command = r1, bg = "grey")
            self.right1.place(x = 245, y = 150)
            
            #Date init
            self.dat_text = tkinter.Label(self.screen, text = "Please select the type of car you would like your partner to drive: ")
            self.dat_text.place(x = 15, y = 190)
            
            self.left2 = tkinter.Button(self.screen, text = "Bugatti", width = "25", height = "2", command = l2, bg = "grey")
            self.left2.place(x = 15, y = 210)

            self.right2 = tkinter.Button(self.screen, text = "One that runs", width = "25", height = "2", command = r2, bg = "grey")
            self.right2.place(x = 245, y = 210)

            #Favorite Foods
            self.foo_text = tkinter.Label(self.screen, text = "Please select the date you would prefer: ")
            self.foo_text.place(x = 15, y = 250)
            
            self.left3 = tkinter.Button(self.screen, text = "Long Walk on the Beach", width = "25", height = "2", command = l3, bg = "grey")
            self.left3.place(x = 15, y = 270)

            self.right3 = tkinter.Button(self.screen, text = "Dinner and a Movie", width = "25", height = "2", command = r3, bg = "grey")
            self.right3.place(x = 245, y = 270)

            #Age
            self.age_text = tkinter.Label(self.screen, text = "Please select the age you would prefer: ")
            self.age_text.place(x = 15, y = 310)
            
            self.left4 = tkinter.Button(self.screen, text = "18-36ish", width = "25", height = "2", command = l4, bg = "grey")
            self.left4.place(x = 15, y = 330)

            self.right4 = tkinter.Button(self.screen, text = "37-65", width = "25", height = "2", command = r4, bg = "grey")
            self.right4.place(x = 245, y = 330)

            #Annual Income
            self.inc_text = tkinter.Label(self.screen, text = "Please select the annual income you prefer your partner to have: ")
            self.inc_text.place(x = 15, y = 370)
            
            self.left5 = tkinter.Button(self.screen, text = "$20,000-$50,000", width = "25", height = "2", command = l5, bg = "grey")
            self.left5.place(x = 15, y = 390)

            self.right5 = tkinter.Button(self.screen, text = "$60,000 - $100,000", width = "25", height = "2", command = r5, bg = "grey")
            self.right5.place(x = 245, y = 390)

            #Results
            self.res = tkinter.Button(self.screen, text = "See your future boo:", width = "25", height = "2", command = result, bg = "grey")
            self.res.place(x = 125, y = 440)

        def femalesel():
            
            #self.prof1.place_forget()
            #self.prof1a.place_forget()
            #self.prof2.place_forget()
            #self.prof2a.place_forget()
            #self.prof3.place_forget()
            #self.prof3a.place_forget()
            #self.prof4.place_forget()
            #self.prof4a.place_forget()
            
            global x
            
            self.x = 50
            
            self.female.config(state="disabled")
            self.male.config(state="normal")
            
            self.male.place_forget()

            #Button Init

            self.reset_text = tkinter.Label(self.screen, text = "Unsatisfied? Press below to try again!", fg = "black")
            self.reset_text.place(x = 10, y = 620)
            self.reset = tkinter.Button(self.screen, text = "Reset", width = "25", height = "2", command = reset, bg = "grey")
            self.reset.place(x = 15, y = 650)
            
            #Dessert init
            self.des_text = tkinter.Label(self.screen, text = "Please select the flavor of dessert you prefer: ")
            self.des_text.place(x = 15, y = 130)
            
            self.left1 = tkinter.Button(self.screen, text = "Vanilla", width = "25", height = "2", command = l1, bg = "grey")
            self.left1.place(x = 15, y = 150)

            self.right1 = tkinter.Button(self.screen, text = "Chocolate", width = "25", height = "2", command = r1, bg = "grey")
            self.right1.place(x = 245, y = 150)
            
            #Date init
            self.dat_text = tkinter.Label(self.screen, text = "Please select the Summer date you would prefer: ")
            self.dat_text.place(x = 15, y = 190)
            
            self.left2 = tkinter.Button(self.screen, text = "Horseback Riding", width = "25", height = "2", command = l2, bg = "grey")
            self.left2.place(x = 15, y = 210)

            self.right2 = tkinter.Button(self.screen, text = "Kayaking", width = "25", height = "2", command = r2, bg = "grey")
            self.right2.place(x = 245, y = 210)

            #Favorite Foods
            self.foo_text = tkinter.Label(self.screen, text = "Please select the meal you would prefer: ")
            self.foo_text.place(x = 15, y = 250)
            
            self.left3 = tkinter.Button(self.screen, text = "Big Mac(s)", width = "25", height = "2", command = l3, bg = "grey")
            self.left3.place(x = 15, y = 270)

            self.right3 = tkinter.Button(self.screen, text = "Salad", width = "25", height = "2", command = r3, bg = "grey")
            self.right3.place(x = 245, y = 270)

            #Age
            self.age_text = tkinter.Label(self.screen, text = "Please select the age you would prefer: ")
            self.age_text.place(x = 15, y = 310)
            
            self.left4 = tkinter.Button(self.screen, text = "18-30", width = "25", height = "2", command = l4, bg = "grey")
            self.left4.place(x = 15, y = 330)

            self.right4 = tkinter.Button(self.screen, text = "30-50ish", width = "25", height = "2", command = r4, bg = "grey")
            self.right4.place(x = 245, y = 330)

            #Annual Income
            self.inc_text = tkinter.Label(self.screen, text = "Please select the annual income you prefer your partner to have: ")
            self.inc_text.place(x = 15, y = 370)
            
            self.left5 = tkinter.Button(self.screen, text = "An Income", width = "25", height = "2", command = l5, bg = "grey")
            self.left5.place(x = 15, y = 390)

            self.right5 = tkinter.Button(self.screen, text = "Stay-at-Home", width = "25", height = "2", command = r5, bg = "grey")
            self.right5.place(x = 245, y = 390)

            #Results
            self.res = tkinter.Button(self.screen, text = "See your future boo:", width = "25", height = "2", command = result, bg = "grey")
            self.res.place(x = 125, y = 440)
            
            
        #Left Side

        
        def l1():
            self.left1.config(state="disabled")
            self.right1.config(state="normal")
            self.x += 1
            #print(self.x)

        def l2():
            
            self.left2.config(state="disabled")
            self.right2.config(state="normal")
            self.x += 1
            #print(self.x)

        def l3():
            
            self.left3.config(state="disabled")
            self.right3.config(state="normal")
            self.x += 1
            #print(self.x)

        def l4():
            
            self.left4.config(state="disabled")
            self.right4.config(state="normal")
            self.x += 1
            if self.x < 39:
                self.m = False
            elif self.x > 39:
                self.f = False
            #print(self.x)

        def l5():
            
            self.left5.config(state="disabled")
            self.right5.config(state="normal")
            self.x += 1
            #print(self.x)

        #Right Side
        
        def r1():
            self.right1.config(state="disabled")
            self.left1.config(state="normal")
            self.x -= 1
            #print(self.x)

        def r2():
            self.right2.config(state="disabled")
            self.left2.config(state="normal")
            self.x -= 1
            #print(self.x)

        def r3():
            self.right3.config(state="disabled")
            self.left3.config(state="normal")
            self.x -= 1
            #print(self.x)

        def r4():
            self.right4.config(state="disabled")
            self.left4.config(state="normal")
            self.x -= 1
            #age decider
            if self.x < 39:
                self.m = True
            elif self.x > 39:
                self.f = True
            
            #print(self.x)

        def r5():
            self.right5.config(state="disabled")
            self.left5.config(state="normal")
            self.x -= 1
            #print(self.x)


        
        def result():
            
            self.male.config(state = "disabled")
            self.female.config(state = "disabled")
            self.res.config(state = "disabled")
            
            self.left1.config(state = "disabled")
            self.left2.config(state = "disabled")
            self.left3.config(state = "disabled")
            self.left4.config(state = "disabled")
            self.left5.config(state = "disabled")
            
            self.right1.config(state = "disabled")
            self.right2.config(state = "disabled")
            self.right3.config(state = "disabled")
            self.right4.config(state = "disabled")
            self.right5.config(state = "disabled")
            #for female
            if self.x >= 45 and self.x <= 50 and self.f == True:
                
                self.prof3 = tkinter.Label(self.screen, text = "Love to be in charge? Your 58 year old match Karen certainly does!", bg = "pink", fg = "black", width = "50", height = "3")
                self.prof3a = tkinter.Label(self.screen, text = "She is in Kansas, and fiestier than the tornadoes her state is known for!", bg = "pink", fg = "black", width = "50", height = "3")
                self.prof3.place(x = 15, y = 480)
                self.prof3a.place(x = 15, y = 515)

            elif self.x >= 45 and self.x <= 50 and self.f == False:
                
                self.prof3 = tkinter.Label(self.screen, text = "Meet Shakira, the only 23 year old, hip-hop-loving, vegan you'll ever need!", bg = "pink", fg = "black", width = "50", height = "3")
                self.prof3a = tkinter.Label(self.screen, text = "Shakira... loves hip-hop and greens!", bg = "pink", fg = "black", width = "50", height = "3")
                self.prof3.place(x = 15, y = 480)
                self.prof3a.place(x = 15, y = 515)
                
            elif self.x > 50 and self.x <= 55 and self.f == False:
                
                self.prof4 = tkinter.Label(self.screen, text = "Rhonda is the girl for you! She is 29 years old, and climbs rocks!", bg = "pink", fg = "black", width = "50", height = "3")
                self.prof4a = tkinter.Label(self.screen, text = "Rhonda lives in Colorado, and will climb any mountain to reach your heart!", bg = "pink", fg = "black", width = "50", height = "3")
                self.prof4.place(x = 15, y = 480)
                self.prof4a.place(x = 15, y = 515)

            elif self.x > 50 and self.x <= 55 and self.f == True:
                
                self.prof4 = tkinter.Label(self.screen, text = "Meet Susan! Susan, is 45 years old, and is ecstatic to meet you!", bg = "pink", fg = "black", width = "50", height = "3")
                self.prof4a = tkinter.Label(self.screen, text = "For a good time, go to Susan's Library, where she is the librarian!", bg = "pink", fg = "black", width = "50", height = "3")
                self.prof4.place(x = 15, y = 480)
                self.prof4a.place(x = 15, y = 515)
                
            #for male 
            elif self.x >= 20 and self.x <= 25 and self.m == True:
                 
                self.prof1 = tkinter.Label(self.screen, text = "You were paired up with Mike! Mike is in the prime of life, a fresh 65!", bg = "pink", fg = "black", width = "50", height = "3")
                self.prof1a = tkinter.Label(self.screen, text = "Mike lives in the exciting state of Nevada, and loves collecting rocks!", bg = "pink", fg = "black", width = "50", height = "3")
                self.prof1.place(x = 15, y = 480)
                self.prof1a.place(x = 15, y = 515)

            elif self.x >= 20 and self.x <= 25 and self.m == False:
                
                self.prof2 = tkinter.Label(self.screen, text = "You got paired up with David! David is 32, and one spicy man!", bg = "pink", fg = "black", width = "50", height = "3")
                self.prof2a = tkinter.Label(self.screen, text = "David lives in a beautiful suburb in Mexico! He can't wait to meet you!", bg = "pink", fg = "black", width = "50", height = "3")
                self.prof2.place(x = 15, y = 480)
                self.prof2a.place(x = 15, y = 515)
                
            elif self.x > 25 and self.x <= 30 and self.m == False:
                
                self.prof2 = tkinter.Label(self.screen, text = "Jimson is 24, and is finally done with jail- he learned how to tattoo himself!", bg = "pink", fg = "black", width = "50", height = "3")
                self.prof2a = tkinter.Label(self.screen, text = "Jimson loves to give and receive tattoos, as well as pump iron!", bg = "pink", fg = "black", width = "50", height = "3")
                self.prof2.place(x = 15, y = 480)
                self.prof2a.place(x = 15, y = 515)

            elif self.x > 25 and self.x <= 30 and self.m == True:
                
                self.prof1 = tkinter.Label(self.screen, text = "You were paired up with Barry! Barry is 45, and in love with living!", bg = "pink", fg = "black", width = "50", height = "3")
                self.prof1a = tkinter.Label(self.screen, text = "Barry lives with his Mother in balmy Alabama! He likes to fish and Samba!", bg = "pink", fg = "black", width = "50", height = "3")
                self.prof1.place(x = 15, y = 480)
                self.prof1a.place(x = 15, y = 515)

        #reset

        def reset():
            self.male.config(state = "normal")
            self.female.config(state = "normal")
            
            
            self.female.place(x = 245, y = 90)
            self.male.place(x = 15, y = 90)

            self.left1.place_forget()
            self.left2.place_forget()
            self.left3.place_forget()
            self.left4.place_forget()
            self.left5.place_forget()
            
            self.right1.place_forget()
            self.right2.place_forget()
            self.right3.place_forget()
            self.right4.place_forget()
            self.right5.place_forget()
            
            self.des_text.place_forget()
            self.dat_text.place_forget()
            self.foo_text.place_forget()
            self.age_text.place_forget()
            self.inc_text.place_forget()
            
            self.res.place_forget()
            self.reset.place_forget()
            self.reset_text.place_forget()
            
            self.prof1.place_forget()
            self.prof1a.place_forget()
            self.prof2.place_forget()
            self.prof2a.place_forget()
            self.prof3.place_forget()
            self.prof3a.place_forget()
            self.prof4.place_forget()
            self.prof4a.place_forget()
            
        
        
        def main(): 

            self.m = True
            self.f = True

            
            #init labels

            self.prof1 = tkinter.Label(self.screen, text = "profile1", bg = "blue", fg = "black", width = "50", height = "3")
            self.prof1a = tkinter.Label(self.screen, text = "profile1", bg = "blue", fg = "black", width = "50", height = "3")
            self.prof2 = tkinter.Label(self.screen, text = "profile2", bg = "blue", fg = "black", width = "50", height = "3")
            self.prof2a = tkinter.Label(self.screen, text = "profile1", bg = "blue", fg = "black", width = "50", height = "3")
            self.prof3 = tkinter.Label(self.screen, text = "profile3", bg = "pink", fg = "black", width = "50", height = "3")
            self.prof3a = tkinter.Label(self.screen, text = "profile1", bg = "blue", fg = "black", width = "50", height = "3")
            self.prof4 = tkinter.Label(self.screen, text = "profile4", bg = "pink", fg = "black", width = "50", height = "3")
            self.prof4a = tkinter.Label(self.screen, text = "profile1", bg = "blue", fg = "black", width = "50", height = "3")
            
            self.screen.geometry("500x700")
            self.screen.title("Questionnaire")

            self.heading = tkinter.Label(self.screen, text = "Ready to find the future Mr. or Mrs. You?", bg = "yellow", fg = "black", width = "500", height = "3")
            self.heading.pack()

            self.gender_text = tkinter.Label(self.screen, text = "Please select the gender you wish to be matched up with: ")
            self.gender_text.place(x = 15, y = 70)

            self.male = tkinter.Button(self.screen, text = "Male", width = "25", height = "2", command = malesel, bg = "grey")
            self.male.place(x = 15, y = 90)
            
            self.female = tkinter.Button(self.screen, text = "Female", width = "25", height = "2", command = femalesel, bg = "grey")
            self.female.place(x = 245, y = 90)
            
            self.quitter = tkinter.Button(self.screen, text = "Quit", width = "25", height = "2", command = self.screen.destroy, bg = "grey")
            self.quitter.place(x = 245, y = 650)
            
            self.reset_text = tkinter.Label(self.screen, text = "Unsatisfied? Press below to try again!", fg = "black")
                
        main()

        tkinter.mainloop()

my_gui = MyGUI()

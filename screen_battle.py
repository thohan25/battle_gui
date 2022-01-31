import tkinter

class Screen_Battle (tkinter.Frame):
    def __init__ (self, master, player1, player2, callback_on_exit):
        super().__init__(master)

        # Save references to the two player objects
        self.player1 = player1
        self.player2 = player2

        # Store the maximum number of hit points which are needed on the screen display.
        self.player1_max_hp = player1.hit_points
        self.player2_max_hp = player2.hit_points

        # Save the method reference to which we return control after this page Exits.
        self.callback_on_exit = callback_on_exit

        self.create_widgets()
        self.grid()
        
    def create_widgets (self):
        '''
        This method creates all of the (initial) widgets for the battle page.
        '''
        self.attack_bttn = tkinter.Button(self, text = "Attack", command = self.attack_clicked, fg = "red", font = "sans", bg = "black")
        self.attack_bttn.grid(row = 0, column = 0)

        you_lbl = tkinter.Label(self, text = "You", font = "sans").grid(row = 2, column = 0)
        comp_lbl = tkinter.Label(self, text = "Computer", font = "sans").grid(row = 2, column = 1)
        
        img1 = tkinter.PhotoImage(file="images/" + self.player1.large_image);
        w= tkinter.Label (self,
                    image = img1, 
                     )
        w.photo = img1 
        w.grid (row = 3, column = 0)

        img2 = tkinter.PhotoImage(file="images/" + self.player2.large_image);
        w= tkinter.Label (self,
                    image = img2, 
                     )
        w.photo = img2
        w.grid (row = 3, column = 1)
        
        self.hp1 = tkinter.Label(self, text = str(self.player1.hit_points) + "/" + str(self.player1_max_hp), font = "sans")
        self.hp1.grid(row = 4, column = 0)
        self.hp2 = tkinter.Label(self, text = str(self.player2.hit_points) + "/" + str(self.player2_max_hp), font = "sans")
        self.hp2.grid(row = 4, column = 1)

        self.attack_lbl1 = tkinter.Label(self, text = "", font = "sans")
        self.attack_lbl2 = tkinter.Label(self, text = "", font = "sans")

    def attack_clicked(self):
        ''' This method is called when the user presses the "Attack" button.
            
            This method does the following:
            1) Calls the character.attack method for both the player and (if still alive) the computer.
            2) Updates the labels on the top right with the results of the attacks.
            3) Determines if there was a victor, and if so display that info 
            4) If there is a victor, remove the Attack button.  Create an Exit button to replace it.  

            To remove a widget, use the destroy() method. For example:
    
                self.button.destroy()   
        '''       
        result2 = ""
        result1 = self.player1.attack(self.player2)
        if self.player2.hit_points > 0:
            result2 = self.player2.attack(self.player1)
        else:
            attack_lbl3 = tkinter.Label(self, text = self.player1.name + " is victorious!", font = "sans").grid(row = 2, column = 1) 
            self.attack_bttn.destroy()
            self.exit_bttn = tkinter.Button(self, text = "Exit!", command = self.exit_clicked, fg = "red", font = "sans", bg = "black").grid(row = 5, column = 1, sticky = tkinter.E)
        
        if self.player1.hit_points < 0:
            attack_lbl3 = tkinter.Label(self, text = self.player2.name + " is victorious!", font = "sans").grid(row = 2, column = 1) 
            self.attack_bttn.destroy()
            self.exit_bttn = tkinter.Button(self, text = "Exit!", command = self.exit_clicked, fg = "red", font = "sans", bg = "black").grid(row = 5, column = 1, sticky = tkinter.E)
        
        self.attack_lbl1.destroy()
        self.attack_lbl2.destroy()
        self.attack_lbl1 = tkinter.Label(self, text = result1, font = "sans")
        self.attack_lbl1.grid(row = 0, column = 1)
        self.attack_lbl2 = tkinter.Label(self, text = result2, font = "sans")
        self.attack_lbl2.grid(row = 1, column = 1) 

        self.hp1.destroy()
        self.hp2.destroy()
        self.hp1 = tkinter.Label(self, text = str(self.player1.hit_points) + "/" + str(self.player1_max_hp), font = "sans")
        self.hp1.grid(row = 4, column = 0)
        self.hp2 = tkinter.Label(self, text = str(self.player2.hit_points) + "/" + str(self.player2_max_hp), font = "sans")
        self.hp2.grid(row = 4, column = 1)
                                            
    def exit_clicked(self):
        ''' This method is called when the Exit button is clicked. 
            It passes control back to the callback method. '''        
        self.callback_on_exit()
  
            
            
            
            
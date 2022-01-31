import tkinter

class Screen_PrepareToBattle (tkinter.Frame):
    def __init__ (self, master, player1, player2, callback_on_commence_battle):
        super().__init__(master)

        # Save player character object references
        self.player1 = player1
        self.player2 = player2
        
        # Save the method reference to which we return control after the player hits "Next"
        self.callback_on_commence_battle = callback_on_commence_battle
        
        self.create_widgets()
        self.grid()
        
    
    def create_widgets (self):
        '''
        This method creates all of the widgets the prepare to battle page.
        '''
        you_lbl = tkinter.Label(self, text = "You", font = "sans").grid(row = 0, column = 0)
        comp_lbl = tkinter.Label(self, text = "Computer", font = "sans").grid(row = 0, column = 1)
        
        img1 = tkinter.PhotoImage(file="images/" + self.player1.large_image);
        w= tkinter.Label (self,
                    image = img1, 
                     )
        w.photo = img1 
        w.grid (row = 1, column = 0)

        img2 = tkinter.PhotoImage(file="images/" + self.player2.large_image);
        w= tkinter.Label (self,
                    image = img2, 
                     )
        w.photo = img2
        w.grid (row = 1, column = 1)

        hp1 = tkinter.Label(self, text = str(self.player1.hit_points) + " HP", font = "sans").grid(row = 2, column = 0)
        dxt1 = tkinter.Label(self, text = str(self.player1.dexterity) + " Dexterity", font = "sans").grid(row = 3, column = 0)
        str1 = tkinter.Label(self, text = str(self.player1.strength) + " Strength", font = "sans").grid(row = 4, column = 0)
        
        hp2 = tkinter.Label(self, text = str(self.player2.hit_points) + " HP", font = "sans").grid(row = 2, column = 1)
        dxt2 = tkinter.Label(self, text = str(self.player2.dexterity) + " Dexterity", font = "sans").grid(row = 3, column = 1)
        str2 = tkinter.Label(self, text = str(self.player2.strength) + " Strength", font = "sans").grid(row = 4, column = 1)

        commence_bttn = tkinter.Button(self, text = "Commence Battle!", command = self.commence_battle_clicked, fg = "red", font = "sans", bg = "black").grid(row = 5, column = 1, sticky = tkinter.E)

    def commence_battle_clicked(self):
        ''' This method is called when the Battle button is clicked. 
            It passes control back to the callback method. '''         
        self.callback_on_commence_battle()
            
        
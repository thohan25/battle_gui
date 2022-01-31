import tkinter

class Screen_CharacterSelection (tkinter.Frame):
    def __init__ (self, master, roster, callback_on_selected):
        super().__init__(master)
       # Save the CharacterRoster  
        self.roster = roster
        # Save the method reference to which we return control after the player hits "Character Selected"
        self.callback_on_selected = callback_on_selected

        self.grid()
        self.create_widgets()
        
    def create_widgets (self):
        '''
        This method creates all of the widgets character selector page.
        The information about each character should be derived from self.roster, 
        which is a CharacterRoster loaded from battle_characters.txt. 
        The layout should NOT be hard-coded: if you re-order, alter, or remove entries 
        in battle_characters.txt, the layout should automatically reflect those changes. 
        
        ########
        
        The radio buttons on this page should all use the variable "self.character_index_index".  
        The values of the radio buttons must be a number equally the position of the character in the list. 
        For example, if the characters listed are Troll, Elf, Human, and Dwarf.  self.character_index would equal 0 
        for the Troll, 1 for the Elf, and so forth.  
        
        The variable self.character_index has been instantiated for your convenience below.
        
        ########

        Here is some sample code for including an image on a page:   (char is a Character object)
            
            imageSmall = tkinter.PhotoImage(file="images/" + char.small_image);
            w= tkinter.Label (self,
                        image = imageSmall, 
                         )
            w.photo = imageSmall # saving the image as a property is required for "saving" the image. It's odd.

            w.grid (ADD PARAMETERS HERE)
        '''
        self.character_index = tkinter.StringVar()
        self.character_index.set(None)
        
        self.roster.character_list
        chars = self.roster.get_number_of_characters()
        
        hp_lbl = tkinter.Label(self, text = "Hit Points").grid(row = 0, column = 2)
        dxt_lbl = tkinter.Label(self, text = "Dexterity").grid(row = 0, column = 3)
        str_lbl = tkinter.Label(self, text = "Strength").grid(row = 0, column = 4)

        for char in range(chars):
            imageSmall = tkinter.PhotoImage(file="images/" + self.roster.character_list[char].small_image);
            w= tkinter.Label (self,
                        image = imageSmall, 
                         )
            w.photo = imageSmall # saving the image as a property is required for "saving" the image. It's odd.
            w.grid (row = char+1, column = 1)

            select_bttn = tkinter.Radiobutton(self, text = self.roster.character_list[char].name, variable = self.character_index, value = char)
            select_bttn.grid(row = char+1, column = 0)

            char_hp = tkinter.Label(self, text = self.roster.character_list[char].hit_points).grid(row = char+1, column = 2)
            char_dxt = tkinter.Label(self, text = self.roster.character_list[char].dexterity).grid(row = char+1, column = 3)
            char_str = tkinter.Label(self, text = self.roster.character_list[char].strength).grid(row = char+1, column = 4)

        char_selected = tkinter.Button(self, text = "Character Selected!", command = self.selected_clicked, fg = "red", font = "sans", bg = "black").grid(row = 5, column = 3, columnspan = 2)
       
 
    def selected_clicked(self):
        ''' This method is to be called when the "Character Selected!" button is clicked. 
            Notice that it passes self.character_index back to the callback method. '''         
        self.callback_on_selected(self.character_index.get())
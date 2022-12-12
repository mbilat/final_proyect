
# Proyect "Y"

"Y" is a project that I started for my studies. It is a game made with pygame but it also uses .json files, and sql3. Both its gameplay and its artistic section are still under development. Feel free to give this project a run, and message me if you have any feedback!



#### *Gameplay:*

* [YouTube](https://www.youtube.com/watch?v=2UBIxTz1Xyk)

# **About the proyect**

"Y" is a 2D game slightly inspired by Donkey Kong mobility with its stairs. The visual section belongs to Pixel Adventure momentarily until I can change them for images of my authorship.
From the menu to the gameplay is handled only with the keyboard. The game has random spawns (both enemies and bonuses) so that the difficulty is managed a bit by luck. My idea is to continue with this idea of the game influenced by 50% luck. Enemies are already created as objects so it's easy to program new enemies to inherit from those already in the game.
The idea of the gameplay is to collect the flags to activate the portal with which you win when you reach it. For this you will have to eliminate the enemies, but it is possible but difficult to win in peaceful mode.
Winning in the shortest possible time is what will take you to the ranking of the game.

# **Setup**

To play it is necessary to have Visual Studio Code (last version), anaconda3. Links below.

* [VisualStudioCode](https://code.visualstudio.com/)
* [anaconda3](https://www.anaconda.com/products/distribution)

In Visual Studio Code it is necessary to install python and the pygame library. In the terminal type ` pip install pygame` .

Clone with gitbash or download the files from my repository.
It is necessary to change the path of some files to make it work correctly.

In the file enemigo.py lines 8, 9 ,133 & 134 you must change the string *"C:/Users/bilix/OneDrive/Escritorio/"* for the path where you have downloaded the project.


### **Example**

From this...

    self.walk_l = Auxiliar.getSurfaceFromSpriteSheet("C:/Users/bilix/OneDrive/Escritorio/final_proyect/y_proyecto_final/resources/enemies/Run (36x30).png",12,1)
To this:

    self.walk_l = Auxiliar.getSurfaceFromSpriteSheet("D:/Users/tester/OneDrive/desktop/final_proyect/y_proyecto_final/resources/enemies/Run (36x30).png",12,1)

This must be repeated in the following files and lines.
Line 29 of gui.py

Line 6 of ladder.py

Line 6, 29, 30 & 57 of objetos.py

Line 6 of plataforma.py

Line 8, 9, 10 & 11 of player.py

Line 5 of proyectil.py


## **Controls**
* In Menu:
	* ⇅ to move in the menu.
	* ⇄ to decrease and increase the volume in settings.
	* "INTRO" to mute sounds or music in settings.

* In Game:
	* ⇄ to move left & right.
	* ⇅ to climb ladders.
	* "X" to shoot.

#### Version 1.0.0

# **About me**

Hello, my name is Matias Bilat, I am a young programmer from Argentina and I started this project for my studies, although I want to continue developing this game to get the best out of it and myself.

* [LinkedIn](https://www.linkedin.com/in/mbilat/)
* [GitHub](https://github.com/mbilat)

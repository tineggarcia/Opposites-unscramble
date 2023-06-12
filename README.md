# Unscrambling the Opposites 

![deployed game screenshot](assets/deployed_screen.png)

[Deployed Game Link](https://unscrambling-opposites.herokuapp.com/)

This is a simple game that tests your vocabulary, but to add a bit of challenge, 
you have to unscramble the words to guess, whereas these words are the antonyms 
of the displayed meaning. It might be a bit confusing at first, but trust me, 
you'll get the hang of it real soon. Users will have the option to set how many 
games/words to guess you would like to play, choose between 10-20 games. The game 
will show you for each question, the jumbled words and the meaning of its possible
antonyms. Type in your guess, you have to unscramble it of course, the game will 
validate your answer straight away. Correct answers will be added to your points, 
which will be displayed after the game has ended. Whereas wrong answers of course 
do not earn you a point.
&nbsp;
## Table of Contents
---
- [UX](#ux)
    - [Users goals](#users-goals)
    - [Website owners goals](#website-owners-goals)
    - [Flow Chart](#flow-chart)
- [Features](#features)
    - [Game](#game)
    - [Future feature to implement](#future-feature-to-implement)
- [Technologies used](#tecnologies-used)
- [Libraries used](#libraries-used)
- [Testing and Validation](#testing-and-validation)
    - [PEP8](#pep8)
    - [Manual testing](#manual-testing)
    - [User stories testing](#user-stories-testing)
    - [Bugs](#bugs)
    - [Unfixed Bugs](#unfixed-bugs)
- [Deployment](#deployment)
    - [How to deploy](#how-to-deploy)
- [Credits](#credits)


&nbsp;

## UX
---
User Experience
The purpose of the game is to be really more educational than entertainment. 
To test how good the user's vocabulary is, particularly how well you know your 
antonyms. This is a simple command-line game written in Python.


### Users goals

- Users would have the ease of navigation all throughout the game, despite the game being a command-line game.
- Users would have the ability to always have an option to every question asked or to any action/steps that took place.
- Users would have a clear and readable and very easy to understand interface.
- Users would enjoy the game and would be encouraged to play more.
- Users will be notified of their action, say upon entering the games they want to play, validation and error messages would be available for users to help them enter data correctly.
- Users would be challenged by this game as words in the word bank are not typical words.
- Meanings provided are searched through the PyDictionary tool/package that offers a huge selection of words and their meanings.
- Users would definitely learn new words or be refreshed on the words they already know.  
- Users' knowledge of antonyms would definitely be tested on this game.
- Users will be notified whether their guesses are correct or not.
- Users will be given a tally of their points and will have the option to continue to play another game or just end it.

### Website owners goals
- Provide an educational vocabulary game for the users who are interested to enrich or test their vocabulary. For this game, particularly the antonyms.
- Be able to provide a clear and easy command-line navigation/interface to the user.
- Make necessary validations on user's input and display error messages if needed.
- Be able to provide a final score once the game is finished.
- Provide an option to the user how many times they wish to play or words they would like to guess and they should be able to play another new game should they wish.

[Back to Table of contents](#table-of-contents)

&nbsp;
### Flow Chart
As part of the development of the game, a flowchart was developed to establish 
the guidelines and structure of the application.

![Flow Chart](docs/CI-PP3-Flowchart.png)

&nbsp;
[Back to Table of contents](#table-of-contents)

&nbsp;
## Features

Introduction Welcome section
Rules of the game
Questions and its contents
notification of the result of answers
Display of summary of points
Option to play again or terminate


## Future Features

### Game
Here's what the program does and how the game plays:

1. Welcome Screen which asks for the name of the user.
   ![Welcome Screen](assets/welcome_screen.png)

2. Once the user has input their name, the program prompts the user if the would like to start the game.
   ![Initiate game](assets/initiate_game.png)

3. If the user decides to quit the game, the program automatically restarts, ready to be played agan.
   ![Restart screen](assets/restart_screen.png)

4. The menu of the game then asks the user what they would like to do next giving them a choice to play immediately, check the rules of the game, or quitting the game.
   ![Menu screen](assets/menu_screen.png)

5. If the user selects to review the rules of the game, a description appears and then the user gets asked to select another options from playing or quitting the game.
   ![Rules screen](assets/rules_screen.png)

6. If the user chooses to quit the game, a thank you message appears on the screen and the program restarts again, ready to be used.
   ![Quit screen](assets/restart_screen.png)

7. If the user chooses to play, the firts turn instruction and reference board will populate the screen. Then the user will get propted for a first choice.
   ![First turn screen](assets/first_turn_screen.png)

8. After the user inputs their choice, the choice gets shown into the board and the cumputer makes its move which gets shown on the board as well. Then the program asks for the next move from the user.
   ![Second turn screen](assets/second_turn_screen.png)

9. The promt for a choice will continue until the game is won with three symbols in a row or both players have run out of moves in a tie. A feedback message will display in both cases and then the game will restart again ready to be used.
   ![user wins](assets/user_wins_screen.png)

&nbsp;

### Future feature to implement
- To use a better GUI, i.e. Textual Interface that is still command-line.
- To be able to add and store user profile. 
- To be able to provide different game mode. 
- To use spreadsheet or anything the same to store the vocabulary. 

&nbsp;
[Back to Table of contents](#table-of-contents)

&nbsp;

## Technologies Used

Python was used to code the application/gameGitHub - Version control, repositoryGitPod - IDE used to code the program and for some of the manual testing and push to Github.Heroku - to deploy the application/gameLucidchart was used to design the flow chart.Python was used to code the game.Gitpod was used to create this app and then push everything to github.Visual Studio Code was used to work on the app locally.PyCharm was also used to work on the app locally.Github is used to store the repository.Heroku is used to deploy the app.I also used the following Python librariesRandomsysosargparsepydictionaryRichcolorama

Python was used to code the application/gameGitHub - Version control, repositoryGitPod - IDE used to code the program and for some of the manual testing and push to Github.Heroku - to deploy the application/gameLucidchart was used to design the flow chart.Python was used to code the game.Gitpod was used to create this app and then push everything to github.Visual Studio Code was used to work on the app locally.PyCharm was also used to work on the app locally.Github is used to store the repository.Heroku is used to deploy the app.I also used the following Python librariesRandomsysosargparsepydictionaryRichcolorama
- JavaScript - generated from the python essential template build by Code Institute.
- GitHub - Version control.
- GitPod - IDE used to code the program and for some of the manual testing.
- Heroku - Program deployment for the users to access it without deploy it themselves.

### Libraries used
- Math - for calculation and managment of numbers and data types.
- Random - to randomize the choices of the computer player.
- Time - to slow down the respode of the program and allow the user to view the response of the computer.
- Os - to create the clear_screen() function, which facilitates the UX eliminating previous code on the terminal window making it clutter free.

&nbsp;

[Back to Table of contents](#table-of-contents)

&nbsp;

## Testing and Validation
---

### PEP8
The code was checked with PEP8 validator and passed with no error found.

&nbsp;

### Manual testing
All features have been tested manually with a Mac Mini and a Chromebook with multiple browsers (Chrome, Safari, Firefox).

&nbsp;

### User stories testing
For the program owner:
- The game offers entertainment to the users and the chance to play it multiple times.
- The game contains informations about the game of Tic Tac Toe that the user can easily access.
- The game give options to the user to quit the game at the menu if they would like.

For new users and returning visitors:
- The user can improve their skill at the game excercising with this program which puts them against the computer.
- The user can navigate through the game with very easy commands
- Always available reference of the possible choices when making a move, makes it easy to find the right commands.

&nbsp;

### Bugs
- Game automatically lets user win at first move. Fixed missing colon and indentation in "winner" function.
- Corrected prompt to the user for the next move to suggest numbers from 0-8, since is 0 index based instead of 1-9.
- Added extra spaces in-between command line prompt to help visual clarity for the user.

&nbsp;

### Unfixed Bugs
- None that I'm aware of at the moment.

&nbsp;
## Deployment
There is only this main branch of the project version available in GitHub.
This version is also deployed live on Heroku - [Link]

### How to deploy
To deploy this page to Heroku from its [GitHub repository](https://github.com/alessandracosta8/Tic-Tac-Toe) the following steps were taken:

- Log into or register a new account at [Heroku](https://www.heroku.com/).
- Click on the button **New** in the top right corner of the dashboard.
- From the drop-down menu then select **Create new app**.
- Enter your app name in the first field, the names must be unique so check that then name you have chosen is available on Heroku, then select your region.
- Click on **Create App**.
- Once the app is created you will see the Overview panel of the application. Now move to the **Settings** tab.
- Once you are in the **Settings** tab scroll down till you find **Config Vars**.
- Press the button **Reveal Config Vars** and for 'KEY' field, type in 'PORT' and for the value field type in '8000'.
  Then press the **Add** button.
- Scroll down to **Buildpacks**. Click the button **Add buildpack** and select 'python'. Do the same step and add 'node.js'.
  **PYTHON MUST BE ON TOP OF THE BUILDPACKS. IF IN YOUR CASE NODE.JS IS FIRST, CLICK AND DRAG PYTHON TO TOP AND SAVE.**
- Return back to the **Deploy** tab. From the deployment method, select 'Github' as the deployment.
- You will be asked to connect your github account. Confirm and proceed.
- Search for your repository name and connect.
- Once that is done and successfully connected, select how you want to push updates from the following options.

  _Clicking **Enable Automatic Deploys**. This will update once you push updates to your Github._

  _Selecting the correct branch for deployment from drop-down menu and pressing **Deploy Branch** button. This will have to be done everytime manually._

&nbsp;

[Back to Table of contents](#table-of-contents)

&nbsp;

## Credits
----
- 
- [Python Classmethods and Staticmethods](https://www.youtube.com/watch?v=rq8cL2XMM5M)
- [Python if __name__ == __main__ Explained with Code Examples](https://www.freecodecamp.org/news/if-name-main-python-example/#:~:text=We%20can%20use%20an%20if,name%20if%20it%20is%20imported.)
- [Python Tutorial: if __name__ == '__main__'](https://www.youtube.com/watch?v=sugvnHA7ElY)
- [12 Beginner Python Projects](https://www.youtube.com/watch?v=8ext9G7xspg&t=2189s)
- [Tic Tac Toe definition - Collins Dictionary](https://www.collinsdictionary.com/dictionary/english/tic-tac-toe#:~:text=Tic%2Dtac%2Dtoe%20is%20a,same%20symbols%20in%20a%20row.)
- [W3 Schools](https://www.w3schools.com/)
- [Github](https://github.com/marcin-kli/MP1/blob/Milestone-Projects/README.md) - README file example
- [GitHub](https://github.com/MustafaSahinci/project-portofolio-3) - clear screen function example
- Mentor: Adegbenga Adeye - For his support and patience!


&nbsp;

[Back to Table of contents](#table-of-contents)

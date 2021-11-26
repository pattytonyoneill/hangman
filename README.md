# Hangman
- Hangman is a Python Terminal game, which runs on a mock terminal in Heroku.
- Users guess letters from a word until they run out of lives or guess the word correctly.

![image]()

## How to Play
1. Guess a letter
2. If you get it right the letter it is put in the space. If it is wrong Hangman form starts to come up.
3. Keep guessing until either you guess the word and win or end up with a hangman and no lives left.

## Existing Features
- _Random word generation_
- _Accepts user input_
- _Keeps track of right and wrong guesses_
- _Input validation and score checking_

## User Stories:
- _First time Visitor Goals_
  - As a first time user of this site, I would like to be able to easily decifer the main purpose of the game
  - As a first time user, I would like to be able to easily navigate the game
  - As a first time user, I would like to see how many lives that I have left

## Languages Used:

- _Python_

## Frameworks, Libraries & Programs Used:

- [Git](https://git-scm.com): used to utilize the Gitpod terminal to commit to Git and Push to GitHub
- [GitHub](https://github.com/): used to store project code after being pushed from Git
- [Lucid Charts](https://www.lucidchart.com/pages/): used to draw a chart of the hangman game process
- [Am I Responsive?](http://ami.responsivedesign.is/) Used on Readme to show how the application looks on different devices.

## Bugs
- Getting while loop to work correctly. Firstly I took a couple of days away from the code. Next I rewrote this several times until I got it right.

- When I deployed my code it did not deploy correctly.  I had to redo pip3 line due to a typo on that line and it was right immediately after that.

## Remaining Bugs
- No bugs are remaining

## Features:

- _Responsive on all device sizes_

  - _Desktop_

    - ![image]()

  - _Tablet_

    - ![image]()
  - _Cell Phone_

    - ![image]()

- _Interactive Elements_

  -  The buttons on this page make it possible to easily navigate to the game that the user wishes to play. 

    - ![image]()

  - The user clicks on the correct answer and continues on to the next question
    - ![image]()

  
## Future Additions to page

- Mutiplayer function
- Ability to choose the length of the word


## Testing

- I have manually tested this project by doing the following:
    - Given invalid inputs such as a number and a repeat of previous letter used.
    - Tested in my local terminal as well as on Heroku.

## Validator Testing

## Deployment

- The site was deployed to Heroku. I used the steps listed below to deploy. 
  -  Fork or clone this repository
  -  Create a new Heroku app. 
  -  Under settings set buildback to python.
  -  Under settings set buildback to nodeJS.
  -  Link the app to the repository.
  -  Click on Deploy

The live link can be found here - 

### Local Deployment

In order to make a local copy of this repository, you can clone it by typing the following into your IDE Terminal:

- `git clone https://github.com/pattytonyoneill/hangman.git`

Alternatively, if using Gitpod, you can click below to create your own workspace using this repository.

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/pattytonyoneill/hangman)

## Credits

### Code
- _Readme used sample readme from code institute as a model. [Github](https://github.com/Code-Institute-Solutions/readme-template/blob/master/README.md)_

### Content
- _All content written by the developer._

### Acknowlegements
- _My Mentor for his help and feedback._
- _Tutor support at Code Institute_
- _Family for help with help and feedback on website as a use_
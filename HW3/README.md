Problem 1:

This problem involves parsing through the text file in standard input. Each line is converted to a variable called word. Then, the line is passed through a function to check if it's a palindrome. Checking for palindromality is quite simple. If the variable word is the same as word indexed backwards, then it is a palindrome. If the word is a palindrome, then it will print True, otherwise False. Then it will move onto the next word. A count is collected while the function goes through each line, adding 1 to the count if the word is a palindrome. At the end of the algorithm, the total count will be printed, which represents the total number of palindromes in the text.

Problem 2:

Problem 2 involves finding all possible substrings in a given string. 

Problem 3:


Problem 4:

This algorithm takes as standard input the buster and ghostbuster coordinate pairs. First, it will parse each line and split it into a list of characters. It ignores the B and G characters and focuses only on the X and Y coordinates of each buster/ghost pair. The algorithm checks to make sure that the value in the first row matches the number of pairs, or it will raise an error message. 

An empty list called lines will be created. Line by line the algorithm will parse through the text and assign the coordinates to each buster and ghost pair. Then it will run the coordinates through a function that finds the slope and y-intercept for each pair. It will add the slope and intercept pairs into the lines list. Then the list of lines will be passed through a function that compares the slope of each line. If any slope is different, then we know that the lines will intersect at some point. If all slopes are the same, then the lines are parallel and will not cross, except in the case that the lines are on top of each other. 

If the any of the slopes do not match the first line's slope, then it automatically passed through False. If all slopes are the same, then it will now compare the y-intercepts. The y-intercepts should all be unique , otherwise as least two lines are right on top of each other. A list will be created with all of the y-intercepts from the ghost/buster pairs. Then a set will be created of the y-intercepts. This will remove any duplicates in the list of y-intercepts. If the length of the set and the length of the list are the same then all y-intercepts are unique and no lines intersect. The function returns True. If the length of the set and the list differ, that means at least one of the y-intercepts are not unique the lines overlap. The functions returns False.

If the function returns True then it will print the message that all ghosts were eliminated. If the function returns False, then it will print the message that all ghosts were not eliminated.



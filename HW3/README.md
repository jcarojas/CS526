Problem 1:

This problem involves parsing through the text file in standard input. Each line is converted to a variable called word. Then, the line is passed through a function to check if it's a palindrome. Checking for palindromality is quite simple. If the variable word is the same as word indexed backwards, then it is a palindrome. If the word is a palindrome, then it will print True, otherwise False. Then it will move onto the next word. A count is collected while the function goes through each line, adding 1 to the count if the word is a palindrome. At the end of the algorithm, the total count will be printed, which represents the total number of palindromes in the text.

Problem 2:

Problem 2 involves finding all possible substrings in a given string. The algorithm starts by assigned the contents of the text to a variable called text. Normally, assigning the entire contents of a text file to a variable uses up precious memory. However, since we are only expecting one line as input, we can ignore the memory usage. 

We also create a set called found that holds all of the substrings. We use a set to collect all of the substrings instead of a list because searching for existence of an element in a set is much quicker than searching for existence of an element in a list. With a list, we would need to search through each element one by one (linear search), whereas a set is washable and can very quickly determine if an element exists inside of a set.

The variable text is passed through a function to collect substrings along with the set of all substrings. If the variable text is empty string or if the string is found in the set, then it will return and exit the program. I added this step to optimize the time it takes to complete the program. Without adding this if statement, then the substring will go through all possible substring cases, even the ones that already were found.

If a unique substring is found then the function will call itself and pass the text without the first character, and then call itself without the last character. This recursion allows it to find all possible substrings and avoid trying to add duplicates into the set. Even though you can add an element that exists already inside of a set, we utilize the set instead of a list to quickly search if the element inside exists already.

The last step of the algorithm is to iterate through each element in the sorted version of the set. The sorted version will be in alphabetical order, which is required for this program. For each iterations, it prints the substring, then finally, it will print the total number of substrings found in the input string. 

Problem 3:


Problem 4:

This algorithm takes as standard input the buster and ghostbuster coordinate pairs. First, it will parse each line and split it into a list of characters. It ignores the B and G characters and focuses only on the X and Y coordinates of each buster/ghost pair. The algorithm checks to make sure that the value in the first row matches the number of pairs, or it will raise an error message. 

An empty list called lines will be created. Line by line the algorithm will parse through the text and assign the coordinates to each buster and ghost pair. Then it will run the coordinates through a function that finds the slope and y-intercept for each pair. It will add the slope and intercept pairs into the lines list. Then the list of lines will be passed through a function that compares the slope of each line. If any slope is different, then we know that the lines will intersect at some point. If all slopes are the same, then the lines are parallel and will not cross, except in the case that the lines are on top of each other. 

If the any of the slopes do not match the first line's slope, then it automatically passed through False. If all slopes are the same, then it will now compare the y-intercepts. The y-intercepts should all be unique , otherwise as least two lines are right on top of each other. A list will be created with all of the y-intercepts from the ghost/buster pairs. Then a set will be created of the y-intercepts. This will remove any duplicates in the list of y-intercepts. If the length of the set and the length of the list are the same then all y-intercepts are unique and no lines intersect. The function returns True. If the length of the set and the list differ, that means at least one of the y-intercepts are not unique the lines overlap. The functions returns False.

If the function returns True then it will print the message that all ghosts were eliminated. If the function returns False, then it will print the message that all ghosts were not eliminated.



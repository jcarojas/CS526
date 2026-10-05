Problem 1: 
The primary advantage of utilizing a tail pointer in a linked list is that the time it takes to append a node at the end of a list is a constant O(1). You do not need to walk through the whole list to get to the last value, which would be O(n) for a linked list of n length. This tail pointer also provides easy access to the end of the list, which can be utilized for many different directives and helper functions in our program and driver.

Problem 2:
The singly linked list is a chain of nodes, where each node contains a reference to the value and the next node. The list contains a head, tail, and a length/count reference. The list will be initialized to have no head, tail, or length until elements are added to the list.

Operations:
Append - This operation is optimized at O(1) since the tail pointer lets us add directly after the last node. This is better than jumping through each node with a O(n). The count increases by 1.
Prepend - Also optimized at O(1) since we simply point the new node at head, then move the original head. The count increases by 1.
Insert - This method utilizes Append if the index indicated would essentially be the same as adding to the end of the list, and Prepend when we want to insert the value at the beginning of the list (index = 0). For the case ins which we add in the middle of the list, we must point to the node before the target inde. We will make that node point to our new node. Then we will make the new node point to the remainder of the list to complete the list. the count increases by 1. This operation uses a helper function that I will discuss shortly.
Get - this operation walks through the list until it finds the given index, where O(i). This operation uses a helper function that I will discuss shortly.
Find and Delete - These operations are a linear scan O(n) through the list. Find traverses through the list and keeps track of each iteration until it finds the target value, then returns that index. Delete also traverses through the list node by node until it finds the target value. Delete utilizes a helper function that I will discuss shortly.  
Delete_at - This operation walks through the list a total of I times. It identifies the node before the target index then uses an unlinking helper function to remove the node and connect the two adjacent pieces (similar to delete). I will discuss the helper function shortly.
Len - This operation simply returns the count of the list, so O(1). 
Print_list - This operation traverses through each node so O(n). It adds the values of the singly linked list into a list [] as strings, and then prints them one by one, joined by "->" in between each node.

There were a handful of helper operations that I created to perform certain actions that I noticed multiple functions needed: _check_index, _node_at, and _unlink. I created these helper functions for simplicity and practical reasons. Utilizing s helper function prevents me from repeating the same code over and over. Additionally, utilizing a helper function allows me to de-bug and alter my code quickly. The helper function allows for flexibility if I wanted to alter the way a certain function behaves. Instead of changing the same thing multiple times if I need to make an edit or fix a bug, I simply need to fix/edit the helper function that all functions call to.

_check_index(index) - very simply, this helper function raises an IndexError if the index given is out of range. The insert, get, update, and delete_at functions utilize this helper function to confirm that the index given is a valid index to use for the directive.
_node_at(index) - very simply, this helper function returns the node at a desired index. it traverses through the list i times and the last node it arrives at is returned (at position = index). The get, update, and delete_at functions utilize this helper function to optimize.
_unlink(prev, current) - this helper function takes as inputs the two nodes in which you want to unlink. the prev node will remain in the list but the current node will be removed. The prev node will now point to the node that originally followed current. The delete and delete_at functions use this helper function.

I decided to store length as a variable that we can call for the _len_ function. The alternative is counting through the list entirely each time you want to know the total number of nodes in the list. In exchange for a little bit of memory, I save a lot of time to call the _len_ function.

For the driver, we use "for line in sys.stdin" to read the text one line at a time so that memory does not grow. If we read the whole text first, we would use more memory with no extra benefit.

For text validation, the driver first checks for blank lines or comments. it skips these lines. Once it finds usable text, it confirms whether the directive is valid. Next, it confirms that the correct number of arguments is provided following the directive. Each directive has a specified number of arguments that it should be paired with. Next, the driver confirms that the argument provided is a whole number. Indices must be whole numbers, and we will assume that values can only be whole numbers for now. Finally, the driver will run the directive/operation on the list. 

I created a dictionary that stores the directives as keys and the expected number of arguments as the values. The dictionary helps to confirm that the given directive can be followed appropriately and has the correct number of expected arguments. Additionally, the dictionary is the source of known directives to search through for validation.

WHOLE_NUMBER is a pattern matcher that checks and confirms whole numbers are being input as arguments for the indices or values.

I created a DirectiveError class so that exceptions would interrupt the code altogether, print a warning then continue to the next line. This also allows for practical usage while I am coding. If I encounter an issue with a directive that is unknown, it will be printed to me so that I can address. If I used a built-in like ValueError, it crashes loudly and will not be hidden as a warning. A blanket Exception would simply swallow it.

I created functions called parse_index(token) and parse_value(token). Parse_index simply confirms that the argument passed through is a whole number or it raises an error. Additionally it returns the confirmed whole number as an integer. This function is called in the executive of any directives that utilize an index as an argument. Parse_value also confirms that the arguments is a whole number and then returns as an integer. If the argument is not a whole number, it remains as a string.

I also created a warn function for troubleshooting purposes. This function prints the line number of any errors and the corresponding message. This function is utilized anytime there is an IndexError, or DirectiveError.



Problem 3:

(a)The base case of my function will be n = 0. When n = 0, then we return 1. We say that it is one step because when you are already at the top, there is only one way to finish: don't move. I also added a guard for cases in which n is negative. When n is negative, it returns 0. this is an important step in the function because otherwise it wouldn't know how to handle ways(1) through ways(2). ways(1) = ways(0) + ways(-1) + ways(-2) = 1 + 0 + 0 = 1.

(b) If we climb only 1 or 2 steps a time, then the ways(n) function would produce the fibonacci sequence.

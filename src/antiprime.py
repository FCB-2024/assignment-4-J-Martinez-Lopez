## ADD WHATEVER ARGUMENTS ARE NECESSARY TO THE MAIN FUNCTION
## IN THE SAME ORDER AS THE ARGUMENTS ARE TAKEN FROM THE
## COMMAND LINE SPECIFIED BELOW

import sys 

def main(x) :
	## YOU CODE SHOULD START HERE AST THE SAME
	## IDENTATION AS THIS COMMENT

    y = int(sys.argv[1]) - 1
    i = 1
    j = 1
    div_x = 0
    div_y = 0

    while (i <= x) :
        if (x % i == 0) :
            div_x = div_x + 1
        i = i + 1
    
    while (y >= 1) :
        j = 1
        while (j <= y) :
            if (y % j == 0) :
                div_y = div_y + 1
            j = j + 1

	## THE LAST LINES OF YOUR CODE SHOULD EITHER
	## RETURN THE VALUE "anti-prime" or "not anti-prime"
	## REPLACE THE FOLLOWING LINE BY WHATEVER LINES
	## OF CODE ALLOW THIS FUNCTION TO RETURN THE VALUE
	## "anti-prime" or "not anti-prime"

        if (div_y >= div_x) :
            y = 0
            res = "not anti-prime"
        
        else :
            y = y - 1
            div_y = 0
        
    if (div_x > div_y) :
        res = "antiprime"
    return(res)

## DO NOT REMOVE THIS LINE BELOW
if __name__ == "__main__" :

	## MODIFY THE LINE BELOW AND ADD BEFORE WHATEVER LINES ARE NECESSARY
	## TO RUN THIS PROGRAM AS, FOR INSTANCE:
	## $ python antiprime.py 6
	## WHERE THE FIRST ARGUMENT IS A POSITIVE INTEGER NUMBER FOR WHICH
	## YOU WANT TO FIGURE OUT WHETHER IS ANTI-PRIME OR NOT
    if (len(sys.argv) == 2) :
        x = int(sys.argv[1])
    else :
        print (f"error: antiprime.py <x>")
    
print(main(x))




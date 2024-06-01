To get the flag, we need to reverse the actions of the provided Python script. I added some comments
to the script labeling variables with their actual values and describing the functionality of sections
of the program. From there, it was a matter of undoing the actions of the script in reverse order.
The array "phoneSteak," provided at the top of the Python file, is where we start. First, we reverse
the order of the second half of the array. Then, we perform three swaps (see comments for which specific
indices are swapped). Finally, we perform a bitwise XOR on every element of the array and then add 27 to every
element of the array. The array is now a list of the ASCII codes of the characters of the flag. By converting these
numbers to their ASCII characters, we are able to get the flag.

flag: SIVBGR{pyth0n_r3v3rs1ng_pr0}

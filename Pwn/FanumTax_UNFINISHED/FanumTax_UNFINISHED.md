We are given an executable called fanum_strings that I uploaded to the decompiler explorer at
dogbolt.org. The challenge description and the name of this executable hint towards something
about strings, and sure enough, there is a format string vulnerability present in the executable.
The program prompts the user for input, then prints that input out with printf() without any
format specifiers.

Within the executable, there is a function called win(). This function is never explicitly called
by the program, but if we can get it to execute, it will most likely reveal the flag. I ran the
command nm on the executable to expose the memory addresses of various items in the program, and
I was able to determine that the win() function was located at 0x401236.

The next step was to somehow exploit the format string vulnerability to place the win() function's
address on the stack, causing it to be executed and reveal the flag. This is where I got stuck.
By providing "aaaa%p%p%p%p%p%p%p%p" as input to the program, I could see where my input was being
placed on the stack (the %p specifier reveals pointers on the stack) by looking for a bunch of 61's,
which is the hexadecimal code for the character "a." I could not figure out, however, how to get
the address of win() to that location. I also could not figure out how to write the address of win()
as ASCII characters, which seemed to be a necessary step, since the input seemed to be processed as
ASCII text. Multiple characters from the ASCII version of win()'s address are not actual keyboard
characters.

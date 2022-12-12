# CS110 Final Exam

## SHORT DESCRIPTION *(1 or 2 sentences describing your program)*
  Fetches random facts(from an api), and searches through and emoji api for relevant emojis.

## KNOWN BUGS AND INCOMPLETE PARTS *(list any known bugs or non-working parts)*
  Pygame is seemingly unable to blit emojis to the screen, no matter the font I choose. And so the emojis are only visible in the shell/console.

## REFERENCES *(any resources you use outside of class materials)*
  Used code found online to wrap my text to the next line when it got too long so it wouldnt spill over off the sides of the window. Nothing revolutionary, mainly used just to save time.
  Reference: https://stackoverflow.com/questions/64273966/python-pygame-make-text-in-pygame-wrap-when-in-leaves-the-window

## MISCELLANEOUS COMMENTS *(anything else you would like the grader to know)*
  - colors.py is a list of colors for the background to cycle through that I chose myself. Some are a bit bright, apologies.
  - The blinking text was made by mapping it's alpha to the amount of milliseconds that have passed. After subtracting the seconds, the closer the millisecond value is to 500, the more visible the text is.
  - I felt loading screens were necessary because the emoji search takes so damn long.
  - 
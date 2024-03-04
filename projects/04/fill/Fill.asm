// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen
// by writing 'black' in every pixel;
// the screen should remain fully black as long as the key is pressed. 
// When no key is pressed, the program clears the screen by writing
// 'white' in every pixel;
// the screen should remain fully clear as long as no key is pressed.

//// Replace this comment with your code.


(LOOP)
//@8192
@50
D=A
@counter
M=D

@KBD
D=M
@WHITE
D;JEQ

(BLACK)
@counter
M=M-1   // lowers our counter
D=M
@SCREEN
A=A+D
M=-1
@LOOP
D;JEQ // jumps when our counter reaches zero
@BLACK
0;JEQ

(WHITE)
@counter
M=M-1   // lowers our counter
D=M  // D = counter
@SCREEN
A=A+D
M=0
@LOOP
D;JEQ
@WHITE
0;JEQ

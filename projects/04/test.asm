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


@SCREEN
D=A
@addr
M=D

@0
D=M
@n
M=D // sets our n to MEM[0]

@i
M=0 // i is set to zero

(LOOP)
@i
D=M
@n
D=D-M
@END
D;JGT // if i>n

@addr
A=M
M=-1

@i
M=M+1
@32
D=A
@addr
M=D+M // adds 32 to addr
@LOOP
0;JMP

(END)
@END
0;JMP

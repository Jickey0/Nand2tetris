// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Mult.asm

// Multiplies two numbers A * B = C
// The inputs of this program are the values stored
// in R0 and R1 (RAM[0] and RAM[1]).

// C = 0
// for i in range(A):
//     C = C + B
// return C

@0
D=M
@counter // i refers to some mem. location.
M=D // i=MEM[0]

@1
D=M
@2 // sum refers to some mem. location.
M=0 // sum=MEM[1]

(LOOP)
@counter
D=M // D=sum
@END
D;JLE // If the sum is zero goto END
@1
D=M // D=MEM[1]
@2
M=D+M // sum=sum+i
@counter
M=M-1 // i=i-1
@LOOP
0;JMP // Goto LOOP

(END)
@END
0;JMP // Infinite loop

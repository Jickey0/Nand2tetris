
// PUSH CONST 17
@17
D=A
@SP
A=M
M=D
@SP
M=M+1

// PUSH CONST 17
@17
D=A
@SP
A=M
M=D
@SP
M=M+1

// eq
@SP
M=M-1
A=M
D=M
A=A-1
D=M-D // sub to see if they equal zero
@FOO0
D;JEQ
D=0
@BAR0
0;JMP
(FOO0)
D=-1
(BAR0)
@SP
A=M
A=A-1
M=D

// PUSH CONST 17
@17
D=A
@SP
A=M
M=D
@SP
M=M+1

// PUSH CONST 16
@16
D=A
@SP
A=M
M=D
@SP
M=M+1

// eq
@SP
M=M-1
A=M
D=M
A=A-1
D=M-D // sub to see if they equal zero
@FOO1
D;JEQ
D=0
@BAR1
0;JMP
(FOO1)
D=-1
(BAR1)
@SP
A=M
A=A-1
M=D

// PUSH CONST 16
@16
D=A
@SP
A=M
M=D
@SP
M=M+1

// PUSH CONST 17
@17
D=A
@SP
A=M
M=D
@SP
M=M+1

// eq
@SP
M=M-1
A=M
D=M
A=A-1
D=M-D // sub to see if they equal zero
@FOO2
D;JEQ
D=0
@BAR2
0;JMP
(FOO2)
D=-1
(BAR2)
@SP
A=M
A=A-1
M=D

// PUSH CONST 892
@892
D=A
@SP
A=M
M=D
@SP
M=M+1

// PUSH CONST 891
@891
D=A
@SP
A=M
M=D
@SP
M=M+1

// lt
@SP
M=M-1
A=M
D=M
A=A-1
D=M-D // sub to see if 
@FOO3
D;JLT
D=0
@BAR3
0;JMP
(FOO3)
D=-1
(BAR3)
@SP
A=M
A=A-1
M=D

// PUSH CONST 891
@891
D=A
@SP
A=M
M=D
@SP
M=M+1

// PUSH CONST 892
@892
D=A
@SP
A=M
M=D
@SP
M=M+1

// lt
@SP
M=M-1
A=M
D=M
A=A-1
D=M-D // sub to see if 
@FOO4
D;JLT
D=0
@BAR4
0;JMP
(FOO4)
D=-1
(BAR4)
@SP
A=M
A=A-1
M=D

// PUSH CONST 891
@891
D=A
@SP
A=M
M=D
@SP
M=M+1

// PUSH CONST 891
@891
D=A
@SP
A=M
M=D
@SP
M=M+1

// lt
@SP
M=M-1
A=M
D=M
A=A-1
D=M-D // sub to see if 
@FOO5
D;JLT
D=0
@BAR5
0;JMP
(FOO5)
D=-1
(BAR5)
@SP
A=M
A=A-1
M=D

// PUSH CONST 32767
@32767
D=A
@SP
A=M
M=D
@SP
M=M+1

// PUSH CONST 32766
@32766
D=A
@SP
A=M
M=D
@SP
M=M+1

// gt
@SP
M=M-1
A=M
D=M
A=A-1
D=M-D // sub to see if 
@FOO6
D;JGT
D=0
@BAR6
0;JMP
(FOO6)
D=-1
(BAR6)
@SP
A=M
A=A-1
M=D

// PUSH CONST 32766
@32766
D=A
@SP
A=M
M=D
@SP
M=M+1

// PUSH CONST 32767
@32767
D=A
@SP
A=M
M=D
@SP
M=M+1

// gt
@SP
M=M-1
A=M
D=M
A=A-1
D=M-D // sub to see if 
@FOO7
D;JGT
D=0
@BAR7
0;JMP
(FOO7)
D=-1
(BAR7)
@SP
A=M
A=A-1
M=D

// PUSH CONST 32766
@32766
D=A
@SP
A=M
M=D
@SP
M=M+1

// PUSH CONST 32766
@32766
D=A
@SP
A=M
M=D
@SP
M=M+1

// gt
@SP
M=M-1
A=M
D=M
A=A-1
D=M-D // sub to see if 
@FOO8
D;JGT
D=0
@BAR8
0;JMP
(FOO8)
D=-1
(BAR8)
@SP
A=M
A=A-1
M=D

// PUSH CONST 57
@57
D=A
@SP
A=M
M=D
@SP
M=M+1

// PUSH CONST 31
@31
D=A
@SP
A=M
M=D
@SP
M=M+1

// PUSH CONST 53
@53
D=A
@SP
A=M
M=D
@SP
M=M+1

// ADD
@SP
M=M-1
A=M
D=M
A=A-1
D=D+M
M=D

// PUSH CONST 112
@112
D=A
@SP
A=M
M=D
@SP
M=M+1

// SUB
@SP
M=M-1
A=M
D=M
A=A-1
D=M-D
M=D

// NEGATIVE
@SP
A=M
A=A-1
M=-M

// and
@SP
M=M-1
A=M
D=M
A=A-1
D=M&D
M=D

// PUSH CONST 82
@82
D=A
@SP
A=M
M=D
@SP
M=M+1

// or
@SP
M=M-1
A=M
D=M
A=A-1
D=M|D
M=D

// NOT
@SP
A=M
A=A-1
M=!M

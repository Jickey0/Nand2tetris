
// PUSH ARG 1
@1
D=A
@ARG
D=D+M
A=D // move to the addr
D=M // save that value to D
@SP
A=M
M=D
@SP
M=M+1

// pop po1nter THAT
@SP
AM=M-1
D=M
@THAT
M=D

// PUSH CONST 0
@0
D=A
@SP
A=M
M=D
@SP
M=M+1

// POP THAT 0
@0
D=A
@THAT
D=D+M
@14
M=D // adress of value to be popped
@SP
M=M-1
A=M
D=M
@14
A=M
M=D

// PUSH CONST 1
@1
D=A
@SP
A=M
M=D
@SP
M=M+1

// POP THAT 1
@1
D=A
@THAT
D=D+M
@14
M=D // adress of value to be popped
@SP
M=M-1
A=M
D=M
@14
A=M
M=D

// PUSH ARG 0
@0
D=A
@ARG
D=D+M
A=D // move to the addr
D=M // save that value to D
@SP
A=M
M=D
@SP
M=M+1

// PUSH CONST 2
@2
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

// POP ARG 0
@0
D=A
@ARG
D=D+M
@14
M=D // adress of value to be popped
@SP
M=M-1
A=M
D=M
@14
A=M
M=D

// create Label
(LOOP)

// PUSH ARG 0
@0
D=A
@ARG
D=D+M
A=D // move to the addr
D=M // save that value to D
@SP
A=M
M=D
@SP
M=M+1

// if-goto -- not sure if im supposed to pop the val or not
@SP
M=M-1
A=M
D=M
@COMPUTE_ELEMENT
D;JGT

// GOTO 
@END
0;JMP

// create Label
(COMPUTE_ELEMENT)

// PUSH THAT 0
@0
D=A
@THAT
D=D+M
A=D // move to the addr
D=M // save that value to D
@SP
A=M
M=D
@SP
M=M+1

// PUSH THAT 1
@1
D=A
@THAT
D=D+M
A=D // move to the addr
D=M // save that value to D
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

// POP THAT 2
@2
D=A
@THAT
D=D+M
@14
M=D // adress of value to be popped
@SP
M=M-1
A=M
D=M
@14
A=M
M=D

// PUSH THIS 1
@1
D=A
@THIS
D=D+A
A=D // move to the addr
D=M // save that value to D
@SP
A=M
M=D
@SP
M=M+1

// PUSH CONST 1
@1
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

// pop po1nter THAT
@SP
AM=M-1
D=M
@THAT
M=D

// PUSH ARG 0
@0
D=A
@ARG
D=D+M
A=D // move to the addr
D=M // save that value to D
@SP
A=M
M=D
@SP
M=M+1

// PUSH CONST 1
@1
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

// POP ARG 0
@0
D=A
@ARG
D=D+M
@14
M=D // adress of value to be popped
@SP
M=M-1
A=M
D=M
@14
A=M
M=D

// GOTO 
@LOOP
0;JMP

// create Label
(END)

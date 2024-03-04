
// PUSH CONST 3030
@3030
D=A
@SP
A=M
M=D
@SP
M=M+1

// pop po1nter THIS
@SP
AM=M-1
D=M
@THIS
M=D

// PUSH CONST 3040
@3040
D=A
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

// PUSH CONST 32
@32
D=A
@SP
A=M
M=D
@SP
M=M+1

// POP THIS 2
@2
D=A
@THIS
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

// PUSH CONST 46
@46
D=A
@SP
A=M
M=D
@SP
M=M+1

// POP THAT 6
@6
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

// PUSH THIS 0
@0
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

// ADD
@SP
M=M-1
A=M
D=M
A=A-1
D=D+M
M=D

// PUSH THIS 2
@2
D=A
@THIS
D=D+M
A=D // move to the addr
D=M // save that value to D
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

// PUSH THAT 6
@6
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

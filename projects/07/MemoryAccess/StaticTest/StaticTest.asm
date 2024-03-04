
// PUSH CONST 111
@111
D=A
@SP
A=M
M=D
@SP
M=M+1

// PUSH CONST 333
@333
D=A
@SP
A=M
M=D
@SP
M=M+1

// PUSH CONST 888
@888
D=A
@SP
A=M
M=D
@SP
M=M+1

// POP 16 8
@8
D=A
@16
D=D+A
@14
M=D // adress of value to be popped
@SP
M=M-1
A=M
D=M
@14
A=M
M=D

// POP 16 3
@3
D=A
@16
D=D+A
@14
M=D // adress of value to be popped
@SP
M=M-1
A=M
D=M
@14
A=M
M=D

// POP 16 1
@1
D=A
@16
D=D+A
@14
M=D // adress of value to be popped
@SP
M=M-1
A=M
D=M
@14
A=M
M=D

// PUSH 16 3
@3
D=A
@16
D=D+A
A=D // move to the addr
D=M // save that value to D
@SP
A=M
M=D
@SP
M=M+1

// PUSH 16 1
@1
D=A
@16
D=D+A
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

// PUSH 16 8
@8
D=A
@16
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

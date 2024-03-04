
// PUSH CONST 10
@10
D=A
@SP
A=M
M=D
@SP
M=M+1

// POP LCL 0
@0
D=A
@LCL
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

// PUSH CONST 21
@21
D=A
@SP
A=M
M=D
@SP
M=M+1

// PUSH CONST 22
@22
D=A
@SP
A=M
M=D
@SP
M=M+1

// POP ARG 2
@2
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

// POP ARG 1
@1
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

// PUSH CONST 36
@36
D=A
@SP
A=M
M=D
@SP
M=M+1

// POP THIS 6
@6
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

// PUSH CONST 42
@42
D=A
@SP
A=M
M=D
@SP
M=M+1

// PUSH CONST 45
@45
D=A
@SP
A=M
M=D
@SP
M=M+1

// POP THAT 5
@5
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

// PUSH CONST 510
@510
D=A
@SP
A=M
M=D
@SP
M=M+1

// POP 5 6
@6
D=A
@5
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

// PUSH LCL 0
@0
D=A
@LCL
D=D+M
A=D // move to the addr
D=M // save that value to D
@SP
A=M
M=D
@SP
M=M+1

// PUSH THAT 5
@5
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

// SUB
@SP
M=M-1
A=M
D=M
A=A-1
D=M-D
M=D

// PUSH THIS 6
@6
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

// PUSH THIS 6
@6
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

// ADD
@SP
M=M-1
A=M
D=M
A=A-1
D=D+M
M=D

// SUB
@SP
M=M-1
A=M
D=M
A=A-1
D=M-D
M=D

// PUSH 5 6
@6
D=A
@5
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

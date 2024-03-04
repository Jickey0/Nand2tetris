
// funct2on
(SimpleFunction.test)

@2 // saves 2nput loop #
D=A

(ZEROLOOP1) // create zeros 2f needed
@ENDZEROLOOP11
D;JEQ
D=D-1

// push const 0
@SP
A=M
M=0
@SP
M=M+1

@ZEROLOOP1
0;JMP

(ENDZEROLOOP11)

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

// PUSH LCL 1
@1
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

// ADD
@SP
M=M-1
A=M
D=M
A=A-1
D=D+M
M=D

// NOT
@SP
A=M
A=A-1
M=!M

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

// endFrame and retAddr are temporary variables.
// The pointer notation *addr denotes RAM[addr].
// endFrame = LCL // gets the address at the frame’s end
@LCL
D=M
@endFrame
M=D

// retAddr = *(endFrame – 5) // gets the return address
@5
D=A
@endFrame
D=M-D
A=D
D=M
@retAddr
M=D

// *ARG = pop() // puts the return value for the caller
@SP
M=M-1
A=M
D=M
@ARG
A=M
M=D

// SP = ARG + 1 // repositions SP
@ARG
D=M+1
@SP
M=D

// THAT = *(endFrame – 1) // restores THAT
@1
D=A
@endFrame
D=M-D
A=D
D=M
@THAT
M=D

// THIS = *(endFrame – 2) // restores THIS
@2
D=A
@endFrame
D=M-D
A=D
D=M
@THIS
M=D

// ARG = *(endFrame – 3) // restores ARG
@3
D=A
@endFrame
D=M-D
A=D
D=M
@ARG
M=D

// LCL = *(endFrame – 4) // restores LCL
@4
D=A
@endFrame
D=M-D
A=D
D=M
@LCL
M=D

// GOTO return adress
@retAddr
A=M
0;JMP

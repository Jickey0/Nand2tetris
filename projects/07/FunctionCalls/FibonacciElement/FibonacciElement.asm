 
// starts the SP at 256
@256
D=A
@SP
M=D

// call functionName nArgs
// push retAddrLabel1 // Generates and pushes this label // subtracts the # of args
@retAddrLabel1
D=A
@SP
A=M
M=D
@SP
M=M+1

// push LCL // Saves the caller’s LCL
@LCL
D=M
@SP
M=M+1 // move sp up
A=M
A=A-1 // move down sp to save the val
M=D

// push ARG // Saves the caller’s ARG
@ARG
D=M
@SP
M=M+1 // move sp up
A=M
A=A-1 // move down sp to save the val
M=D

// push THIS // Saves the caller’s THIS
@THIS
D=M
@SP
M=M+1 // move sp up
A=M
A=A-1 // move down sp to save the val
M=D

// push THAT // Saves the caller’s THAT
@THAT
D=M
@SP
M=M+1 // move sp up
A=M
A=A-1 // move down sp to save the val
M=D

// ARG = SP – 5 – nArgs // Repositions ARG
@5
D=A
@0
D=D+A
@SP
D=M-D
@ARG
M=D

// LCL = SP // Repositions LCL
@SP
D=M
@LCL
M=D

// goto functionName // Transfers control to the callee
@Sys.init
0;JMP

// (retAddrLabel1) // Injects this label into the code // still confused but oh well
(retAddrLabel1)

// funct0on
(Main.fibonacci)

@0 // saves 0nput loop #
D=A

(ZEROLOOP3) // create zeros 0f needed
@ENDZEROLOOP33
D;JEQ
D=D-1

// push const 0
@SP
A=M
M=0
@SP
M=M+1

@ZEROLOOP3
0;JMP

(ENDZEROLOOP33)

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

// if-goto -- not sure if im supposed to pop the val or not
@SP
M=M-1
A=M
D=M
@N_LT_2
D;JGT

// GOTO 
@N_GE_2
0;JMP

// create Label
(N_LT_2)

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

// create Label
(N_GE_2)

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

// call functionName nArgs
// push retAddrLabel12 // Generates and pushes this label // subtracts the # of args
@retAddrLabel12
D=A
@SP
A=M
M=D
@SP
M=M+1

// push LCL // Saves the caller’s LCL
@LCL
D=M
@SP
M=M+1 // move sp up
A=M
A=A-1 // move down sp to save the val
M=D

// push ARG // Saves the caller’s ARG
@ARG
D=M
@SP
M=M+1 // move sp up
A=M
A=A-1 // move down sp to save the val
M=D

// push THIS // Saves the caller’s THIS
@THIS
D=M
@SP
M=M+1 // move sp up
A=M
A=A-1 // move down sp to save the val
M=D

// push THAT // Saves the caller’s THAT
@THAT
D=M
@SP
M=M+1 // move sp up
A=M
A=A-1 // move down sp to save the val
M=D

// ARG = SP – 5 – nArgs // Repositions ARG
@5
D=A
@1
D=D+A
@SP
D=M-D
@ARG
M=D

// LCL = SP // Repositions LCL
@SP
D=M
@LCL
M=D

// goto functionName // Transfers control to the callee
@Main.fibonacci
0;JMP

// (retAddrLabel12) // Injects this label into the code // still confused but oh well
(retAddrLabel12)

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

// call functionName nArgs
// push retAddrLabel15 // Generates and pushes this label // subtracts the # of args
@retAddrLabel15
D=A
@SP
A=M
M=D
@SP
M=M+1

// push LCL // Saves the caller’s LCL
@LCL
D=M
@SP
M=M+1 // move sp up
A=M
A=A-1 // move down sp to save the val
M=D

// push ARG // Saves the caller’s ARG
@ARG
D=M
@SP
M=M+1 // move sp up
A=M
A=A-1 // move down sp to save the val
M=D

// push THIS // Saves the caller’s THIS
@THIS
D=M
@SP
M=M+1 // move sp up
A=M
A=A-1 // move down sp to save the val
M=D

// push THAT // Saves the caller’s THAT
@THAT
D=M
@SP
M=M+1 // move sp up
A=M
A=A-1 // move down sp to save the val
M=D

// ARG = SP – 5 – nArgs // Repositions ARG
@5
D=A
@1
D=D+A
@SP
D=M-D
@ARG
M=D

// LCL = SP // Repositions LCL
@SP
D=M
@LCL
M=D

// goto functionName // Transfers control to the callee
@Main.fibonacci
0;JMP

// (retAddrLabel15) // Injects this label into the code // still confused but oh well
(retAddrLabel15)

// ADD
@SP
M=M-1
A=M
D=M
A=A-1
D=D+M
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

// funct0on
(Sys.init)

@0 // saves 0nput loop #
D=A

(ZEROLOOP19) // create zeros 0f needed
@ENDZEROLOOP1919
D;JEQ
D=D-1

// push const 0
@SP
A=M
M=0
@SP
M=M+1

@ZEROLOOP19
0;JMP

(ENDZEROLOOP1919)

// PUSH CONST 4
@4
D=A
@SP
A=M
M=D
@SP
M=M+1

// call functionName nArgs
// push retAddrLabel21 // Generates and pushes this label // subtracts the # of args
@retAddrLabel21
D=A
@SP
A=M
M=D
@SP
M=M+1

// push LCL // Saves the caller’s LCL
@LCL
D=M
@SP
M=M+1 // move sp up
A=M
A=A-1 // move down sp to save the val
M=D

// push ARG // Saves the caller’s ARG
@ARG
D=M
@SP
M=M+1 // move sp up
A=M
A=A-1 // move down sp to save the val
M=D

// push THIS // Saves the caller’s THIS
@THIS
D=M
@SP
M=M+1 // move sp up
A=M
A=A-1 // move down sp to save the val
M=D

// push THAT // Saves the caller’s THAT
@THAT
D=M
@SP
M=M+1 // move sp up
A=M
A=A-1 // move down sp to save the val
M=D

// ARG = SP – 5 – nArgs // Repositions ARG
@5
D=A
@1
D=D+A
@SP
D=M-D
@ARG
M=D

// LCL = SP // Repositions LCL
@SP
D=M
@LCL
M=D

// goto functionName // Transfers control to the callee
@Main.fibonacci
0;JMP

// (retAddrLabel21) // Injects this label into the code // still confused but oh well
(retAddrLabel21)

// create Label
(END)

// GOTO 
@END
0;JMP

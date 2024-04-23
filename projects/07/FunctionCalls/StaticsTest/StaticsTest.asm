 
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
(Class1.set)

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

// POP static0Var0 0
@0
D=A
@static0Var0
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

// POP static0Var1 1
@1
D=A
@static0Var1
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

// PUSH CONST 0
@0
D=A
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

// funct0on
(Class1.get)

@0 // saves 0nput loop #
D=A

(ZEROLOOP6) // create zeros 0f needed
@ENDZEROLOOP66
D;JEQ
D=D-1

// push const 0
@SP
A=M
M=0
@SP
M=M+1

@ZEROLOOP6
0;JMP

(ENDZEROLOOP66)

// PUSH static0Var0 0
@0
D=A
@static0Var0
D=D+A
A=D // move to the addr
D=M // save that value to D
@SP
A=M
M=D
@SP
M=M+1

// PUSH static0Var1 1
@1
D=A
@static0Var1
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

(ZEROLOOP10) // create zeros 0f needed
@ENDZEROLOOP1010
D;JEQ
D=D-1

// push const 0
@SP
A=M
M=0
@SP
M=M+1

@ZEROLOOP10
0;JMP

(ENDZEROLOOP1010)

// PUSH CONST 6
@6
D=A
@SP
A=M
M=D
@SP
M=M+1

// PUSH CONST 8
@8
D=A
@SP
A=M
M=D
@SP
M=M+1

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
@2
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
@Class1.set
0;JMP

// (retAddrLabel12) // Injects this label into the code // still confused but oh well
(retAddrLabel12)

// POP 5 0
@0
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

// PUSH CONST 23
@23
D=A
@SP
A=M
M=D
@SP
M=M+1

// PUSH CONST 15
@15
D=A
@SP
A=M
M=D
@SP
M=M+1

// call functionName nArgs
// push retAddrLabel14 // Generates and pushes this label // subtracts the # of args
@retAddrLabel14
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
@2
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
@Class2.set
0;JMP

// (retAddrLabel14) // Injects this label into the code // still confused but oh well
(retAddrLabel14)

// POP 5 0
@0
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

// call functionName nArgs
// push retAddrLabel16 // Generates and pushes this label // subtracts the # of args
@retAddrLabel16
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
@Class1.get
0;JMP

// (retAddrLabel16) // Injects this label into the code // still confused but oh well
(retAddrLabel16)

// call functionName nArgs
// push retAddrLabel18 // Generates and pushes this label // subtracts the # of args
@retAddrLabel18
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
@Class2.get
0;JMP

// (retAddrLabel18) // Injects this label into the code // still confused but oh well
(retAddrLabel18)

// create Label
(END)

// GOTO 
@END
0;JMP

// funct0on
(Class2.set)

@0 // saves 0nput loop #
D=A

(ZEROLOOP22) // create zeros 0f needed
@ENDZEROLOOP2222
D;JEQ
D=D-1

// push const 0
@SP
A=M
M=0
@SP
M=M+1

@ZEROLOOP22
0;JMP

(ENDZEROLOOP2222)

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

// POP static2Var0 0
@0
D=A
@static2Var0
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

// POP static2Var1 1
@1
D=A
@static2Var1
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

// PUSH CONST 0
@0
D=A
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

// funct0on
(Class2.get)

@0 // saves 0nput loop #
D=A

(ZEROLOOP25) // create zeros 0f needed
@ENDZEROLOOP2525
D;JEQ
D=D-1

// push const 0
@SP
A=M
M=0
@SP
M=M+1

@ZEROLOOP25
0;JMP

(ENDZEROLOOP2525)

// PUSH static2Var0 0
@0
D=A
@static2Var0
D=D+A
A=D // move to the addr
D=M // save that value to D
@SP
A=M
M=D
@SP
M=M+1

// PUSH static2Var1 1
@1
D=A
@static2Var1
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

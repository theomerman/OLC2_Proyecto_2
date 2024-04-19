.data
    my_variable: .word 4   # Declare a variable named my_variable and initialize it to 0
    my_word: .string "first result: "

.text
    .global _start  # Declare the entry point

_start:
	lw a0, my_word
	li a7, 4
	ecall

    
	li a7, 93
	ecall
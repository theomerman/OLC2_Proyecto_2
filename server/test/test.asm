# For
.data
next_line: .string "\n"
.text
_start:
  # Inicio de for
	j begin_for1
    
begin_for1:
	declaracion de variable
	
	j for_condition2

for_condition2:
	condicion de for
	
	bgtz t1, for_block3
	j exit_label4
    

for_block3:
	# instrucciones
	modificacion variable
	j for_condition2
	
	
exit_for4:
	li a7, 10
	ecall





# Switch

.data
next_line: .string "\n"
.text
_start:
	j begin_switch0
	
begin_switch1:

	jal case1
	jal case2
	jal case3
	j exit4
	
case1:
	cargar_comparasion
	beq t0,t1 case1_true
	jalr ra

case1_true:
  instrucciones
  jalr ra


case2:
	cargar_comparasion
	beq t0,t1 case2_true
	jalr ra

case2_true:
  instrucciones
  jalr ra


case3:
	cargar_comparasion
	beq t0,t1 case3_true
	jalr ra

case3_true:
  instrucciones
  jalr ra

exit4:
	li a7, 10
	ecall
	
	


# array
	la t0, arr
	addi t1, t0, 4
	lw a0 0(t1)
	
	li a7, 1
	ecall
	
	
	
	li a7, 10
	ecall

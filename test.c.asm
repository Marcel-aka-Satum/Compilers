.data 
	text0: .asciiz "test" 
.text 
main:
	addiu   $sp, $sp, -20
	sw   $ra, 16($sp)
	sw   $fp, 12($sp)
	move  $fp, $sp
	# this should print the numbers: 0, 1, 2, 3, 4, 5
	addiu    $t0, $zero, 0
	sw   $t0, 8($fp)
	jal loop0
	addiu    $v0, $zero, 0
	move  $sp, $fp
	lw   $fp, 12($sp)
	lw   $ra, 16($sp)
	addiu   $sp, $sp, 20
	jal    exit
loop0:
	addiu    $t0, $zero, 10
	sw   $t0, 4($fp)
	lw   $t0, 8($fp)
	addiu  $t0, $t0, 1
	sw $t0, 8($fp)
	li $v0, 4 
	la $a0, text0
 	syscall 
	addiu    $t0, $zero, 10
	sw   $t0, 8($fp)
	lw   $t0, 8($fp)
	li $v0, 1 
	move $a0, $t0
 	syscall 
	blt  $t0,10, loop0
	jr   $ra
	# this should print the numbers: 0, 1, 2, 3, 4, 5
exit:
 	 li $v0, 10 
 	 syscall
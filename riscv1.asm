.data
next_line: .string "\n"
str0: .string "----------------------"
str1: .string "----ARCHIVO BASICO----"
str2: .string "--------21 pts--------"
str3: .string "----------------------"
str4: .string "imprimir"
str5: .string "cadena valida"
str6: .string "El valor de val1 es:"
str7: .string "El valor de val2 es:"
str8: .string "El valor de val3 es:"
str9: .string "El resultado de la operación es:"
str10: .string "El valor de bol es:"
str11: .string "El valor de cad1 es:"
str12: .string "El valor de cad2 es:"
str13: .string "El valor de bol2:"
.text
_start:
	la a0, str0
	li a7, 4
	ecall
	la a0, next_line
	li a7, 4
	ecall
	la a0, str1
	li a7, 4
	ecall
	la a0, next_line
	li a7, 4
	ecall
	la a0, str2
	li a7, 4
	ecall
	la a0, next_line
	li a7, 4
	ecall
	la a0, str3
	li a7, 4
	ecall
	la a0, next_line
	li a7, 4
	ecall
	li t0, 0
	li t1, 4
	sw t0, -1000(t1)
	li t0, 4
	lw t1, -1000(t0)
	beqz t1, if_true2
	li t1, 0
	li t0, 8
	sw t1, -1000(t0)
	j if_exit1
if_exit1:
	li t0, 2
	li t1, 12
	sw t0, -1000(t1)
	li t0, 6
	li t1, 16
	sw t0, -1000(t1)
	li t0, 16
	lw t0, -1000(t0)
	li t1, 12
	lw t1, -1000(t1)
	mul t2, t0, t1
	li t0, 20
	sw t2, -1000(t0)
	li t0, 50
	li t1, 24
	sw t0, -1000(t1)
	li t0, 24
	lw t0, -1000(t0)
	li t1, 20
	lw t1, -1000(t1)
	mul t2, t0, t1
	li t0, 28
	sw t2, -1000(t0)
	li t0, 3
	li t1, 32
	sw t0, -1000(t1)
	li t0, 3
	li t1, 36
	sw t0, -1000(t1)
	li t0, 8
	li t1, 40
	sw t0, -1000(t1)
	li t0, 40
	lw t0, -1000(t0)
	li t1, 36
	lw t1, -1000(t1)
	mul t2, t0, t1
	li t0, 44
	sw t2, -1000(t0)
	li t0, 44
	lw t0, -1000(t0)
	li t1, 32
	lw t1, -1000(t1)
	mul t2, t0, t1
	li t0, 48
	sw t2, -1000(t0)
	li t0, 3
	li t1, 52
	sw t0, -1000(t1)
	li t0, 2
	li t1, 56
	sw t0, -1000(t1)
	li t0, 56
	lw t0, -1000(t0)
	li t1, 52
	lw t1, -1000(t1)
	mul t2, t0, t1
	li t0, 60
	sw t2, -1000(t0)
	li t0, 5
	li t1, 64
	sw t0, -1000(t1)
	li t0, 64
	lw t0, -1000(t0)
	li t1, 60
	lw t1, -1000(t1)
	add t2, t0, t1
	li t0, 68
	sw t2, -1000(t0)
	li t0, 4
	li t1, 72
	sw t0, -1000(t1)
	li t0, 72
	lw t0, -1000(t0)
	li t1, 68
	lw t1, -1000(t1)
	mul t2, t0, t1
	li t0, 76
	sw t2, -1000(t0)
	li t0, 2
	li t1, 80
	sw t0, -1000(t1)
	li t0, 80
	lw t0, -1000(t0)
	li t1, 76
	lw t1, -1000(t1)
	add t2, t0, t1
	li t0, 84
	sw t2, -1000(t0)
	li t0, 10
	li t1, 88
	sw t0, -1000(t1)
	li t0, 88
	lw t0, -1000(t0)
	li t1, 84
	lw t1, -1000(t1)
	mul t2, t0, t1
	li t0, 92
	sw t2, -1000(t0)
	li t0, 5
	li t1, 96
	sw t0, -1000(t1)
	li t0, 96
	lw t0, -1000(t0)
	li t1, 92
	lw t1, -1000(t1)
	add t2, t0, t1
	li t0, 100
	sw t2, -1000(t0)
	li t0, 100
	lw t0, -1000(t0)
	li t1, 48
	lw t1, -1000(t1)
	sub t2, t0, t1
	li t0, 104
	sw t2, -1000(t0)
	li t0, 7
	li t1, 108
	sw t0, -1000(t1)
	li t0, 108
	lw t0, -1000(t0)
	li t1, 104
	lw t1, -1000(t1)
	sub t2, t0, t1
	li t0, 112
	sw t2, -1000(t0)
	li t0, 112
	lw t0, -1000(t0)
	li t1, 28
	lw t1, -1000(t1)
	add t2, t0, t1
	li t0, 116
	sw t2, -1000(t0)
	li t0, 3
	li t1, 120
	sw t0, -1000(t1)
	li t0, 2
	li t1, 124
	sw t0, -1000(t1)
	li t0, 124
	lw t0, -1000(t0)
	li t1, 120
	lw t1, -1000(t1)
	mul t2, t0, t1
	li t0, 128
	sw t2, -1000(t0)
	li t0, 5
	li t1, 132
	sw t0, -1000(t1)
	li t0, 132
	lw t0, -1000(t0)
	li t1, 128
	lw t1, -1000(t1)
	mul t2, t0, t1
	li t0, 136
	sw t2, -1000(t0)
	li t0, 6
	li t1, 140
	sw t0, -1000(t1)
	li t0, 140
	lw t0, -1000(t0)
	li t1, 136
	lw t1, -1000(t1)
	sub t2, t0, t1
	li t0, 144
	sw t2, -1000(t0)
	li t0, 8
	li t1, 148
	sw t0, -1000(t1)
	li t0, 5
	li t1, 152
	sw t0, -1000(t1)
	li t0, 10
	li t1, 156
	sw t0, -1000(t1)
	li t0, 7
	li t1, 160
	sw t0, -1000(t1)
	li t0, 7
	li t1, 164
	sw t0, -1000(t1)
	li t0, 7
	li t1, 168
	sw t0, -1000(t1)
	li t0, 168
	lw t0, -1000(t0)
	li t1, 164
	lw t1, -1000(t1)
	mul t2, t0, t1
	li t0, 172
	sw t2, -1000(t0)
	li t0, 172
	lw t0, -1000(t0)
	li t1, 160
	lw t1, -1000(t1)
	mul t2, t0, t1
	li t0, 176
	sw t2, -1000(t0)
	li t0, 9
	li t1, 180
	sw t0, -1000(t1)
	li t0, 180
	lw t0, -1000(t0)
	li t1, 176
	lw t1, -1000(t1)
	add t2, t0, t1
	li t0, 184
	sw t2, -1000(t0)
	li t0, 7
	li t1, 188
	sw t0, -1000(t1)
	li t0, 5
	li t1, 192
	sw t0, -1000(t1)
	li t0, 6
	li t1, 196
	sw t0, -1000(t1)
	li t0, 196
	lw t0, -1000(t0)
	li t1, 192
	lw t1, -1000(t1)
	mul t2, t0, t1
	li t0, 200
	sw t2, -1000(t0)
	li t0, 3
	li t1, 204
	sw t0, -1000(t1)
	li t0, 3
	li t1, 208
	sw t0, -1000(t1)
	li t0, 208
	lw t0, -1000(t0)
	li t1, 204
	lw t1, -1000(t1)
	mul t2, t0, t1
	li t0, 212
	sw t2, -1000(t0)
	li t0, 212
	lw t0, -1000(t0)
	li t1, 200
	lw t1, -1000(t1)
	sub t2, t0, t1
	li t0, 216
	sw t2, -1000(t0)
	li t0, 216
	lw t0, -1000(t0)
	li t1, 188
	lw t1, -1000(t1)
	sub t2, t0, t1
	li t0, 220
	sw t2, -1000(t0)
	li t0, 220
	lw t0, -1000(t0)
	li t1, 184
	lw t1, -1000(t1)
	sub t2, t0, t1
	li t0, 224
	sw t2, -1000(t0)
	li t0, 224
	lw t0, -1000(t0)
	li t1, 156
	lw t1, -1000(t1)
	add t2, t0, t1
	li t0, 228
	sw t2, -1000(t0)
	li t0, 6
	li t1, 232
	sw t0, -1000(t1)
	li t0, 8
	li t1, 236
	sw t0, -1000(t1)
	li t0, 236
	lw t0, -1000(t0)
	li t1, 232
	lw t1, -1000(t1)
	sub t2, t0, t1
	li t0, 240
	sw t2, -1000(t0)
	li t0, 240
	lw t0, -1000(t0)
	li t1, 228
	lw t1, -1000(t1)
	add t2, t0, t1
	li t0, 244
	sw t2, -1000(t0)
	li t0, 244
	lw t0, -1000(t0)
	li t1, 152
	lw t1, -1000(t1)
	sub t2, t0, t1
	li t0, 248
	sw t2, -1000(t0)
	li t0, 9
	li t1, 252
	sw t0, -1000(t1)
	li t0, 2
	li t1, 256
	sw t0, -1000(t1)
	li t0, 2
	li t1, 260
	sw t0, -1000(t1)
	li t0, 2
	li t1, 264
	sw t0, -1000(t1)
	li t0, 2
	li t1, 268
	sw t0, -1000(t1)
	li t0, 268
	lw t0, -1000(t0)
	li t1, 264
	lw t1, -1000(t1)
	mul t2, t0, t1
	li t0, 272
	sw t2, -1000(t0)
	li t0, 272
	lw t0, -1000(t0)
	li t1, 260
	lw t1, -1000(t1)
	mul t2, t0, t1
	li t0, 276
	sw t2, -1000(t0)
	li t0, 276
	lw t0, -1000(t0)
	li t1, 256
	lw t1, -1000(t1)
	mul t2, t0, t1
	li t0, 280
	sw t2, -1000(t0)
	li t0, 280
	lw t0, -1000(t0)
	li t1, 252
	lw t1, -1000(t1)
	sub t2, t0, t1
	li t0, 284
	sw t2, -1000(t0)
	li t0, 284
	lw t0, -1000(t0)
	li t1, 248
	lw t1, -1000(t1)
	sub t2, t0, t1
	li t0, 288
	sw t2, -1000(t0)
	li t0, 288
	lw t0, -1000(t0)
	li t1, 148
	lw t1, -1000(t1)
	add t2, t0, t1
	li t0, 292
	sw t2, -1000(t0)
	li t0, 292
	lw t0, -1000(t0)
	li t1, 144
	lw t1, -1000(t1)
	sub t2, t0, t1
	li t0, 296
	sw t2, -1000(t0)
	li t0, 2
	li t1, 300
	sw t0, -1000(t1)
	li t0, 2
	li t1, 304
	sw t0, -1000(t1)
	li t0, 2
	li t1, 308
	sw t0, -1000(t1)
	li t0, 2
	li t1, 312
	sw t0, -1000(t1)
	li t0, 2
	li t1, 316
	sw t0, -1000(t1)
	li t0, 2
	li t1, 320
	sw t0, -1000(t1)
	li t0, 320
	lw t0, -1000(t0)
	li t1, 316
	lw t1, -1000(t1)
	mul t2, t0, t1
	li t0, 324
	sw t2, -1000(t0)
	li t0, 324
	lw t0, -1000(t0)
	li t1, 312
	lw t1, -1000(t1)
	mul t2, t0, t1
	li t0, 328
	sw t2, -1000(t0)
	li t0, 328
	lw t0, -1000(t0)
	li t1, 308
	lw t1, -1000(t1)
	sub t2, t0, t1
	li t0, 332
	sw t2, -1000(t0)
	li t0, 332
	lw t0, -1000(t0)
	li t1, 304
	lw t1, -1000(t1)
	mul t2, t0, t1
	li t0, 336
	sw t2, -1000(t0)
	li t0, 1
	li t1, 340
	sw t0, -1000(t1)
	li t0, 3
	li t1, 344
	sw t0, -1000(t1)
	li t0, 296
	lw t0, -1000(t0)
	li t1, 344
	lw t1, -1000(t1)
	mul t2, t0, t1
	li t0, 348
	sw t2, -1000(t0)
	li t0, 2
	li t1, 352
	sw t0, -1000(t1)
	li t0, 352
	lw t0, -1000(t0)
	li t1, 348
	lw t1, -1000(t1)
	add t2, t0, t1
	li t0, 356
	sw t2, -1000(t0)
	li t0, 356
	lw t0, -1000(t0)
	li t1, 340
	lw t1, -1000(t1)
	add t2, t0, t1
	li t0, 360
	sw t2, -1000(t0)
	li t0, 360
	lw t0, -1000(t0)
	li t1, 336
	lw t1, -1000(t1)
	sub t2, t0, t1
	li t0, 364
	sw t2, -1000(t0)
	li t0, 116
	lw t0, -1000(t0)
	li t1, 364
	lw t1, -1000(t1)
	add t2, t0, t1
	li t0, 368
	sw t2, -1000(t0)
	li t0, 368
	lw t0, -1000(t0)
	li t1, 300
	lw t1, -1000(t1)
	sub t2, t0, t1
	li t0, 372
	sw t2, -1000(t0)
	la a0, str6
	li a7, 4
	ecall
	li t0, 116
	lw a0, -1000(t0)
	li a7, 1
	ecall
	la a0, next_line
	li a7, 4
	ecall
	la a0, str7
	li a7, 4
	ecall
	li t0, 296
	lw a0, -1000(t0)
	li a7, 1
	ecall
	la a0, next_line
	li a7, 4
	ecall
	la a0, str8
	li a7, 4
	ecall
	li t0, 372
	lw a0, -1000(t0)
	li a7, 1
	ecall
	la a0, next_line
	li a7, 4
	ecall
	la a0, str9
	li a7, 4
	ecall
	li t0, 372
	lw a0, -1000(t0)
	li a7, 1
	ecall
	la a0, next_line
	li a7, 4
	ecall
	la a0, str10
	li a7, 4
	ecall
	li t0, 4
	lw a0, -1000(t0)
	li a7, 1
	ecall
	la a0, next_line
	li a7, 4
	ecall
	la a0, str11
	li a7, 4
	ecall
	la a0, str4
	li a7, 4
	ecall
	la a0, next_line
	li a7, 4
	ecall
	la a0, str12
	li a7, 4
	ecall
	la a0, str5
	li a7, 4
	ecall
	la a0, next_line
	li a7, 4
	ecall
	la a0, str13
	li a7, 4
	ecall
	li t0, 8
	lw a0, -1000(t0)
	li a7, 1
	ecall
	la a0, next_line
	li a7, 4
	ecall
	li t0, 100
	li t1, 376
	sw t0, -1000(t1)
	li t0, 100
	li t1, 380
	sw t0, -1000(t1)
	li t0, 7
	li t1, 384
	sw t0, -1000(t1)
	li t0, 1
	li t1, 388
	sw t0, -1000(t1)
	li t0, 10
	li t1, 392
	sw t0, -1000(t1)
	li t0, 10
	li t1, 396
	sw t0, -1000(t1)
	li t0, 380
	lw t0, -1000(t0)
	li t1, 384
	lw t1, -1000(t1)
	blt t0, t1, if_true4
	li t0, 400
	li t1, 0
	sw t1, -1000(t0)
	j if_exit3
if_exit3:
	li t0, 376
	lw t0, -1000(t0)
	li t1, 380
	lw t1, -1000(t1)
	bgt t0, t1, if_true6
	li t0, 404
	li t1, 0
	sw t1, -1000(t0)
	j if_exit5
if_exit5:
	li t0, 404
	lw t0, -1000(t0)
	li t1, 400
	lw t1, -1000(t1)
	or t0, t0, t1
	li t1, 408
	sw t0, -1000(t1)
	li t0, 408
	lw a0, -1000(t0)
	li a7, 1
	ecall
	la a0, next_line
	li a7, 4
	ecall
	li t0, 14
	li t1, 412
	sw t0, -1000(t1)
	li t0, 412
	lw t0, -1000(t0)
	li t1, 384
	lw t1, -1000(t1)
	bne t0, t1, if_true8
	li t0, 416
	li t1, 0
	sw t1, -1000(t0)
	j if_exit7
if_exit7:
	li t0, 392
	lw t0, -1000(t0)
	li t1, 396
	lw t1, -1000(t1)
	beq t0, t1, if_true10
	li t0, 420
	li t1, 0
	sw t1, -1000(t0)
	j if_exit9
if_exit9:
	li t0, 376
	lw t0, -1000(t0)
	li t1, 380
	lw t1, -1000(t1)
	beq t0, t1, if_true12
	li t0, 424
	li t1, 0
	sw t1, -1000(t0)
	j if_exit11
if_exit11:
	li t0, 424
	lw t0, -1000(t0)
	li t1, 420
	lw t1, -1000(t1)
	and t0, t0, t1
	li t1, 428
	sw t0, -1000(t1)
	li t0, 428
	lw t0, -1000(t0)
	li t1, 416
	lw t1, -1000(t1)
	or t0, t0, t1
	li t1, 432
	sw t0, -1000(t1)
	li t0, 432
	lw a0, -1000(t0)
	li a7, 1
	ecall
	la a0, next_line
	li a7, 4
	ecall
	li t0, 5
	li t1, 436
	sw t0, -1000(t1)
	li t0, 5
	li t1, 440
	sw t0, -1000(t1)
	li t0, 100
	li t1, 444
	sw t0, -1000(t1)
	li t0, 1
	li t1, 448
	sw t0, -1000(t1)
	li t0, 448
	lw t1, -1000(t0)
	beqz t1, if_true14
	li t1, 0
	li t0, 452
	sw t1, -1000(t0)
	j if_exit13
if_exit13:
	li t0, 452
	lw t1, -1000(t0)
	beqz t1, if_true16
	li t1, 0
	li t0, 456
	sw t1, -1000(t0)
	j if_exit15
if_exit15:
	li t0, 436
	lw t0, -1000(t0)
	li t1, 436
	lw t1, -1000(t1)
	sub t2, t0, t1
	li t0, 460
	sw t2, -1000(t0)
	li t0, 50
	li t1, 464
	sw t0, -1000(t1)
	li t0, 50
	li t1, 468
	sw t0, -1000(t1)
	li t0, 468
	lw t0, -1000(t0)
	li t1, 464
	lw t1, -1000(t1)
	add t2, t0, t1
	li t0, 472
	sw t2, -1000(t0)
	li t0, 472
	lw t0, -1000(t0)
	li t1, 460
	lw t1, -1000(t1)
	add t2, t0, t1
	li t0, 476
	sw t2, -1000(t0)
	li t0, 444
	lw t0, -1000(t0)
	li t1, 476
	lw t1, -1000(t1)
	beq t0, t1, if_true18
	li t0, 480
	li t1, 0
	sw t1, -1000(t0)
	j if_exit17
if_exit17:
	li t0, 480
	lw t0, -1000(t0)
	li t1, 456
	lw t1, -1000(t1)
	and t0, t0, t1
	li t1, 484
	sw t0, -1000(t1)
	li t0, 484
	lw a0, -1000(t0)
	li a7, 1
	ecall
	la a0, next_line
	li a7, 4
	ecall
	li t0, 15
	li t1, 488
	sw t0, -1000(t1)
	li t0, 0
	li t1, 492
	sw t0, -1000(t1)
	li t0, 2
	li t1, 496
	sw t0, -1000(t1)
	li t0, 488
	lw t0, -1000(t0)
	li t1, 496
	lw t1, -1000(t1)
	rem t0, t0, t1
	li t1, 500
	sw t0, -1000(t1)
	li t0, 500
	lw t0, -1000(t0)
	li t1, 492
	lw t1, -1000(t1)
	beq t0, t1, if_true20
	li t0, 504
	li t1, 0
	sw t1, -1000(t0)
	j if_exit19
if_exit19:
	li t0, 504
	lw a0, -1000(t0)
	li a7, 1
	ecall
	la a0, next_line
	li a7, 4
	ecall
	li a7, 10
	ecall
if_true20:
	li t0, 504
	li t1, 1
	sw t1, -1000(t0)
	j if_exit19
if_true18:
	li t0, 480
	li t1, 1
	sw t1, -1000(t0)
	j if_exit17
if_true16:
	li t0, 456
	li t1, 1
	sw t1, -1000(t0)
	j if_exit15
if_true14:
	li t0, 452
	li t1, 1
	sw t1, -1000(t0)
	j if_exit13
if_true12:
	li t0, 424
	li t1, 1
	sw t1, -1000(t0)
	j if_exit11
if_true10:
	li t0, 420
	li t1, 1
	sw t1, -1000(t0)
	j if_exit9
if_true8:
	li t0, 416
	li t1, 1
	sw t1, -1000(t0)
	j if_exit7
if_true6:
	li t0, 404
	li t1, 1
	sw t1, -1000(t0)
	j if_exit5
if_true4:
	li t0, 400
	li t1, 1
	sw t1, -1000(t0)
	j if_exit3
if_true2:
	li t0, 8
	li t1, 1
	sw t1, -1000(t0)
	j if_exit1

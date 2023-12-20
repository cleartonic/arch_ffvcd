hirom

;================
;starting crystal
;================
org $E79F00
db $0F, $FF

;=================
;Chests and Events
;=================
org $C0FAB2 
db $20, $23
org $C0FAB4 
db $20, $45
org $C0FAB6 
db $60, $6B
org $C0FAB8 
db $60, $50
org $C0FABA 
db $20, $94
org $C0FABC 
db $20, $53
org $C0FABE 
db $20, $03
org $C0FAC0 
db $40, $AB
org $C0FAC2 
db $60, $24
org $C0FAC4 
db $20, $02
org $C0FAC6 
db $20, $35
org $C0FAC8 
db $60, $4D
org $C0FACA 
db $40, $95
org $C0FACC 
db $40, $B3
org $C0FACE 
db $60, $83
org $C0FAD0 
db $20, $3A
org $C0FAD2 
db $60, $0E
org $C0FAD4 
db $60, $75
org $C0FAD6 
db $20, $0E
org $C0FAD8 
db $60, $3A
org $C0FADA 
db $50, $11
org $C0FADC 
db $60, $30
org $C0FADE 
db $60, $6C
org $C0FAE0 
db $40, $52
org $C0FAE2 
db $20, $3C
org $C0FAE4 
db $40, $AF
org $C0FAE6 
db $60, $41
org $C0FAE8 
db $50, $13
org $C0FAEA 
db $20, $18
org $C0FAEC 
db $20, $14
org $C0FAEE 
db $60, $42
org $C0FAF0 
db $20, $44
org $C0FAF2 
db $20, $0F
org $C0FAF4 
db $40, $FC
org $C0FAF6 
db $20, $42
org $C0FAF8 
db $20, $9C
org $C0FAFA 
db $20, $56
org $C0FAFC 
db $20, $43
org $C0FAFE 
db $60, $87
org $C0FB02 
db $20, $95
org $C0FB04 
db $50, $10
org $C0FB06 
db $60, $60
org $C0FB08 
db $60, $06
org $C0FB0A 
db $60, $74
org $C0FB0C 
db $20, $4C
org $C0FB0E 
db $20, $0B
org $C0FB10 
db $40, $38
org $C0FB12 
db $60, $21
org $C0FB14 
db $40, $4D
org $C0FB16 
db $20, $5C
org $C0FB18 
db $40, $9D
org $C0FB1A 
db $60, $73
org $C0FB1C 
db $60, $14
org $C0FB1E 
db $20, $33
org $C0FB20 
db $20, $3D
org $C0FB22 
db $60, $4A
org $C0FB24 
db $60, $32
org $C0FB26 
db $20, $8D
org $C0FB28 
db $40, $E0
org $C0FB2A 
db $20, $97
org $C0FB2C 
db $60, $44
org $C0FB2E 
db $20, $48
org $C0FB30 
db $20, $9B
org $C0FB32 
db $60, $76
org $C0FB34 
db $60, $70
org $C0FB36 
db $60, $82
org $C0FB38 
db $20, $08
org $C0FB3A 
db $20, $9A
org $C0FB3C 
db $50, $12
org $C0FB3E 
db $20, $2F
org $C0FB40 
db $60, $81
org $D13212 
db $20, $22
org $D13216 
db $20, $51
org $D1321A 
db $60, $34
org $D1321E 
db $40, $55
org $D13222 
db $60, $71
org $D13226 
db $40, $2F
org $D1322A 
db $20, $1A
org $D1322E 
db $40, $6A
org $D13232 
db $20, $04
org $D13236 
db $60, $29
org $D1323A 
db $40, $68
org $D1323E 
db $20, $13
org $D13242 
db $40, $3E
org $D13246 
db $60, $0A
org $D1324A 
db $60, $27
org $D1324E 
db $50, $08
org $D13252 
db $20, $0D
org $D13256 
db $20, $39
org $D1325A 
db $50, $0D
org $D1325E 
db $40, $A1
org $D13262 
db $20, $88
org $D13266 
db $20, $10
org $D1326A 
db $60, $4B
org $D1326E 
db $20, $9D
org $D13272 
db $50, $05
org $D13276 
db $40, $AD
org $D1327A 
db $20, $32
org $D1327E 
db $40, $5F
org $D13282 
db $20, $8E
org $D13286 
db $60, $35
org $D1328A 
db $60, $58
org $D1328E 
db $40, $CB
org $D13292 
db $60, $13
org $D13296 
db $50, $04
org $D1329A 
db $60, $72
org $D1329E 
db $20, $8A
org $D132A2 
db $20, $2D
org $D132A6 
db $40, $18
org $D132AA 
db $40, $44
org $D132AE 
db $20, $47
org $D132B2 
db $40, $47
org $D132B6 
db $20, $3B
org $D132BA 
db $20, $16
org $D132BE 
db $60, $1F
org $D132C2 
db $40, $FE
org $D132C6 
db $40, $2E
org $D132CA 
db $60, $3C
org $D132CE 
db $20, $89
org $D132D2 
db $20, $4D
org $D132D6 
db $50, $14
org $D132DA 
db $60, $0C
org $D132DE 
db $40, $82
org $D132E2 
db $40, $22
org $D132E6 
db $40, $23
org $D132EA 
db $50, $15
org $D132EE 
db $40, $9E
org $D132F2 
db $60, $16
org $D132F6 
db $20, $49
org $D132FA 
db $40, $F3
org $D132FE 
db $20, $2E
org $D13302 
db $40, $59
org $D13306 
db $60, $28
org $D1330A 
db $60, $77
org $D1330E 
db $60, $80
org $D13312 
db $60, $51
org $D13316 
db $20, $4F
org $D1331A 
db $60, $7C
org $D1331E 
db $20, $25
org $D13322 
db $40, $16
org $D13326 
db $20, $84
org $D1332A 
db $60, $54
org $D1332E 
db $20, $12
org $D13332 
db $20, $26
org $D13336 
db $60, $78
org $D1333A 
db $50, $07
org $D1333E 
db $40, $E3
org $D13342 
db $60, $40
org $D13346 
db $40, $C0
org $D1334A 
db $40, $E3
org $D1334E 
db $60, $7B
org $D13352 
db $40, $C7
org $D13356 
db $40, $41
org $D1335A 
db $40, $8B
org $D1335E 
db $40, $0D
org $D13362 
db $40, $5A
org $D13366 
db $60, $48
org $D1336A 
db $20, $1B
org $D1336E 
db $60, $11
org $D13372 
db $40, $EB
org $D13376 
db $60, $7D
org $D1337A 
db $50, $00
org $D1337E 
db $60, $6A
org $D13382 
db $40, $9A
org $D13386 
db $20, $15
org $D1338A 
db $60, $39
org $D1338E 
db $60, $0B
org $D13392 
db $20, $01
org $D13396 
db $20, $3F
org $D1339A 
db $20, $92
org $D1339E 
db $50, $01
org $D133A2 
db $20, $50
org $D133A6 
db $40, $E5
org $D133AA 
db $40, $E2
org $D133AE 
db $40, $B2
org $D133B2 
db $60, $6F
org $D133B6 
db $60, $1E
org $D133BA 
db $40, $E3
org $D133BE 
db $40, $A0
org $D133C2 
db $40, $E1
org $D133C6 
db $40, $61
org $D133CA 
db $20, $20
org $D133CE 
db $20, $38
org $D133D2 
db $20, $41
org $D133D6 
db $20, $9E
org $D133DA 
db $60, $6D
org $D133DE 
db $60, $38
org $D133E2 
db $20, $57
org $D133E6 
db $20, $90
org $D133EA 
db $20, $31
org $D133EE 
db $60, $15
org $D133F2 
db $60, $09
org $D133F6 
db $60, $79
org $D133FA 
db $60, $0F
org $D133FE 
db $60, $6E
org $D13402 
db $20, $99
org $D13406 
db $20, $07
org $D1340A 
db $40, $BA
org $D1340E 
db $50, $03
org $D13412 
db $20, $98
org $D13416 
db $20, $2C
org $D1341A 
db $60, $7A
org $D1341E 
db $40, $25
org $D13422 
db $20, $40
org $D13426 
db $20, $55
org $D1342A 
db $60, $53
org $D1342E 
db $60, $3D
org $D13432 
db $60, $3B
org $D13436 
db $20, $30
org $D1343A 
db $40, $1E
org $D1343E 
db $40, $9F
org $D13442 
db $60, $1B
org $D13446 
db $60, $59
org $D1344A 
db $20, $93
org $D1344E 
db $40, $56
org $D13452 
db $20, $5E
org $D13456 
db $40, $49
org $D1345A 
db $20, $17
org $D1345E 
db $40, $12
org $D13462 
db $20, $5B
org $D13466 
db $20, $58
org $D1346A 
db $40, $29
org $D1346E 
db $50, $0F
org $D13472 
db $60, $31
org $D13476 
db $40, $E2
org $D1347A 
db $40, $67
org $D1347E 
db $40, $E3
org $D13482 
db $40, $E3
org $D13486 
db $40, $6B
org $D1348A 
db $20, $4B
org $D1348E 
db $20, $1C
org $D13492 
db $20, $9F
org $D13496 
db $20, $1F
org $D1349A 
db $50, $09
org $D1349E 
db $50, $06
org $D134A2 
db $40, $EB
org $D134A6 
db $60, $17
org $D134AA 
db $20, $0A
org $D134AE 
db $40, $EB
org $D134B2 
db $40, $EB
org $D134B6 
db $40, $EB
org $D134BA 
db $40, $BD
org $D134BE 
db $40, $1A
org $D134C2 
db $40, $F6
org $D134C6 
db $50, $0A
org $D134CA 
db $40, $0B
org $D134CE 
db $40, $E3
org $D134D2 
db $60, $08
org $D134D6 
db $40, $EB
org $D134DA 
db $60, $2A
org $D134DE 
db $60, $45
org $D134E2 
db $50, $0B
org $D134E6 
db $20, $2B
org $D134EA 
db $40, $C1
org $D134EE 
db $20, $96
org $D134F2 
db $60, $0D
org $D134F6 
db $50, $0C
org $D134FA 
db $40, $19
org $D134FE 
db $40, $85
org $D13502 
db $20, $8C
org $D13506 
db $40, $F9
org $D1350A 
db $20, $59
org $D1350E 
db $60, $07
org $D13512 
db $40, $51
org $D13516 
db $40, $CE
org $D1351A 
db $20, $91
org $D1351E 
db $40, $07
org $D13522 
db $40, $5E
org $D13526 
db $40, $EF
org $D1352A 
db $20, $52
org $D1352E 
db $20, $5D
org $D13532 
db $40, $4C
org $D13536 
db $20, $24
org $D1353A 
db $20, $46
org $D1353E 
db $60, $1C
org $D13542 
db $60, $49
org $D13546 
db $20, $29
org $D1354A 
db $20, $05
org $D1354E 
db $20, $06
org $D13552 
db $60, $22
org $D13556 
db $40, $58
org $D1355A 
db $20, $21
org $D1355E 
db $60, $33
org $D13562 
db $20, $1D
org $D13566 
db $40, $F2
org $D1356A 
db $60, $85
org $D1356E 
db $40, $5C
org $D13572 
db $50, $02
org $D13576 
db $40, $D0
org $D1357A 
db $50, $0E
org $D1357E 
db $60, $18
org $D13582 
db $40, $E4
org $D13586 
db $20, $2A
org $D1358A 
db $40, $E4
org $D1358E 
db $40, $E4
org $D13592 
db $40, $88
org $D13596 
db $20, $1E
org $D1359A 
db $20, $83
org $D1359E 
db $60, $52
org $D135A2 
db $60, $12
org $D135A6 
db $20, $28
org $D135AA 
db $20, $5A
org $D135AE 
db $40, $14
org $D135B2 
db $40, $E3
org $D135B6 
db $20, $4E
org $D135BA 
db $40, $E3
org $D135BE 
db $20, $19
org $D135C2 
db $20, $0C
org $D135C6 
db $20, $8F
org $D135CA 
db $20, $37
org $D135CE 
db $60, $43
org $D135D2 
db $60, $68
org $D135D6 
db $60, $7E
org $D135DA 
db $60, $5A
org $D135DE 
db $40, $60
org $D135E2 
db $60, $4C
org $D135E6 
db $20, $11
org $D135EA 
db $60, $10
org $D135EE 
db $40, $5B
org $D135F2 
db $40, $5B
org $D135F6 
db $20, $8B
org $D135FA 
db $40, $AC
org $D135FE 
db $40, $86
org $C0FB70 
db $20, $27
org $C0FB72 
db $40, $BF
org $C0FB74 
db $30, $1A
org $C0FB76 
db $60, $69
org $C0FB78 
db $60, $19
org $C0FB7A 
db $30, $08
org $C0FB7C 
db $30, $0B
org $C0FB7E 
db $30, $00
org $C0FB80 
db $30, $18
org $C0FB82 
db $20, $54
org $C0FB84 
db $30, $1D
org $C0FB86 
db $20, $85
org $C0FB88 
db $40, $3A
org $C0FB8A 
db $40, $1D
org $C0FB8C 
db $30, $04
org $C0FBB6 
db $30, $06
org $C0FBB8 
db $60, $61
org $C0FBBA 
db $30, $0E
org $C0FB8E 
db $30, $16
org $C0FB90 
db $30, $07
org $C0FB92 
db $30, $01
org $C0FB94 
db $30, $05
org $C0FB96 
db $30, $02
org $C0FB98 
db $30, $0D
org $C0FB9A 
db $20, $34
org $C0FB9C 
db $30, $1C
org $C0FB9E 
db $20, $86
org $C0FBA0 
db $20, $4A
org $C0FBA2 
db $60, $1A
org $C0FBA4 
db $30, $1B
org $C0FBA6 
db $20, $82
org $C0FBA8 
db $30, $03
org $C0FBAA 
db $30, $12
org $C0FBAC 
db $20, $87
org $C0FBAE 
db $30, $0C
org $C0FBB0 
db $60, $20
org $C0FBB2 
db $30, $15
org $C0FBB4 
db $20, $09
;=====
;shops
;=====
org $D12D40
db $01, $95, $96, $B4, $E1, $E3, $E5, $E8, $E9
org $D12D49
db $00, $02, $0B, $00, $00, $00, $00, $00, $00
org $D12D52
db $07, $06, $6D, $00, $00, $00, $00, $00, $00
org $D12D5B
db $07, $28, $39, $44, $7A, $00, $00, $00, $00
org $D12D64
db $01, $0D, $CC, $E4, $E8, $E9, $EC, $00, $00
org $D12D6D
db $01, $1F, $30, $3C, $BB, $E5, $E6, $FC, $FE
org $D12D76
db $07, $9C, $20, $58, $71, $00, $00, $00, $00
org $D12D7F
db $01, $55, $64, $81, $83, $90, $A1, $C6, $F3
org $D12D88
db $07, $08, $15, $42, $00, $00, $00, $00, $00
org $D12D91
db $07, $35, $5A, $6C, $80, $00, $00, $00, $00
org $D12D9A
db $07, $8D, $18, $19, $75, $00, $00, $00, $00
org $D12DA3
db $01, $0B, $24, $4B, $62, $9A, $A3, $B6, $CE
org $D12DAC
db $07, $0D, $11, $31, $00, $00, $00, $00, $00
org $D12DB5
db $00, $17, $26, $3C, $48, $95, $00, $00, $00
org $D12DBE
db $01, $0F, $67, $88, $89, $8A, $A6, $E6, $F0
org $D12DC7
db $00, $24, $2F, $8C, $93, $99, $00, $00, $00
org $D12DD0
db $01, $09, $4C, $69, $8C, $C5, $E0, $E3, $00
org $D12DD9
db $07, $8F, $9A, $13, $7E, $00, $00, $00, $00
org $D12DE2
db $00, $01, $16, $2C, $38, $00, $00, $00, $00
org $D12DEB
db $07, $0A, $82, $00, $00, $00, $00, $00, $00
org $D12DFD
db $01, $38, $A7, $E2, $E4, $ED, $FD, $00, $00
org $D12E18
db $07, $9D, $51, $61, $87, $00, $00, $00, $00
org $D12E21
db $07, $09, $0E, $38, $00, $00, $00, $00, $00
org $D12E2A
db $00, $1A, $28, $39, $4A, $5E, $00, $00, $00
org $D12E33
db $07, $2A, $30, $74, $76, $00, $00, $00, $00
org $D12E3C
db $07, $1A, $73, $00, $00, $00, $00, $00, $00
org $D12E45
db $00, $15, $00, $00, $00, $00, $00, $00, $00
org $D12E4E
db $00, $2B, $40, $41, $8E, $9D, $00, $00, $00
org $D12E57
db $01, $22, $5C, $66, $91, $CF, $E0, $F0, $F9
org $D12E60
db $00, $04, $08, $2D, $4B, $9B, $00, $00, $00
org $D12E69
db $01, $03, $0E, $47, $48, $49, $5A, $65, $F1
org $D12E72
db $00, $13, $22, $44, $84, $89, $00, $00, $00
org $D12E7B
db $00, $03, $07, $3A, $59, $83, $00, $00, $00
org $D12E84
db $07, $8A, $45, $83, $00, $00, $00, $00, $00
org $D12E8D
db $07, $8B, $14, $22, $00, $00, $00, $00, $00
org $D12E96
db $01, $60, $A5, $C3, $F1, $F2, $00, $00, $00
org $D12E9F
db $01, $82, $84, $EC, $F1, $F4, $00, $00, $00
org $D12EA8
db $01, $44, $50, $B3, $C0, $E2, $F6, $00, $00
org $D12EB1
db $00, $18, $21, $27, $4C, $58, $00, $00, $00
org $D12EBA
db $07, $8C, $0B, $00, $00, $00, $00, $00, $00
org $D12EC3
db $01, $02, $20, $21, $33, $5B, $97, $9D, $E5
org $D12ECC
db $07, $32, $40, $72, $85, $00, $00, $00, $00
org $D12ED5
db $01, $29, $57, $8B, $B1, $E1, $FA, $00, $00
org $D12EDE
db $07, $90, $97, $33, $77, $00, $00, $00, $00
org $D12EF9
db $00, $12, $25, $8A, $8F, $92, $00, $00, $00
org $D12F0B
db $00, $34, $52, $86, $87, $00, $00, $00, $00
org $D12F14
db $01, $36, $5D, $8E, $99, $9E, $A0, $FB, $00
org $D12F26
db $00, $09, $23, $31, $42, $82, $00, $00, $00
org $D12F2F
db $01, $08, $1E, $2D, $86, $93, $A9, $AA, $C4
org $D12F38
db $00, $1E, $2E, $30, $32, $4E, $00, $00, $00
org $D12F41
db $00, $11, $1F, $20, $43, $5B, $00, $00, $00
org $D12F4A
db $01, $07, $1A, $52, $98, $A4, $ED, $00, $00
org $D12F53
db $00, $3F, $47, $51, $53, $88, $00, $00, $00
org $D12F5C
db $00, $0A, $0F, $55, $5D, $9A, $00, $00, $00
org $D12F65
db $01, $06, $0C, $13, $17, $35, $3A, $43, $6C

;===========
;shop prices
;===========
org $D12A00
db $1, $00
org $D12A02
db $1, $00
org $D12A04
db $1, $0F
org $D12A06
db $1, $1E
org $D12A08
db $1, $2D
org $D12A0A
db $1, $3C
org $D12A0C
db $1, $5A
org $D12A0E
db $2, $1A
org $D12A10
db $2, $33
org $D12A12
db $2, $22
org $D12A14
db $2, $44
org $D12A16
db $4, $02
org $D12A18
db $4, $02
org $D12A1A
db $1, $1C
org $D12A1C
db $1, $30
org $D12A1E
db $1, $58
org $D12A20
db $2, $1C
org $D12A22
db $2, $2A
org $D12A24
db $2, $54
org $D12A26
db $2, $38
org $D12A28
db $2, $6E
org $D12A2A
db $4, $02
org $D12A2C
db $4, $03
org $D12A2E
db $1, $4B
org $D12A30
db $1, $0A
org $D12A32
db $1, $4F
org $D12A34
db $2, $1B
org $D12A36
db $2, $36
org $D12A38
db $2, $66
org $D12A3A
db $2, $51
org $D12A3C
db $2, $6C
org $D12A3E
db $4, $02
org $D12A40
db $4, $03
org $D12A42
db $1, $41
org $D12A44
db $1, $69
org $D12A46
db $2, $20
org $D12A48
db $2, $40
org $D12A4A
db $2, $60
org $D12A4C
db $2, $80
org $D12A4E
db $4, $02
org $D12A50
db $4, $03
org $D12A52
db $2, $3A
org $D12A54
db $1, $32
org $D12A56
db $2, $76
org $D12A58
db $2, $58
org $D12A5A
db $2, $94
org $D12A5C
db $4, $02
org $D12A5E
db $4, $02
org $D12A60
db $4, $03
org $D12A62
db $1, $14
org $D12A64
db $1, $4B
org $D12A66
db $1, $4B
org $D12A68
db $1, $4B
org $D12A6A
db $2, $0F
org $D12A6C
db $2, $1E
org $D12A6E
db $4, $02
org $D12A70
db $1, $14
org $D12A72
db $1, $32
org $D12A74
db $2, $12
org $D12A76
db $2, $09
org $D12A78
db $2, $1B
org $D12A7A
db $4, $02
org $D12A7C
db $4, $03
org $D12A7E
db $2, $19
org $D12A80
db $2, $19
org $D12A82
db $2, $19
org $D12A84
db $2, $26
org $D12A86
db $2, $32
org $D12A88
db $2, $4B
org $D12A8A
db $4, $02
org $D12A8C
db $4, $03
org $D12A8E
db $2, $08
org $D12A90
db $2, $10
org $D12A92
db $2, $20
org $D12A94
db $4, $02
org $D12A96
db $2, $0B
org $D12A98
db $2, $21
org $D12A9A
db $2, $16
org $D12A9C
db $4, $02
org $D12A9E
db $2, $2C
org $D12AA0
db $1, $32
org $D12AA2
db $3, $09
org $D12AA4
db $4, $02
org $D12AA6
db $2, $0F
org $D12AA8
db $1, $0A
org $D12AAA
db $3, $10
org $D12AAC
db $3, $13
org $D12AAE
db $2, $64
org $D12AB0
db $2, $6E
org $D12AB2
db $1, $6E
org $D12AB4
db $1, $4B
org $D12AB6
db $2, $7D
org $D12AB8
db $43, $0A
org $D12ABA
db $3, $0F
org $D12ABC
db $1, $4E
org $D12ABE
db $2, $4E
org $D12AC0
db $4, $01
org $D12AC2
db $4, $03
org $D12AC4
db $1, $0A
org $D12AC6
db $3, $19
org $D12AC8
db $2, $6E
org $D12ACA
db $2, $0F
org $D12ACC
db $2, $55
org $D12ACE
db $3, $0A
org $D12AD0
db $4, $02
org $D12AD2
db $2, $3B
org $D12AD4
db $4, $04
org $D12AD6
db $3, $19
org $D12AD8
db $2, $44
org $D12ADA
db $2, $3A
org $D12ADC
db $4, $02
org $D12ADE
db $1, $0A
org $D12AE0
db $1, $0A
org $D12AE2
db $1, $0A
org $D12AE4
db $1, $0A
org $D12AE6
db $1, $0A
org $D12AE8
db $1, $0A
org $D12AEA
db $1, $0A
org $D12AEC
db $1, $0A
org $D12AEE
db $1, $0A
org $D12AF0
db $1, $0A
org $D12AF2
db $1, $0A
org $D12AF4
db $1, $0A
org $D12AF6
db $1, $0A
org $D12AF8
db $1, $0A
org $D12AFA
db $1, $0A
org $D12AFC
db $1, $0A
org $D12AFE
db $1, $0A
org $D12B00
db $1, $0A
org $D12B02
db $1, $09
org $D12B04
db $1, $1D
org $D12B06
db $1, $27
org $D12B08
db $1, $3B
org $D12B0A
db $2, $1E
org $D12B0C
db $2, $2D
org $D12B0E
db $2, $3C
org $D12B10
db $2, $5A
org $D12B12
db $1, $05
org $D12B14
db $1, $19
org $D12B16
db $1, $23
org $D12B18
db $1, $37
org $D12B1A
db $2, $23
org $D12B1C
db $2, $46
org $D12B1E
db $2, $69
org $D12B20
db $1, $23
org $D12B22
db $2, $0F
org $D12B24
db $2, $1E
org $D12B26
db $2, $2D
org $D12B28
db $4, $03
org $D12B2A
db $3, $23
org $D12B2C
db $2, $23
org $D12B2E
db $2, $19
org $D12B30
db $2, $41
org $D12B32
db $2, $19
org $D12B34
db $1, $08
org $D12B36
db $1, $28
org $D12B38
db $1, $32
org $D12B3A
db $1, $46
org $D12B3C
db $2, $28
org $D12B3E
db $2, $50
org $D12B40
db $3, $0C
org $D12B42
db $1, $23
org $D12B44
db $1, $2D
org $D12B46
db $1, $3C
org $D12B48
db $2, $1E
org $D12B4A
db $2, $3C
org $D12B4C
db $2, $5A
org $D12B4E
db $1, $1E
org $D12B50
db $1, $32
org $D12B52
db $2, $14
org $D12B54
db $2, $0A
org $D12B56
db $2, $28
org $D12B58
db $3, $08
org $D12B5A
db $3, $08
org $D12B5C
db $3, $0A
org $D12B5E
db $4, $03
org $D12B60
db $3, $03
org $D12B62
db $3, $05
org $D12B64
db $2, $28
org $D12B66
db $3, $05
org $D12B68
db $1, $19
org $D12B6A
db $4, $05
org $D12B6C
db $1, $3C
org $D12B6E
db $1, $32
org $D12B70
db $2, $28
org $D12B72
db $2, $2D
org $D12B74
db $2, $19
org $D12B76
db $2, $1E
org $D12B78
db $4, $05
org $D12B7A
db $4, $05
org $D12B7C
db $4, $05
org $D12B7E
db $4, $03
org $D12B80
db $1, $07
org $D12B82
db $3, $0F
org $D12B84
db $2, $1E
org $D12B86
db $2, $32
org $D12B88
db $4, $04
org $D12B8A
db $4, $01
org $D12B8C
db $3, $14
org $D12B8E
db $3, $19
org $D12B90
db $3, $1E
org $D12B92
db $3, $0F
org $D12B94
db $4, $02
org $D12B96
db $3, $0C
org $D12B98
db $4, $02
org $D12B9A
db $4, $04
org $D12B9C
db $4, $01
org $D12B9E
db $2, $3A
org $D12BA0
db $2, $62
org $D12BA2
db $1, $0A
org $D12BA4
db $1, $0A
org $D12BA6
db $1, $0A
org $D12BA8
db $1, $0A
org $D12BAA
db $1, $0A
org $D12BAC
db $1, $0A
org $D12BAE
db $1, $0A
org $D12BB0
db $1, $0A
org $D12BB2
db $1, $0A
org $D12BB4
db $1, $0A
org $D12BB6
db $1, $0A
org $D12BB8
db $1, $0A
org $D12BBA
db $1, $0A
org $D12BBC
db $1, $0A
org $D12BBE
db $1, $0A
org $D12BC0
db $1, $04
org $D12BC2
db $1, $24
org $D12BC4
db $2, $0F
org $D12BC6
db $4, $02
org $D12BC8
db $3, $01
org $D12BCA
db $1, $06
org $D12BCC
db $1, $0F
org $D12BCE
db $1, $0F
org $D12BD0
db $1, $03
org $D12BD2
db $1, $02
org $D12BD4
db $3, $05
org $D12BD6
db $4, $03
org $D12BD8
db $1, $0F
org $D12BDA
db $1, $05
org $D12BDC
db $81, $00
org $D12BDE
db $4, $01
org $D12BE0
db $1, $19
org $D12BE2
db $1, $3C
org $D12BE4
db $1, $0B
org $D12BE6
db $1, $0B
org $D12BE8
db $1, $0B
org $D12BEA
db $1, $0B
org $D12BEC
db $1, $0B
org $D12BEE
db $83, $20
org $D12BF0
db $83, $20
org $D12BF2
db $83, $07
org $D12BF4
db $83, $09
org $D12BF6
db $83, $0E
org $D12BF8
db $2, $02
org $D12BFA
db $2, $02
org $D12BFC
db $2, $02
org $D12BFE
db $81, $00
org $F80000
db $1, $0F
org $F80002
db $1, $0F
org $F80004
db $1, $0F
org $F80006
db $1, $1D
org $F80008
db $1, $1C
org $F8000A
db $2, $03
org $F8000C
db $2, $06
org $F8000E
db $2, $06
org $F80010
db $2, $06
org $F80012
db $2, $19
org $F80014
db $2, $19
org $F80016
db $2, $19
org $F80018
db $2, $23
org $F8001A
db $2, $23
org $F8001C
db $2, $23
org $F8001E
db $3, $05
org $F80020
db $3, $05
org $F80022
db $2, $19
org $F80024
db $1, $12
org $F80026
db $1, $09
org $F80028
db $1, $09
org $F8002A
db $1, $1C
org $F8002C
db $1, $1C
org $F8002E
db $2, $03
org $F80030
db $2, $06
org $F80032
db $2, $06
org $F80034
db $2, $06
org $F80036
db $2, $19
org $F80038
db $2, $19
org $F8003A
db $2, $19
org $F8003C
db $3, $04
org $F8003E
db $3, $04
org $F80040
db $3, $04
org $F80042
db $2, $4B
org $F80044
db $4, $01
org $F80046
db $3, $05
org $F80048
db $1, $0F
org $F8004A
db $1, $0F
org $F8004C
db $1, $0F
org $F8004E
db $1, $1D
org $F80050
db $2, $03
org $F80052
db $2, $03
org $F80054
db $2, $06
org $F80056
db $2, $06
org $F80058
db $2, $06
org $F8005A
db $3, $02
org $F8005C
db $3, $02
org $F8005E
db $3, $03
org $F80060
db $2, $2D
org $F80062
db $2, $2D
org $F80064
db $2, $2D
org $F80066
db $4, $01
org $F80068
db $2, $4B
org $F8006A
db $2, $19
org $F8006C
db $1, $03
org $F8006E
db $1, $08
org $F80070
db $2, $01
org $F80072
db $2, $03
org $F80074
db $2, $03
org $F80076
db $2, $03
org $F80078
db $2, $06
org $F8007A
db $2, $06
org $F8007C
db $2, $06
org $F8007E
db $3, $03
org $F80080
db $3, $03
org $F80082
db $2, $05
org $F80084
db $2, $2D
org $F80086
db $3, $06
org $F80088
db $3, $03
org $F8008A
db $4, $01
org $F8008C
db $4, $01
org $F8008E
db $3, $05
org $F80090
db $1, $19
org $F80092
db $1, $19
org $F80094
db $1, $19
org $F80096
db $2, $0F
org $F80098
db $2, $0F
org $F8009A
db $2, $0F
org $F8009C
db $3, $08
org $F8009E
db $3, $0F
org $F800A0
db $3, $08
org $F800A2
db $4, $01
org $F800A4
db $3, $0C
org $F800A6
db $3, $0C
org $F800A8
db $3, $0C
org $F800AA
db $3, $0F
org $F800AC
db $3, $0F
org $F800AE
db $3, $02
org $F800B0
db $3, $02
org $F800B2
db $3, $02
org $F800B4
db $3, $02
org $F800B6
db $3, $05
org $F800B8
db $3, $02
org $F800BA
db $3, $01
org $F800BC
db $3, $01
org $F800BE
db $1, $00
org $F800C0
db $1, $00
org $F800C2
db $1, $00
org $F800C4
db $1, $00
org $F800C6
db $1, $00
org $F800C8
db $1, $00
org $F800CA
db $1, $00
org $F800CC
db $1, $00
org $F800CE
db $1, $00
org $F800D0
db $1, $00
org $F800D2
db $1, $00
org $F800D4
db $1, $00
org $F800D6
db $1, $00
org $F800D8
db $1, $00
org $F800DA
db $1, $00
org $F800DC
db $1, $00
org $F800DE
db $1, $00
org $F800E0
db $1, $00
org $F800E2
db $1, $00
org $F800E4
db $1, $00
org $F800E6
db $1, $00
org $F800E8
db $1, $00
org $F800EA
db $1, $00
org $F800EC
db $1, $00
org $F800EE
db $1, $00
org $F800F0
db $1, $00
org $F800F2
db $1, $00
org $F800F4
db $1, $00
org $F800F6
db $1, $00
org $F800F8
db $1, $00
org $F800FA
db $1, $00
org $F800FC
db $1, $00
org $F800FE
db $1, $00
org $F80100
db $1, $00
org $F80102
db $1, $00
org $F80104
db $3, $01
org $F80106
db $3, $01
org $F80108
db $3, $05
org $F8010A
db $3, $08
org $F8010C
db $3, $05
org $F8010E
db $3, $05
org $F80110
db $3, $05
org $F80112
db $3, $01
org $F80114
db $3, $01
org $F80116
db $3, $01
org $F80118
db $3, $01
org $F8011A
db $3, $01
org $F8011C
db $3, $05
org $F8011E
db $1, $0F
org $F80120
db $2, $06
org $F80122
db $3, $04
org $F80124
db $1, $4B
org $F80126
db $2, $03
org $F80128
db $2, $19
org $F8012A
db $3, $01
org $F8012C
db $3, $01
org $F8012E
db $3, $05
org $F80130
db $2, $05
org $F80132
db $2, $05
org $F80134
db $4, $01
org $F80136
db $3, $03
org $F80138
db $3, $01
org $F8013A
db $4, $01
org $F8013C
db $3, $08
org $F8013E
db $3, $02
org $F80140
db $1, $00
org $F80142
db $1, $00
org $F80144
db $1, $00
org $F80146
db $1, $00
org $F80148
db $1, $00
org $F8014A
db $1, $00
org $F8014C
db $1, $00
org $F8014E
db $1, $00
org $F80150
db $1, $00
org $F80152
db $1, $00
org $F80154
db $1, $00
org $F80156
db $1, $00
org $F80158
db $1, $00
org $F8015A
db $1, $00
org $F8015C
db $1, $00
org $F8015E
db $1, $00
org $F80160
db $1, $00
org $F80162
db $1, $00
org $F80164
db $1, $00
org $F80166
db $1, $00
org $F80168
db $1, $00
org $F8016A
db $1, $00
org $F8016C
db $1, $00
org $F8016E
db $1, $00
org $F80170
db $1, $00
org $F80172
db $1, $00
org $F80174
db $1, $00
org $F80176
db $1, $00
org $F80178
db $1, $00
org $F8017A
db $1, $00
org $F8017C
db $1, $00
org $F8017E
db $1, $00
org $F80180
db $1, $00
org $F80182
db $1, $00
org $F80184
db $1, $00
org $F80186
db $1, $00
org $F80188
db $1, $00
org $F8018A
db $1, $00
org $F8018C
db $1, $00
org $F8018E
db $1, $00
org $F80190
db $1, $00
org $F80192
db $1, $00
org $F80194
db $1, $00
org $F80196
db $1, $00
org $F80198
db $1, $00
org $F8019A
db $1, $00
org $F8019C
db $1, $00
org $F8019E
db $1, $00
org $F801A0
db $1, $00
org $F801A2
db $1, $00
org $F801A4
db $1, $00
org $F801A6
db $1, $00
org $F801A8
db $1, $00
org $F801AA
db $1, $00
org $F801AC
db $1, $00
org $F801AE
db $1, $00
org $F801B0
db $1, $00
org $F801B2
db $1, $00
org $F801B4
db $1, $00
org $F801B6
db $1, $00
org $F801B8
db $1, $00
org $F801BA
db $1, $00
org $F801BC
db $1, $00
org $F801BE
db $1, $00
org $F801C0
db $1, $00
org $F801C2
db $1, $00
org $F801C4
db $1, $00
org $F801C6
db $1, $00
org $F801C8
db $1, $00
org $F801CA
db $1, $00
org $F801CC
db $1, $00
org $F801CE
db $1, $00
org $F801D0
db $1, $00
org $F801D2
db $1, $00
org $F801D4
db $1, $00
org $F801D6
db $1, $00
org $F801D8
db $1, $00
org $F801DA
db $1, $00
org $F801DC
db $1, $00
org $F801DE
db $1, $00
org $F801E0
db $1, $00
org $F801E2
db $1, $00
org $F801E4
db $1, $00
org $F801E6
db $1, $00
org $F801E8
db $1, $00
org $F801EA
db $1, $00
org $F801EC
db $1, $00
org $F801EE
db $1, $00
org $F801F0
db $1, $00
org $F801F2
db $1, $00
org $F801F4
db $1, $00
org $F801F6
db $1, $00
org $F801F8
db $1, $00
org $F801FA
db $1, $00
org $F801FC
db $1, $00
org $F801FE
db $1, $00
org $F80200
db $4, $05
org $F80202
db $4, $05
org $F80204
db $4, $05
org $F80206
db $4, $05
org $F80208
db $4, $05
org $F8020A
db $4, $05
org $F8020C
db $2, $03
org $F8020E
db $3, $01
org $F80210
db $2, $0F
org $F80212
db $3, $01
org $F80214
db $2, $05
org $F80216
db $3, $01
org $F80218
db $3, $02
org $F8021A
db $3, $03
org $F8021C
db $2, $05
org $F8021E
db $2, $0F
org $F80220
db $3, $03
org $F80222
db $3, $01
org $F80224
db $3, $0F
org $F80226
db $3, $05
org $F80228
db $3, $02
org $F8022A
db $3, $01
org $F8022C
db $4, $02
org $F8022E
db $3, $03
org $F80230
db $2, $03
org $F80232
db $2, $07
org $F80234
db $3, $01
org $F80236
db $3, $03
org $F80238
db $3, $05
org $F8023A
db $4, $05
org $F8023C
db $4, $01
org $F8023E
db $3, $02
org $F80240
db $3, $03
org $F80242
db $3, $05
org $F80244
db $3, $02
org $F80246
db $2, $01
org $F80248
db $3, $01
org $F8024A
db $3, $01
org $F8024C
db $3, $01
org $F8024E
db $3, $05
org $F80250
db $3, $01
org $F80252
db $3, $05
org $F80254
db $4, $01
org $F80256
db $2, $01
org $F80258
db $2, $01
org $F8025A
db $2, $01
org $F8025C
db $2, $01
org $F8025E
db $2, $01
org $F80260
db $2, $05
org $F80262
db $3, $01
org $F80264
db $3, $02
org $F80266
db $3, $03
org $F80268
db $3, $05
org $F8026A
db $3, $08
org $F8026C
db $2, $01
org $F8026E
db $2, $01
org $F80270
db $2, $05
org $F80272
db $3, $01
org $F80274
db $3, $02
org $F80276
db $3, $03
org $F80278
db $3, $05
org $F8027A
db $3, $08
org $F8027C
db $2, $01
org $F8027E
db $2, $01
org $F80280
db $2, $05
org $F80282
db $3, $01
org $F80284
db $3, $02
org $F80286
db $3, $03
org $F80288
db $3, $05
org $F8028A
db $3, $08
org $F8028C
db $2, $01
org $F8028E
db $2, $01
org $F80290
db $2, $05
org $F80292
db $3, $01
org $F80294
db $3, $02
org $F80296
db $3, $03
org $F80298
db $3, $05
org $F8029A
db $3, $08
org $F8029C
db $2, $01
org $F8029E
db $2, $01
org $F802A0
db $3, $02
org $F802A2
db $3, $04
org $F802A4
db $3, $06
org $F802A6
db $3, $08
org $F802A8
db $3, $0C
org $F802AA
db $2, $01
org $F802AC
db $2, $01
org $F802AE
db $2, $01
org $F802B0
db $2, $05
org $F802B2
db $3, $01
org $F802B4
db $3, $02
org $F802B6
db $2, $01
org $F802B8
db $2, $01
org $F802BA
db $2, $01
org $F802BC
db $2, $01
org $F802BE
db $2, $01
org $F802C0
db $4, $02
org $F802C2
db $3, $0F
org $F802C4
db $2, $01
org $F802C6
db $2, $01
org $F802C8
db $2, $01
org $F802CA
db $2, $01
org $F802CC
db $2, $01
org $F802CE
db $2, $01
org $F802D0
db $3, $02
org $F802D2
db $3, $03
org $F802D4
db $3, $05
org $F802D6
db $3, $02
org $F802D8
db $3, $02
org $F802DA
db $3, $02
org $F802DC
db $3, $02
org $F802DE
db $3, $02
org $F802E0
db $3, $02
org $F802E2
db $3, $02
org $F802E4
db $2, $19
org $F802E6
db $3, $01
org $F802E8
db $3, $02
org $F802EA
db $3, $03
org $F802EC
db $3, $01
org $F802EE
db $3, $03
org $F802F0
db $3, $03
org $F802F2
db $3, $05
org $F802F4
db $3, $05
org $F802F6
db $3, $01
org $F802F8
db $3, $01
org $F802FA
db $2, $19
org $F802FC
db $3, $01
org $F802FE
db $2, $01
org $F80300
db $3, $01
org $F80302
db $3, $01
org $F80304
db $3, $01
org $F80306
db $3, $01
org $F80308
db $3, $01
org $F8030A
db $3, $01
org $F8030C
db $3, $01
org $F8030E
db $3, $02
org $F80310
db $3, $01
org $F80312
db $4, $01
org $F80314
db $3, $08
org $F80316
db $3, $08
org $F80318
db $4, $01
org $F8031A
db $4, $01
org $F8031C
db $4, $02
org $F8031E
db $3, $08
org $F80320
db $4, $01
org $F80322
db $3, $0C
org $F80324
db $4, $01
org $F80326
db $4, $01
org $F80328
db $4, $01
org $F8032A
db $3, $0C
org $F8032C
db $4, $01
org $F8032E
db $3, $08
org $F80330
db $3, $08
org $F80332
db $3, $0C
org $F80334
db $3, $08
org $F80336
db $4, $01
org $F80338
db $4, $01
org $F8033A
db $4, $02
org $F8033C
db $4, $02
org $F8033E
db $1, $00
org $F80340
db $1, $00
org $F80342
db $1, $00
org $F80344
db $1, $00
org $F80346
db $1, $00
org $F80348
db $1, $00
org $F8034A
db $1, $00
org $F8034C
db $1, $00
org $F8034E
db $1, $00
org $F80350
db $1, $00
org $F80352
db $1, $00
org $F80354
db $1, $00
org $F80356
db $1, $00
org $F80358
db $1, $00
org $F8035A
db $1, $00
org $F8035C
db $1, $00
org $F8035E
db $1, $00
org $F80360
db $1, $00
org $F80362
db $1, $00
org $F80364
db $1, $00
org $F80366
db $1, $00
org $F80368
db $1, $00
org $F8036A
db $1, $00
org $F8036C
db $1, $00
org $F8036E
db $1, $00
org $F80370
db $1, $00
org $F80372
db $1, $00
org $F80374
db $1, $00
org $F80376
db $1, $00
org $F80378
db $1, $00
org $F8037A
db $1, $00
org $F8037C
db $1, $00
org $F8037E
db $1, $00
org $F80380
db $1, $00
org $F80382
db $1, $00
org $F80384
db $1, $00
org $F80386
db $1, $00
org $F80388
db $1, $00
org $F8038A
db $1, $00
org $F8038C
db $1, $00
org $F8038E
db $1, $00
org $F80390
db $1, $00
org $F80392
db $1, $00
org $F80394
db $1, $00
org $F80396
db $1, $00
org $F80398
db $1, $00
org $F8039A
db $1, $00
org $F8039C
db $1, $00
org $F8039E
db $1, $00
org $F803A0
db $1, $00
org $F803A2
db $1, $00
org $F803A4
db $1, $00
org $F803A6
db $1, $00
org $F803A8
db $1, $00
org $F803AA
db $1, $00
org $F803AC
db $1, $00
org $F803AE
db $1, $00
org $F803B0
db $1, $00
org $F803B2
db $1, $00
org $F803B4
db $1, $00
org $F803B6
db $1, $00
org $F803B8
db $1, $00
org $F803BA
db $1, $00
org $F803BC
db $1, $00
org $F803BE
db $1, $00
org $F803C0
db $1, $00
org $F803C2
db $1, $00
org $F803C4
db $1, $00
org $F803C6
db $1, $00
org $F803C8
db $1, $00
org $F803CA
db $1, $00
org $F803CC
db $1, $00
org $F803CE
db $1, $00
org $F803D0
db $1, $00
org $F803D2
db $1, $00
org $F803D4
db $1, $00
org $F803D6
db $1, $00
org $F803D8
db $1, $00
org $F803DA
db $1, $00
org $F803DC
db $1, $00
org $F803DE
db $1, $00
org $F803E0
db $1, $00
org $F803E2
db $1, $00
org $F803E4
db $1, $00
org $F803E6
db $1, $00
org $F803E8
db $1, $00
org $F803EA
db $1, $00
org $F803EC
db $1, $00
org $F803EE
db $1, $00
org $F803F0
db $1, $00
org $F803F2
db $1, $00
org $F803F4
db $1, $00
org $F803F6
db $1, $00
org $F803F8
db $1, $00
org $F803FA
db $1, $00
org $F803FC
db $1, $00
;  ########################### 
;  # New AI for enemy: Omega
;  ########################### 
; New AOE skill: SurgeBeam
org $D0B235
db $DD
; New AOE skill: Maelstrom
org $D0B238
db $C2
; New AOE skill: AquaRake
org $D0B23D
db $84
; New AOE skill: Quake
org $D0B245
db $D6
; New AOE skill: BreathWing
org $D0B248
db $DA
; New AOE skill: ZombieBreath
org $D0B24E
db $B9
; New single target skill: Jump
org $D0B236
db $E8
; New single target skill: Fight
org $D0B237
db $80
; New single target skill: Quarter
org $D0B23A
db $42
; New single target skill: Comet
org $D0B23B
db $3F
; New single target skill: Hug
org $D0B23C
db $B4
; New single target skill: MustardBomb
org $D0B243
db $C7
; New single target skill: Blaster
org $D0B244
db $B2
; New single target skill: RainbowWind
org $D0B247
db $BD
; New single target skill: Missile
org $D0B249
db $9F
; New single target skill: Doom
org $D0B24C
db $34
; New single target skill: Aero3
org $D0B24D
db $91
; New single target skill: StomachAcid
org $D0B25B
db $C5
; New single target skill: Missile
org $D0B25C
db $9F
; New single target skill: Tailscrew
org $D0B25F
db $C4
; New single target skill: Doom
org $D0B260
db $34
; New status skill: Break
org $D0B25D
db $2E
; New status skill: DarkShock
org $D0B261
db $94
db $76, $7A, $8D, $7E, $8B, $01
db $60, $87, $7D, $96, $7F, $88, $8B, $96, $8C, $8D, $7A, $8D, $8E, $8C, $7E, $8C, $A3, $A3, $A3, $01
db $72, $85, $7E, $7E, $89, $01
db $00
;  ########################### 
;  # New AI for enemy: Shinryuu
;  ########################### 
; New AOE skill: Flame
org $D0C532
db $DB
; New AOE skill: TrueEdge
org $D0C533
db $D0
; New AOE skill: L5
org $D0C534
db $85
; New AOE skill: Maelstrom
org $D0C53F
db $C2
; New AOE skill: Maelstrom
org $D0C540
db $C2
; New AOE skill: Maelstrom
org $D0C55C
db $C2
; New AOE skill: TidalWave
org $D0C567
db $D1
; New single target skill: Bio
org $D0C52F
db $2F
; New single target skill: MustardBomb
org $D0C53B
db $C7
; New single target skill: ReaperSword
org $D0C546
db $B0
; New single target skill: Emission
org $D0C547
db $92
; New single target skill: DanceoftheDead
org $D0C54A
db $B7
; New single target skill: Emission
org $D0C54B
db $92
; New single target skill: Blaster
org $D0C52E
db $B2
; New status skill: FrogSong
org $D0C530
db $89
; New status skill: Mute
org $D0C53A
db $15
; New status skill: Haste
org $D0C53C
db $3A
; New status skill: Stop
org $D0C53E
db $3D
; New status skill: FrogSong
org $D0C548
db $89
; New status skill: Condemn
org $D0C54C
db $82
db $76, $82, $87, $7D, $01
db $60, $87, $7D, $96, $7F, $88, $8B, $96, $8C, $8D, $7A, $8D, $8E, $8C, $7E, $8C, $A3, $A3, $A3, $01
db $72, $85, $88, $90, $01
db $00

; CODE OF THE VOID: 
org $E77476
db $60, $74, $66, $76, $79, $72
org $F80900
db $60, $74, $66, $76, $79, $72



; PORTAL BOSS

; Formation changes
org $D04EB0
db $00, $80, $00, $80
org $D04EB4
db $65, $66, $67
org $D04EBE
db $28, $21
;AI table changes
org $D09ECA
db $E0, $F1
db $E0, $F2
db $E0, $F3
;Formation table changes
org $D07954
db $EB, $01
db $EB, $01
;AI Changes
; # Form 1
    org $D0F1E0
db $00, $00, $00, $00            
db $FE                           
db $FD, $F7, $03, $F0            
db $AB                           
db $90                           
db $90                           
db $94                           
db $FD, $BD, $9D, $9D            
db $FD, $F7, $02, $F0            
db $23                           
db $23                           
db $FD, $F3, $23, $F0            
db $15                           
db $FD, $F7, $09, $F0            
db $FD, $F3, $23, $F0            
db $91                           
db $EA                           
db $FD, $F3, $23, $F0            
db $80                           
db $FD, $F3, $23, $F0            
db $B5                           
db $FD, $BD, $9D, $9D            
db $FD, $F3, $23, $F0            
db $49                           
db $FD, $F3, $0D, $F0            
db $3A                           
db $FF                           

db $06, $00, $16, $00            
db $FE                           
db $FD, $F3, $2D, $00            
db $91                           
db $FE                           
db $07, $01, $2B, $00            
db $FE                           
db $FD, $BB, $AA, $AA            
db $FE                           

db $0F, $00, $00, $00, $FE, $FD, $F2, $82, $40, $EE, $FF
; # Form 2
    org $D0F2E0 
db $00, $00, $00, $00            
db $FE                           
db $FD, $40, $3D, $40            
db $FD, $F3, $23, $F0            
db $80                           
db $FD, $33, $33, $33            
db $FD, $F7, $0A, $F0            
db $FD, $F3, $23, $F0            
db $99                           
db $FD, $F3, $23, $F0            
db $C5                           
db $FD, $94, $94, $94            
db $FD, $BD, $9D, $9D            
db $FD, $F7, $02, $F0            
db $23                           
db $23                           
db $FD, $F7, $03, $F0            
db $2D                           
db $2D                           
db $2D                           
db $FD, $80, $80, $80            
db $FD, $B8, $B8, $B9            
db $FD, $F3, $23, $F0            
db $B5                           
db $FD, $33, $33, $33            
db $23                           
db $FD, $BD, $9D, $9D            
db $FD, $B2, $B2, $B2            
db $FD, $F3, $0D, $F0            
db $3A                           
db $FF                           
db $06, $00, $16, $00            
db $FE                           
db $FD, $F3, $2D, $00            
db $91                           
db $B0                           
db $FE                           
db $07, $00, $2B, $00            
db $FE                           
db $FD, $BB, $AA, $AA            
db $FE                           

db $0F, $00, $00, $00, $FE, $FD, $F2, $82, $20, $EE, $FF

; # Form 3
    org $D0F3E0
db $00, $00, $00, $00            
db $FE                           
db $FD, $F7, $02, $F0            
db $AB                           
db $AB                           
db $FD, $F7, $04, $F0            
db $23                           
db $23                           
db $23                           
db $23                           
db $94                           
db $FD, $F7, $06, $F0            
db $FD, $F3, $23, $F0            
db $91                           
db $EA                           
db $FD, $BD, $9D, $9D            
db $FD, $F3, $23, $F0            
db $80                           
db $FD, $B8, $B8, $B9            
db $FD, $F3, $23, $F0            
db $B5                           
db $FD, $BD, $9D, $9D            
db $FD, $F3, $23, $F0            
db $49                           
db $FD, $9E, $9E, $9E            
db $FD, $F7, $02, $F0            
db $EA                           
db $33                           
db $FD, $80, $80, $80            
db $FD, $37, $3D, $40            
db $FF                           
db $06, $00, $16, $00            
db $FE                           
db $FD, $F3, $2D, $00            
db $D7                           
db $FE                           

db $07, $01, $2B, $00            
db $FE                           
db $FD, $BB, $AA, $AA            
db $FE                           
db $07, $00, $2B, $00            
db $FE                           
db $FD, $BB, $AA, $AA            
db $FE                           

db $0F, $00, $00, $00            
db $FE                           
db $AA                           
db $FF                           


org $D0F1D4
db $B0, $4F
org $E74FB0
db $A3, $A3, $A3, $00
;Enemy X/Y Coords
org $d09858
db $78, $78, $78, $78, $78, $78, $78, $78
; Battle sprite changes
org $D4B879
db $31, $27, $01, $68, $51
db $31, $27, $01, $69, $51
db $31, $27, $01, $5f, $51
org $E00E42
db $72, $88, $86, $7B, $7E, $8B, $6C, $7A, $80, $7E
db $72, $88, $86, $7B, $7E, $8B, $6C, $7A, $80, $7E
db $72, $88, $86, $7B, $7E, $8B, $6C, $7A, $80, $7E
; Pre-battle dialogue
org $E14BF1
db $73, $81, $7E, $96, $90, $82, $87, $7D, $96, $82, $8C, $96, $7C, $7A, $85, $85, $82, $87, $80, $A3, $A3, $A3, $96, $82, $8D, $99, $8C, $01, $8D, $82, $86, $7E, $96, $7F, $88, $8B, $96, $8E, $8C, $96, $8D, $88, $96, $7F, $82, $80, $81, $8D, $A3, $00;=======
;enemies
;=======
; Enemy: Ramuh
; Stats: 
org $D004E0
db $23, $38, $07, $08, $0b, $2c, $04, $04, $E4, $0C, $98, $21, $E4, $0C, $00, $00, $34, $00, $64, $F4, $00, $04, $00, $00, $80, $18, $0, $0, $00, $0, $27, $15
; Loot: 
org $D0509C
db $E1, $E1, $00, $F9
; --------------------------
; Original boss Ramuh rank 31.0 -> Randomized boss Chim.Brain rank 16.0
; HP: 10000 -> 3300
; ENEMY: Ramuh
; Skills: ['Bolt2', 'ElectricShock', 'Bolt2', 'Flash', 'Bolt2', 'ElectricShock', 'Bolt2', 'Thunder', 'Psych']
; New skill: Bolt2
org $d0a1a2
db $2C
; New skill: ElectricShock
org $d0a1a3
db $CE
; New skill: Bolt2
org $d0a1a5
db $2C
; New skill: Flash
org $d0a1a6
db $8B
; New skill: Bolt2
org $d0a1aa
db $2C
; New skill: ElectricShock
org $d0a1ab
db $CE
; New skill: Bolt2
org $d0a1ad
db $2C
; New skill: Thunder
org $d0a1ae
db $DC
; New skill: Psych
org $d0a1af
db $35

; Enemy: Shoat
; Stats: 
org $D00E40
db $2a, $97, $0b, $00, $1a, $4e, $0a, $00, $8A, $4D, $F3, $3C, $8A, $4D, $00, $00, $00, $00, $FB, $FF, $EF, $00, $00, $00, $34, $18, $0, $0, $00, $0, $72, $26
; Loot: 
org $D051C8
db $E4, $00, $00, $FA
; --------------------------
; Original boss Shoat rank 32.0 -> Randomized boss Minotauros rank 39.0
; HP: 10000 -> 19850
; ENEMY: Shoat

; Enemy: Golem
; Stats: 
org $D00CE0
db $0c, $42, $0b, $00, $00, $00, $00, $00, $50, $46, $6F, $10, $50, $46, $00, $00, $00, $00, $F0, $00, $00, $00, $00, $00, $00, $18, $0, $0, $00, $0, $67, $03
; Loot: 
org $D0519C
db $EC, $EC, $00, $00
; --------------------------
; Original boss Golem, BoneDragon, ZombieDrgn, Golem rank 33.0 -> Randomized boss Calofisteri rank 43.0
; HP: 10000 -> 18000
; ENEMY: Golem

; Enemy: BoneDragon
; Stats: 
org $D01420
db $23, $6c, $0d, $1b, $3c, $00, $1b, $0b, $28, $23, $B6, $13, $00, $00, $00, $00, $00, $08, $34, $E0, $00, $08, $00, $01, $31, $0, $0, $0, $00, $0, $A1, $25
; Loot: 
org $D05284
db $00, $00, $00, $00
; --------------------------
; Original boss Golem, BoneDragon, ZombieDrgn, Golem rank 33.0 -> Randomized boss Calofisteri rank 43.0
; HP: 10000 -> 18000
; ENEMY: Golem
; ENEMY: BoneDragon

; Enemy: ZombieDrgn
; Stats: 
org $D014C0
db $23, $6c, $0d, $1b, $1e, $00, $1b, $0b, $28, $23, $48, $1A, $00, $00, $00, $00, $00, $08, $74, $60, $00, $08, $00, $01, $31, $0, $0, $0, $00, $0, $A6, $25
; Loot: 
org $D05298
db $00, $00, $00, $00
; --------------------------
; Original boss Golem, BoneDragon, ZombieDrgn, Golem rank 33.0 -> Randomized boss Calofisteri rank 43.0
; HP: 10000 -> 18000
; ENEMY: Golem
; ENEMY: BoneDragon
; ENEMY: ZombieDrgn

; Enemy: Golem
; Stats: 
org $D01CA0
db $4c, $55, $0d, $00, $aa, $00, $55, $00, $10, $27, $B5, $41, $00, $00, $00, $00, $00, $FF, $FF, $FF, $FF, $00, $00, $00, $20, $18, $0, $0, $00, $0, $E5, $47
; Loot: 
org $D05394
db $00, $EC, $00, $FB
; --------------------------
; Original boss Golem, BoneDragon, ZombieDrgn, Golem rank 33.0 -> Randomized boss Calofisteri rank 43.0
; HP: 10000 -> 18000
; ENEMY: Golem
; ENEMY: BoneDragon
; ENEMY: ZombieDrgn
; ENEMY: Golem

; Enemy: Byblos
; Stats: 
org $D00400
db $24, $38, $08, $14, $06, $23, $18, $0e, $88, $13, $F4, $03, $88, $13, $00, $00, $00, $00, $F8, $D4, $10, $FE, $00, $11, $04, $18, $0, $0, $00, $0, $20, $18
; Loot: 
org $D05080
db $EB, $ED, $00, $F5
; --------------------------
; Original boss Byblos rank 10.0 -> Randomized boss Tyrasaurus rank 21.0
; HP: 3600 -> 5000
; ENEMY: Byblos
; Skills: ['WindSlash', 'WindSlash']
; New skill: WindSlash
org $d0a0db
db $AB
; New skill: WindSlash
org $d0a0e1
db $AB

; Enemy: WingRaptor
; Stats: 
org $D02000
db $23, $48, $07, $06, $15, $01, $0a, $0a, $C4, $09, $1B, $00, $C4, $09, $00, $00, $00, $00, $70, $00, $00, $00, $40, $00, $20, $18, $88, $0, $00, $0, $00, $01
; Loot: 
org $D05400
db $00, $E0, $00, $E4
; --------------------------
; Original boss WingRaptor, WingRaptor rank 1.0 -> Randomized boss Abductor rank 22.0
; HP: 250 -> 2500
; ENEMY: WingRaptor

; Enemy: WingRaptor
; Stats: 
org $D02020
db $23, $48, $0b, $29, $31, $01, $0a, $0a, $C4, $09, $00, $00, $C4, $09, $00, $00, $00, $00, $70, $00, $00, $00, $40, $00, $20, $18, $88, $0, $00, $0, $01, $02
; Loot: 
org $D05404
db $00, $E0, $00, $E4
; --------------------------
; Original boss WingRaptor, WingRaptor rank 1.0 -> Randomized boss Abductor rank 22.0
; HP: 250 -> 2500
; ENEMY: WingRaptor
; ENEMY: WingRaptor

; Enemy: Karlabos
; Stats: 
org $D02040
db $1a, $1d, $03, $02, $02, $00, $08, $00, $B8, $0B, $38, $00, $B8, $0B, $00, $00, $00, $00, $FF, $FF, $00, $00, $00, $04, $20, $18, $0, $0, $00, $0, $02, $05
; Loot: 
org $D05408
db $00, $E0, $00, $F0
; --------------------------
; Original boss Karlabos rank 2.0 -> Randomized boss LiquiFlame, LiquiFlame, LiquiFlame rank 6.0
; HP: 650 -> 3000
; ENEMY: Karlabos

; Enemy: Siren
; Stats: 
org $D02080
db $21, $0c, $06, $00, $00, $0f, $20, $00, $40, $1F, $35, $02, $40, $1F, $00, $00, $00, $00, $30, $44, $00, $00, $00, $00, $A0, $18, $0, $0, $00, $0, $04, $02
; Loot: 
org $D05410
db $00, $00, $00, $9B
; --------------------------
; Original boss Siren, Siren rank 3.0 -> Randomized boss ArchaeAvis, ArchaeAvis, ArchaeAvis, ArchaeAvis, ArchaeAvis rank 15.0
; HP: 900 -> 8000
; ENEMY: Siren
; Skills: ['Mute', 'Slow', 'Haste', 'Cure2', 'Ice2', 'Scan', 'Armor', 'Sleep', 'Bolt2']
; New skill: Mute
org $d0b2e6
db $15
; New skill: Slow
org $d0b2e7
db $37
; New skill: Haste
org $d0b2e8
db $3A
; New skill: Cure2
org $d0b2ea
db $18
; New skill: Ice2
org $d0b2eb
db $2B
; New skill: Scan
org $d0b2ec
db $13
; New skill: Armor
org $d0b2ee
db $16
; New skill: Sleep
org $d0b2ef
db $28
; New skill: Bolt2
org $d0b2f0
db $2C

; Enemy: Siren
; Stats: 
org $D020A0
db $21, $3a, $08, $00, $18, $00, $00, $00, $40, $1F, $A6, $00, $40, $1F, $00, $00, $00, $00, $34, $FF, $10, $08, $00, $01, $A1, $18, $0, $0, $00, $0, $05, $02
; Loot: 
org $D05414
db $00, $00, $00, $82
; --------------------------
; Original boss Siren, Siren rank 3.0 -> Randomized boss ArchaeAvis, ArchaeAvis, ArchaeAvis, ArchaeAvis, ArchaeAvis rank 15.0
; HP: 900 -> 8000
; ENEMY: Siren
; Skills: ['Mute', 'Slow', 'Haste', 'Cure2', 'Ice2', 'Scan', 'Armor', 'Sleep', 'Bolt2']
; New skill: Mute
org $d0b2e6
db $15
; New skill: Slow
org $d0b2e7
db $37
; New skill: Haste
org $d0b2e8
db $3A
; New skill: Cure2
org $d0b2ea
db $18
; New skill: Ice2
org $d0b2eb
db $2B
; New skill: Scan
org $d0b2ec
db $13
; New skill: Armor
org $d0b2ee
db $16
; New skill: Sleep
org $d0b2ef
db $28
; New skill: Bolt2
org $d0b2f0
db $2C
; ENEMY: Siren

; Enemy: Forza
; Stats: 
org $D020C0
db $28, $85, $0b, $00, $13, $00, $07, $0a, $34, $21, $9A, $00, $34, $21, $00, $00, $00, $00, $F0, $00, $00, $00, $00, $00, $A0, $18, $0, $0, $00, $0, $06, $08
; Loot: 
org $D05418
db $00, $00, $00, $F3
; --------------------------
; Original boss Forza, Magisa rank 4.0 -> Randomized boss Omniscient rank 38.0
; HP: 850 -> 16999
; ENEMY: Forza

; Enemy: Magisa
; Stats: 
org $D020E0
db $21, $85, $07, $0a, $00, $3b, $23, $0a, $34, $21, $DB, $04, $34, $21, $00, $00, $00, $00, $F0, $FB, $00, $00, $00, $00, $80, $18, $0, $0, $00, $0, $07, $08
; Loot: 
org $D0541C
db $00, $00, $00, $4B
; --------------------------
; Original boss Forza, Magisa rank 4.0 -> Randomized boss Omniscient rank 38.0
; HP: 850 -> 16999
; ENEMY: Forza
; ENEMY: Magisa
; Skills: ['Fire2', 'Ice2', 'Bolt2', 'Aero3', 'Specialty', 'Drain']
; New skill: Fire2
org $d0b34d
db $2A
; New skill: Ice2
org $d0b34e
db $2B
; New skill: Bolt2
org $d0b34f
db $2C
; New skill: Aero3
org $d0b351
db $91
; New skill: Specialty
org $d0b352
db $81
; New skill: Drain
org $d0b353
db $2D
; Original HP: 8500
; New trigger HP: 3910
org $d0b329
db $46, $0f

; Enemy: Galura
; Stats: 
org $D02100
db $26, $a9, $0c, $00, $0b, $00, $06, $00, $62, $BA, $A3, $00, $62, $BA, $00, $00, $00, $00, $10, $40, $00, $00, $00, $00, $04, $18, $0, $0, $00, $0, $08, $03
; Loot: 
org $D05420
db $E1, $E0, $00, $E1
; --------------------------
; Original boss Galura rank 5.0 -> Randomized boss Gogo rank 41.0
; HP: 1200 -> 47714
; ENEMY: Galura
; Original HP: 47714
; New trigger HP: 31491
org $d0b36a
db $03, $7b

; Enemy: LiquiFlame
; Stats: 
org $D02120
db $30, $51, $0d, $1c, $00, $0e, $15, $00, $20, $4E, $85, $03, $20, $4E, $00, $00, $00, $88, $77, $EF, $FF, $41, $00, $02, $00, $18, $0, $0, $00, $0, $09, $13
; Loot: 
org $D05424
db $00, $00, $00, $FC
; --------------------------
; Original boss LiquiFlame, LiquiFlame, LiquiFlame rank 6.0 -> Randomized boss Stalker, Stalker, Stalker, Stalker rank 35.0
; HP: 3000 -> 20000
; ENEMY: LiquiFlame
; Skills: ['Fight', 'Specialty', 'Flame']
; New skill: Fight
org $d0b381
db $80
; New skill: Specialty
org $d0b382
db $81
; New skill: Flame
org $d0b383
db $DB

; Enemy: LiquiFlame
; Stats: 
org $D02140
db $30, $51, $0a, $0e, $00, $2b, $2b, $00, $20, $4E, $95, $02, $20, $4E, $00, $00, $00, $FE, $77, $EF, $FF, $41, $00, $02, $20, $18, $0, $0, $00, $0, $09, $13
; Loot: 
org $D05428
db $00, $00, $00, $32
; --------------------------
; Original boss LiquiFlame, LiquiFlame, LiquiFlame rank 6.0 -> Randomized boss Stalker, Stalker, Stalker, Stalker rank 35.0
; HP: 3000 -> 20000
; ENEMY: LiquiFlame
; Skills: ['Fight', 'Specialty', 'Flame']
; New skill: Fight
org $d0b381
db $80
; New skill: Specialty
org $d0b382
db $81
; New skill: Flame
org $d0b383
db $DB
; ENEMY: LiquiFlame
; Skills: ['Fire3']
; New skill: Fire3
org $d0b3a8
db $30

; Enemy: LiquiFlame
; Stats: 
org $D02160
db $30, $51, $07, $2b, $00, $1c, $15, $00, $20, $4E, $C2, $01, $20, $4E, $00, $00, $00, $88, $77, $EF, $FF, $41, $00, $02, $00, $18, $0, $0, $00, $0, $09, $13
; Loot: 
org $D0542C
db $00, $00, $00, $3F
; --------------------------
; Original boss LiquiFlame, LiquiFlame, LiquiFlame rank 6.0 -> Randomized boss Stalker, Stalker, Stalker, Stalker rank 35.0
; HP: 3000 -> 20000
; ENEMY: LiquiFlame
; Skills: ['Fight', 'Specialty', 'Flame']
; New skill: Fight
org $d0b381
db $80
; New skill: Specialty
org $d0b382
db $81
; New skill: Flame
org $d0b383
db $DB
; ENEMY: LiquiFlame
; Skills: ['Fire3']
; New skill: Fire3
org $d0b3a8
db $30
; ENEMY: LiquiFlame
; Skills: ['Fire3']
; New skill: Fire3
org $d0b3b8
db $30

; Enemy: Sergeant
; Stats: 
org $D02A40
db $2a, $74, $02, $00, $00, $06, $0c, $0c, $A4, $1F, $20, $00, $A4, $1F, $64, $00, $00, $00, $30, $00, $00, $00, $00, $00, $00, $18, $0, $0, $00, $0, $52, $00
; Loot: 
org $D05548
db $00, $E0, $E9, $00
; --------------------------
; Original boss Sergeant, Karnak, Karnak, Karnak, Iron Claw rank 7.0 -> Randomized boss Antlion rank 29.0
; HP: 1000 -> 8100
; ENEMY: Sergeant

; Enemy: Karnak
; Stats: 
org $D02A60
db $0a, $17, $05, $00, $00, $00, $00, $19, $7E, $09, $20, $00, $00, $00, $8D, $00, $00, $00, $10, $00, $00, $00, $00, $00, $04, $18, $0, $0, $00, $0, $53, $13
; Loot: 
org $D0554C
db $00, $E0, $E0, $00
; --------------------------
; Original boss Sergeant, Karnak, Karnak, Karnak, Iron Claw rank 7.0 -> Randomized boss Antlion rank 29.0
; HP: 1000 -> 8100
; ENEMY: Sergeant
; ENEMY: Karnak
; ENEMY: Karnak
; ENEMY: Karnak

; Enemy: Karnak
; Stats: 
org $D02A60
db $0a, $17, $05, $00, $00, $00, $00, $19, $7E, $09, $20, $00, $00, $00, $8D, $00, $00, $00, $10, $00, $00, $00, $00, $00, $04, $18, $0, $0, $00, $0, $53, $13
; Loot: 
org $D0554C
db $00, $E0, $E0, $00
; --------------------------
; Original boss Sergeant, Karnak, Karnak, Karnak, Iron Claw rank 7.0 -> Randomized boss Antlion rank 29.0
; HP: 1000 -> 8100
; ENEMY: Sergeant
; ENEMY: Karnak
; ENEMY: Karnak
; ENEMY: Karnak

; Enemy: Karnak
; Stats: 
org $D02A60
db $0a, $17, $05, $00, $00, $00, $00, $19, $7E, $09, $20, $00, $00, $00, $8D, $00, $00, $00, $10, $00, $00, $00, $00, $00, $04, $18, $0, $0, $00, $0, $53, $13
; Loot: 
org $D0554C
db $00, $E0, $E0, $00
; --------------------------
; Original boss Sergeant, Karnak, Karnak, Karnak, Iron Claw rank 7.0 -> Randomized boss Antlion rank 29.0
; HP: 1000 -> 8100
; ENEMY: Sergeant
; ENEMY: Karnak
; ENEMY: Karnak
; ENEMY: Karnak

; Enemy: Iron Claw
; Stats: 
org $D02A20
db $2a, $74, $0b, $00, $19, $01, $0c, $0c, $A4, $1F, $BD, $00, $00, $00, $64, $00, $00, $00, $00, $00, $00, $00, $00, $00, $00, $8, $0, $0, $00, $0, $51, $27
; Loot: 
org $D05544
db $00, $F6, $B4, $00
; --------------------------
; Original boss Sergeant, Karnak, Karnak, Karnak, Iron Claw rank 7.0 -> Randomized boss Antlion rank 29.0
; HP: 1000 -> 8100
; ENEMY: Sergeant
; ENEMY: Karnak
; ENEMY: Karnak
; ENEMY: Karnak
; ENEMY: Iron Claw

; Enemy: Hole
; Stats: 
org $D021C0
db $01, $2f, $0e, $00, $00, $01, $13, $13, $50, $C3, $8E, $48, $00, $00, $00, $00, $00, $00, $FF, $FF, $10, $00, $00, $00, $60, $18, $0, $0, $00, $40, $0E, $12
; Loot: 
org $D05438
db $00, $00, $00, $00
; --------------------------
; Original boss Hole, Hole, Hole, Sandworm, Sandworm, Sandworm rank 12.0 -> Randomized boss Twin Tania, Twin Tania rank 48.0
; HP: 3000 -> 50000
; ENEMY: Hole
; Skills: ['Quarter']
; New skill: Quarter
org $d0b3fd
db $42
; ENEMY: Hole
; Skills: ['Quarter']
; New skill: Quarter
org $d0b3fd
db $42
; ENEMY: Hole
; Skills: ['Quarter']
; New skill: Quarter
org $d0b3fd
db $42

; Enemy: Hole
; Stats: 
org $D021C0
db $01, $2f, $0e, $00, $00, $01, $13, $13, $50, $C3, $8E, $48, $00, $00, $00, $00, $00, $00, $FF, $FF, $10, $00, $00, $00, $60, $18, $0, $0, $00, $40, $0E, $12
; Loot: 
org $D05438
db $00, $00, $00, $00
; --------------------------
; Original boss Hole, Hole, Hole, Sandworm, Sandworm, Sandworm rank 12.0 -> Randomized boss Twin Tania, Twin Tania rank 48.0
; HP: 3000 -> 50000
; ENEMY: Hole
; Skills: ['Quarter']
; New skill: Quarter
org $d0b3fd
db $42
; ENEMY: Hole
; Skills: ['Quarter']
; New skill: Quarter
org $d0b3fd
db $42
; ENEMY: Hole
; Skills: ['Quarter']
; New skill: Quarter
org $d0b3fd
db $42

; Enemy: Hole
; Stats: 
org $D021C0
db $01, $2f, $0e, $00, $00, $01, $13, $13, $50, $C3, $8E, $48, $00, $00, $00, $00, $00, $00, $FF, $FF, $10, $00, $00, $00, $60, $18, $0, $0, $00, $40, $0E, $12
; Loot: 
org $D05438
db $00, $00, $00, $00
; --------------------------
; Original boss Hole, Hole, Hole, Sandworm, Sandworm, Sandworm rank 12.0 -> Randomized boss Twin Tania, Twin Tania rank 48.0
; HP: 3000 -> 50000
; ENEMY: Hole
; Skills: ['Quarter']
; New skill: Quarter
org $d0b3fd
db $42
; ENEMY: Hole
; Skills: ['Quarter']
; New skill: Quarter
org $d0b3fd
db $42
; ENEMY: Hole
; Skills: ['Quarter']
; New skill: Quarter
org $d0b3fd
db $42

; Enemy: Sandworm
; Stats: 
org $D021A0
db $43, $95, $0d, $00, $00, $01, $13, $13, $50, $C3, $8E, $48, $1B, $41, $00, $00, $00, $00, $FF, $FF, $10, $00, $00, $00, $60, $18, $0, $0, $00, $0, $0D, $12
; Loot: 
org $D05434
db $00, $00, $00, $00
; --------------------------
; Original boss Hole, Hole, Hole, Sandworm, Sandworm, Sandworm rank 12.0 -> Randomized boss Twin Tania, Twin Tania rank 48.0
; HP: 3000 -> 50000
; ENEMY: Hole
; Skills: ['Quarter']
; New skill: Quarter
org $d0b3fd
db $42
; ENEMY: Hole
; Skills: ['Quarter']
; New skill: Quarter
org $d0b3fd
db $42
; ENEMY: Hole
; Skills: ['Quarter']
; New skill: Quarter
org $d0b3fd
db $42
; ENEMY: Sandworm
; Skills: ['Fight', 'Fight', 'Quicksand']
; New skill: Fight
org $d0b3db
db $80
; New skill: Fight
org $d0b3dc
db $80
; New skill: Quicksand
org $d0b3dd
db $C9
; ENEMY: Sandworm
; Skills: ['Fight', 'Fight', 'Quicksand']
; New skill: Fight
org $d0b3db
db $80
; New skill: Fight
org $d0b3dc
db $80
; New skill: Quicksand
org $d0b3dd
db $C9
; ENEMY: Sandworm
; Skills: ['Fight', 'Fight', 'Quicksand']
; New skill: Fight
org $d0b3db
db $80
; New skill: Fight
org $d0b3dc
db $80
; New skill: Quicksand
org $d0b3dd
db $C9

; Enemy: Sandworm
; Stats: 
org $D021A0
db $43, $95, $0d, $00, $00, $01, $13, $13, $50, $C3, $8E, $48, $1B, $41, $00, $00, $00, $00, $FF, $FF, $10, $00, $00, $00, $60, $18, $0, $0, $00, $0, $0D, $12
; Loot: 
org $D05434
db $00, $00, $00, $00
; --------------------------
; Original boss Hole, Hole, Hole, Sandworm, Sandworm, Sandworm rank 12.0 -> Randomized boss Twin Tania, Twin Tania rank 48.0
; HP: 3000 -> 50000
; ENEMY: Hole
; Skills: ['Quarter']
; New skill: Quarter
org $d0b3fd
db $42
; ENEMY: Hole
; Skills: ['Quarter']
; New skill: Quarter
org $d0b3fd
db $42
; ENEMY: Hole
; Skills: ['Quarter']
; New skill: Quarter
org $d0b3fd
db $42
; ENEMY: Sandworm
; Skills: ['Fight', 'Fight', 'Quicksand']
; New skill: Fight
org $d0b3db
db $80
; New skill: Fight
org $d0b3dc
db $80
; New skill: Quicksand
org $d0b3dd
db $C9
; ENEMY: Sandworm
; Skills: ['Fight', 'Fight', 'Quicksand']
; New skill: Fight
org $d0b3db
db $80
; New skill: Fight
org $d0b3dc
db $80
; New skill: Quicksand
org $d0b3dd
db $C9
; ENEMY: Sandworm
; Skills: ['Fight', 'Fight', 'Quicksand']
; New skill: Fight
org $d0b3db
db $80
; New skill: Fight
org $d0b3dc
db $80
; New skill: Quicksand
org $d0b3dd
db $C9

; Enemy: Sandworm
; Stats: 
org $D021A0
db $43, $95, $0d, $00, $00, $01, $13, $13, $50, $C3, $8E, $48, $1B, $41, $00, $00, $00, $00, $FF, $FF, $10, $00, $00, $00, $60, $18, $0, $0, $00, $0, $0D, $12
; Loot: 
org $D05434
db $00, $00, $00, $00
; --------------------------
; Original boss Hole, Hole, Hole, Sandworm, Sandworm, Sandworm rank 12.0 -> Randomized boss Twin Tania, Twin Tania rank 48.0
; HP: 3000 -> 50000
; ENEMY: Hole
; Skills: ['Quarter']
; New skill: Quarter
org $d0b3fd
db $42
; ENEMY: Hole
; Skills: ['Quarter']
; New skill: Quarter
org $d0b3fd
db $42
; ENEMY: Hole
; Skills: ['Quarter']
; New skill: Quarter
org $d0b3fd
db $42
; ENEMY: Sandworm
; Skills: ['Fight', 'Fight', 'Quicksand']
; New skill: Fight
org $d0b3db
db $80
; New skill: Fight
org $d0b3dc
db $80
; New skill: Quicksand
org $d0b3dd
db $C9
; ENEMY: Sandworm
; Skills: ['Fight', 'Fight', 'Quicksand']
; New skill: Fight
org $d0b3db
db $80
; New skill: Fight
org $d0b3dc
db $80
; New skill: Quicksand
org $d0b3dd
db $C9
; ENEMY: Sandworm
; Skills: ['Fight', 'Fight', 'Quicksand']
; New skill: Fight
org $d0b3db
db $80
; New skill: Fight
org $d0b3dc
db $80
; New skill: Quicksand
org $d0b3dd
db $C9

; Enemy: Hole
; Stats: 
org $D021E0
db $84, $0d, $02, $00, $00, $01, $13, $13, $50, $C3, $8E, $48, $00, $00, $00, $00, $00, $00, $FF, $FF, $10, $00, $00, $80, $60, $18, $0, $0, $00, $80, $0F, $12
; Loot: 
org $D0543C
db $00, $00, $00, $00
; --------------------------
; Original boss Hole, Hole, Hole, Sandworm, Sandworm, Sandworm rank 12.0 -> Randomized boss Twin Tania, Twin Tania rank 48.0
; HP: 3000 -> 50000
; ENEMY: Hole
; Skills: ['Quarter']
; New skill: Quarter
org $d0b3fd
db $42
; ENEMY: Hole
; Skills: ['Quarter']
; New skill: Quarter
org $d0b3fd
db $42
; ENEMY: Hole
; Skills: ['Quarter']
; New skill: Quarter
org $d0b3fd
db $42
; ENEMY: Sandworm
; Skills: ['Fight', 'Fight', 'Quicksand']
; New skill: Fight
org $d0b3db
db $80
; New skill: Fight
org $d0b3dc
db $80
; New skill: Quicksand
org $d0b3dd
db $C9
; ENEMY: Sandworm
; Skills: ['Fight', 'Fight', 'Quicksand']
; New skill: Fight
org $d0b3db
db $80
; New skill: Fight
org $d0b3dc
db $80
; New skill: Quicksand
org $d0b3dd
db $C9
; ENEMY: Sandworm
; Skills: ['Fight', 'Fight', 'Quicksand']
; New skill: Fight
org $d0b3db
db $80
; New skill: Fight
org $d0b3dc
db $80
; New skill: Quicksand
org $d0b3dd
db $C9
; ENEMY: Hole

; Enemy: AdamanTiMi
; Stats: 
org $D02200
db $1b, $36, $0d, $00, $19, $00, $04, $2f, $EC, $2C, $77, $00, $EC, $2C, $00, $00, $00, $00, $7A, $70, $10, $00, $00, $02, $00, $18, $0, $0, $60, $0, $10, $14
; Loot: 
org $D05440
db $00, $F5, $00, $E7
; --------------------------
; Original boss AdamanTiMi rank 13.0 -> Randomized boss Gilgamesh rank 19.0
; HP: 2000 -> 11500
; ENEMY: AdamanTiMi

; Enemy: Sol Cannon
; Stats: 
org $D02280
db $41, $09, $02, $00, $06, $01, $0e, $0e, $20, $4E, $62, $05, $10, $27, $64, $00, $00, $C8, $FF, $FF, $10, $00, $00, $04, $20, $98, $0, $0, $00, $0, $14, $24
; Loot: 
org $D05450
db $E3, $E2, $00, $EB
; --------------------------
; Original boss Sol Cannon, Launcher, Launcher rank 14.0 -> Randomized boss Golem, BoneDragon, ZombieDrgn, Golem rank 33.0
; HP: 22500 -> 20000
; ENEMY: Sol Cannon

; Enemy: Launcher
; Stats: 
org $D02B60
db $15, $09, $02, $00, $00, $01, $09, $09, $D0, $07, $62, $05, $00, $00, $00, $00, $00, $C8, $FF, $FF, $00, $00, $00, $00, $20, $98, $0, $0, $00, $0, $5B, $32
; Loot: 
org $D0556C
db $00, $E2, $00, $E1
; --------------------------
; Original boss Sol Cannon, Launcher, Launcher rank 14.0 -> Randomized boss Golem, BoneDragon, ZombieDrgn, Golem rank 33.0
; HP: 22500 -> 20000
; ENEMY: Sol Cannon
; ENEMY: Launcher

; Enemy: Launcher
; Stats: 
org $D02B80
db $15, $09, $02, $00, $00, $01, $09, $09, $D0, $07, $62, $05, $00, $00, $00, $00, $00, $C8, $FF, $FF, $00, $00, $00, $00, $20, $98, $0, $0, $00, $0, $5B, $32
; Loot: 
org $D05570
db $00, $E2, $00, $E1
; --------------------------
; Original boss Sol Cannon, Launcher, Launcher rank 14.0 -> Randomized boss Golem, BoneDragon, ZombieDrgn, Golem rank 33.0
; HP: 22500 -> 20000
; ENEMY: Sol Cannon
; ENEMY: Launcher
; ENEMY: Launcher

; Enemy: ArchaeAvis
; Stats: 
org $D022A0
db $22, $7a, $08, $0f, $22, $01, $0d, $00, $48, $0D, $79, $0B, $68, $42, $00, $00, $00, $20, $F4, $FF, $10, $00, $40, $40, $20, $98, $88, $0, $00, $0, $15, $15
; Loot: 
org $D05454
db $00, $00, $00, $F2
; --------------------------
; Original boss ArchaeAvis, ArchaeAvis, ArchaeAvis, ArchaeAvis, ArchaeAvis rank 15.0 -> Randomized boss Odin rank 36.0
; HP: 1600 -> 17000
; ENEMY: ArchaeAvis
; Skills: ['Fight', 'BreathWing', 'Specialty']
; New skill: Fight
org $d0b4fe
db $80
; New skill: BreathWing
org $d0b4ff
db $DA
; New skill: Specialty
org $d0b500
db $81

; Enemy: ArchaeAvis
; Stats: 
org $D022C0
db $22, $7a, $08, $0f, $26, $01, $15, $00, $48, $0D, $79, $0B, $68, $42, $00, $00, $00, $20, $F4, $FF, $10, $02, $40, $00, $00, $98, $88, $0, $00, $0, $15, $13
; Loot: 
org $D05458
db $00, $00, $00, $F3
; --------------------------
; Original boss ArchaeAvis, ArchaeAvis, ArchaeAvis, ArchaeAvis, ArchaeAvis rank 15.0 -> Randomized boss Odin rank 36.0
; HP: 1600 -> 17000
; ENEMY: ArchaeAvis
; Skills: ['Fight', 'BreathWing', 'Specialty']
; New skill: Fight
org $d0b4fe
db $80
; New skill: BreathWing
org $d0b4ff
db $DA
; New skill: Specialty
org $d0b500
db $81
; ENEMY: ArchaeAvis
; Skills: ['Fight', 'Blaze', 'Specialty']
; New skill: Fight
org $d0b513
db $80
; New skill: Blaze
org $d0b514
db $CD
; New skill: Specialty
org $d0b515
db $81

; Enemy: ArchaeAvis
; Stats: 
org $D022E0
db $22, $7a, $08, $0f, $24, $01, $24, $00, $48, $0D, $79, $0B, $68, $42, $00, $00, $00, $20, $F4, $FF, $10, $01, $40, $00, $20, $98, $88, $0, $00, $0, $15, $17
; Loot: 
org $D0545C
db $00, $00, $00, $F4
; --------------------------
; Original boss ArchaeAvis, ArchaeAvis, ArchaeAvis, ArchaeAvis, ArchaeAvis rank 15.0 -> Randomized boss Odin rank 36.0
; HP: 1600 -> 17000
; ENEMY: ArchaeAvis
; Skills: ['Fight', 'BreathWing', 'Specialty']
; New skill: Fight
org $d0b4fe
db $80
; New skill: BreathWing
org $d0b4ff
db $DA
; New skill: Specialty
org $d0b500
db $81
; ENEMY: ArchaeAvis
; Skills: ['Fight', 'Blaze', 'Specialty']
; New skill: Fight
org $d0b513
db $80
; New skill: Blaze
org $d0b514
db $CD
; New skill: Specialty
org $d0b515
db $81
; ENEMY: ArchaeAvis
; Skills: ['Fight', 'Flame', 'Specialty']
; New skill: Fight
org $d0b528
db $80
; New skill: Flame
org $d0b529
db $DB
; New skill: Specialty
org $d0b52a
db $81

; Enemy: ArchaeAvis
; Stats: 
org $D02300
db $22, $7a, $08, $0f, $26, $01, $2c, $00, $48, $0D, $79, $0B, $68, $42, $00, $00, $00, $20, $F4, $FF, $10, $04, $40, $00, $00, $98, $88, $0, $00, $0, $15, $18
; Loot: 
org $D05460
db $00, $00, $00, $F5
; --------------------------
; Original boss ArchaeAvis, ArchaeAvis, ArchaeAvis, ArchaeAvis, ArchaeAvis rank 15.0 -> Randomized boss Odin rank 36.0
; HP: 1600 -> 17000
; ENEMY: ArchaeAvis
; Skills: ['Fight', 'BreathWing', 'Specialty']
; New skill: Fight
org $d0b4fe
db $80
; New skill: BreathWing
org $d0b4ff
db $DA
; New skill: Specialty
org $d0b500
db $81
; ENEMY: ArchaeAvis
; Skills: ['Fight', 'Blaze', 'Specialty']
; New skill: Fight
org $d0b513
db $80
; New skill: Blaze
org $d0b514
db $CD
; New skill: Specialty
org $d0b515
db $81
; ENEMY: ArchaeAvis
; Skills: ['Fight', 'Flame', 'Specialty']
; New skill: Fight
org $d0b528
db $80
; New skill: Flame
org $d0b529
db $DB
; New skill: Specialty
org $d0b52a
db $81
; ENEMY: ArchaeAvis
; Skills: ['Fight', 'Thunder', 'Specialty']
; New skill: Fight
org $d0b53d
db $80
; New skill: Thunder
org $d0b53e
db $DC
; New skill: Specialty
org $d0b53f
db $81

; Enemy: ArchaeAvis
; Stats: 
org $D02320
db $28, $82, $0b, $0f, $13, $01, $32, $00, $48, $0D, $79, $0B, $68, $42, $00, $00, $00, $67, $F4, $FF, $10, $00, $40, $00, $20, $98, $88, $0, $00, $0, $15, $14
; Loot: 
org $D05464
db $00, $00, $00, $F6
; --------------------------
; Original boss ArchaeAvis, ArchaeAvis, ArchaeAvis, ArchaeAvis, ArchaeAvis rank 15.0 -> Randomized boss Odin rank 36.0
; HP: 1600 -> 17000
; ENEMY: ArchaeAvis
; Skills: ['Fight', 'BreathWing', 'Specialty']
; New skill: Fight
org $d0b4fe
db $80
; New skill: BreathWing
org $d0b4ff
db $DA
; New skill: Specialty
org $d0b500
db $81
; ENEMY: ArchaeAvis
; Skills: ['Fight', 'Blaze', 'Specialty']
; New skill: Fight
org $d0b513
db $80
; New skill: Blaze
org $d0b514
db $CD
; New skill: Specialty
org $d0b515
db $81
; ENEMY: ArchaeAvis
; Skills: ['Fight', 'Flame', 'Specialty']
; New skill: Fight
org $d0b528
db $80
; New skill: Flame
org $d0b529
db $DB
; New skill: Specialty
org $d0b52a
db $81
; ENEMY: ArchaeAvis
; Skills: ['Fight', 'Thunder', 'Specialty']
; New skill: Fight
org $d0b53d
db $80
; New skill: Thunder
org $d0b53e
db $DC
; New skill: Specialty
org $d0b53f
db $81
; ENEMY: ArchaeAvis
; Skills: ['BreathWing', 'Maelstrom', 'Specialty', 'Entangle', 'Fight', 'Specialty', 'Flame', 'Maelstrom', 'Specialty', 'Entangle', 'Fight', 'Specialty', 'Thunder', 'Maelstrom', 'Specialty', 'Entangle', 'Fight', 'Specialty', 'Blaze', 'Maelstrom', 'Specialty', 'Entangle', 'Fight', 'Specialty']
; New skill: BreathWing
org $d0b567
db $DA
; New skill: Maelstrom
org $d0b568
db $C2
; New skill: Specialty
org $d0b569
db $81
; New skill: Entangle
org $d0b56b
db $BC
; New skill: Fight
org $d0b56c
db $80
; New skill: Specialty
org $d0b56d
db $81
; New skill: Flame
org $d0b56f
db $DB
; New skill: Maelstrom
org $d0b570
db $C2
; New skill: Specialty
org $d0b571
db $81
; New skill: Entangle
org $d0b573
db $BC
; New skill: Fight
org $d0b574
db $80
; New skill: Specialty
org $d0b575
db $81
; New skill: Thunder
org $d0b577
db $DC
; New skill: Maelstrom
org $d0b578
db $C2
; New skill: Specialty
org $d0b579
db $81
; New skill: Entangle
org $d0b57b
db $BC
; New skill: Fight
org $d0b57c
db $80
; New skill: Specialty
org $d0b57d
db $81
; New skill: Blaze
org $d0b57f
db $CD
; New skill: Maelstrom
org $d0b580
db $C2
; New skill: Specialty
org $d0b581
db $81
; New skill: Entangle
org $d0b583
db $BC
; New skill: Fight
org $d0b584
db $80
; New skill: Specialty
org $d0b585
db $81

; Enemy: Chim.Brain
; Stats: 
org $D02340
db $24, $5e, $07, $0b, $0b, $19, $17, $00, $84, $79, $8D, $04, $84, $79, $00, $00, $00, $00, $30, $70, $00, $02, $00, $00, $04, $18, $0, $0, $00, $0, $1A, $13
; Loot: 
org $D05468
db $1B, $EA, $00, $E4
; --------------------------
; Original boss Chim.Brain rank 16.0 -> Randomized boss Guardian, Guardian, Guardian, Guardian rank 26.0
; HP: 3300 -> 31108
; ENEMY: Chim.Brain
; Skills: ['AquaRake', 'Fight', 'Specialty', 'AquaRake', 'Blaze', 'Blaze']
; New skill: AquaRake
org $d0b58e
db $84
; New skill: Fight
org $d0b58f
db $80
; New skill: Specialty
org $d0b590
db $81
; New skill: AquaRake
org $d0b592
db $84
; New skill: Blaze
org $d0b593
db $CD
; New skill: Blaze
org $d0b594
db $CD

; Enemy: Titan
; Stats: 
org $D02360
db $13, $36, $0d, $07, $07, $00, $00, $00, $D0, $07, $01, $06, $D0, $07, $00, $00, $00, $00, $F7, $DF, $00, $20, $00, $00, $A0, $18, $0, $0, $00, $0, $1B, $01
; Loot: 
org $D0546C
db $26, $E0, $00, $E1
; --------------------------
; Original boss Titan rank 18.0 -> Randomized boss AdamanTiMi rank 13.0
; HP: 2500 -> 2000
; ENEMY: Titan
; Skills: ['Fight', 'Fight', 'Specialty', 'Fight', 'Quicksand', 'Specialty']
; New skill: Fight
org $d0b59d
db $80
; New skill: Fight
org $d0b59e
db $80
; New skill: Specialty
org $d0b59f
db $81
; New skill: Fight
org $d0b5a1
db $80
; New skill: Quicksand
org $d0b5a2
db $C9
; New skill: Specialty
org $d0b5a3
db $81

; Enemy: Puroboros
; Stats: 
org $D02380
db $15, $71, $08, $00, $00, $0d, $00, $00, $83, $06, $87, $00, $83, $06, $00, $00, $00, $00, $30, $30, $00, $00, $00, $00, $00, $8, $0, $0, $00, $0, $1C, $16
; Loot: 
org $D05470
db $E9, $00, $E0, $00
; --------------------------
; Original boss Puroboros, Puroboros, Puroboros, Puroboros, Puroboros, Puroboros rank 17.0 -> Randomized boss Shoat rank 32.0
; HP: 1500 -> 10000
; ENEMY: Puroboros
; ENEMY: Puroboros
; ENEMY: Puroboros
; ENEMY: Puroboros
; ENEMY: Puroboros
; ENEMY: Puroboros

; Enemy: Puroboros
; Stats: 
org $D02380
db $15, $71, $08, $00, $00, $0d, $00, $00, $83, $06, $87, $00, $83, $06, $00, $00, $00, $00, $30, $30, $00, $00, $00, $00, $00, $8, $0, $0, $00, $0, $1C, $16
; Loot: 
org $D05470
db $E9, $00, $E0, $00
; --------------------------
; Original boss Puroboros, Puroboros, Puroboros, Puroboros, Puroboros, Puroboros rank 17.0 -> Randomized boss Shoat rank 32.0
; HP: 1500 -> 10000
; ENEMY: Puroboros
; ENEMY: Puroboros
; ENEMY: Puroboros
; ENEMY: Puroboros
; ENEMY: Puroboros
; ENEMY: Puroboros

; Enemy: Puroboros
; Stats: 
org $D02380
db $15, $71, $08, $00, $00, $0d, $00, $00, $83, $06, $87, $00, $83, $06, $00, $00, $00, $00, $30, $30, $00, $00, $00, $00, $00, $8, $0, $0, $00, $0, $1C, $16
; Loot: 
org $D05470
db $E9, $00, $E0, $00
; --------------------------
; Original boss Puroboros, Puroboros, Puroboros, Puroboros, Puroboros, Puroboros rank 17.0 -> Randomized boss Shoat rank 32.0
; HP: 1500 -> 10000
; ENEMY: Puroboros
; ENEMY: Puroboros
; ENEMY: Puroboros
; ENEMY: Puroboros
; ENEMY: Puroboros
; ENEMY: Puroboros

; Enemy: Puroboros
; Stats: 
org $D02380
db $15, $71, $08, $00, $00, $0d, $00, $00, $83, $06, $87, $00, $83, $06, $00, $00, $00, $00, $30, $30, $00, $00, $00, $00, $00, $8, $0, $0, $00, $0, $1C, $16
; Loot: 
org $D05470
db $E9, $00, $E0, $00
; --------------------------
; Original boss Puroboros, Puroboros, Puroboros, Puroboros, Puroboros, Puroboros rank 17.0 -> Randomized boss Shoat rank 32.0
; HP: 1500 -> 10000
; ENEMY: Puroboros
; ENEMY: Puroboros
; ENEMY: Puroboros
; ENEMY: Puroboros
; ENEMY: Puroboros
; ENEMY: Puroboros

; Enemy: Puroboros
; Stats: 
org $D02380
db $15, $71, $08, $00, $00, $0d, $00, $00, $83, $06, $87, $00, $83, $06, $00, $00, $00, $00, $30, $30, $00, $00, $00, $00, $00, $8, $0, $0, $00, $0, $1C, $16
; Loot: 
org $D05470
db $E9, $00, $E0, $00
; --------------------------
; Original boss Puroboros, Puroboros, Puroboros, Puroboros, Puroboros, Puroboros rank 17.0 -> Randomized boss Shoat rank 32.0
; HP: 1500 -> 10000
; ENEMY: Puroboros
; ENEMY: Puroboros
; ENEMY: Puroboros
; ENEMY: Puroboros
; ENEMY: Puroboros
; ENEMY: Puroboros

; Enemy: Puroboros
; Stats: 
org $D02380
db $15, $71, $08, $00, $00, $0d, $00, $00, $83, $06, $87, $00, $83, $06, $00, $00, $00, $00, $30, $30, $00, $00, $00, $00, $00, $8, $0, $0, $00, $0, $1C, $16
; Loot: 
org $D05470
db $E9, $00, $E0, $00
; --------------------------
; Original boss Puroboros, Puroboros, Puroboros, Puroboros, Puroboros, Puroboros rank 17.0 -> Randomized boss Shoat rank 32.0
; HP: 1500 -> 10000
; ENEMY: Puroboros
; ENEMY: Puroboros
; ENEMY: Puroboros
; ENEMY: Puroboros
; ENEMY: Puroboros
; ENEMY: Puroboros

; Enemy: Gilgamesh
; Stats: 
org $D023C0
db $1c, $9a, $07, $00, $00, $00, $00, $00, $20, $4E, $FF, $0A, $20, $4E, $00, $00, $0E, $00, $64, $70, $00, $00, $00, $00, $00, $98, $0, $0, $00, $0, $1E, $1a
; Loot: 
org $D05478
db $00, $00, $00, $E3
; --------------------------
; Original boss Gilgamesh rank 19.0 -> Randomized boss Merugene, Merugene, Merugene, Merugene rank 34.0
; HP: 11500 -> 20000
; ENEMY: Gilgamesh
; Original HP: 20000
; New trigger HP: 17400
org $d0b5f5
db $f8, $43

; Enemy: Gilgamesh
; Stats: 
org $D02460
db $3d, $d8, $0a, $13, $20, $00, $13, $00, $FF, $FF, $49, $07, $FF, $FF, $00, $00, $10, $00, $F4, $70, $10, $00, $00, $00, $A0, $98, $0, $0, $00, $0, $23, $1c
; Loot: 
org $D0548C
db $1A, $F6, $00, $91
; --------------------------
; Original boss Gilgamesh rank 20.0 -> Randomized boss Necrofobia, Barrier, Barrier, Barrier, Barrier, Gilgamesh rank 49.0
; HP: 6500 -> 65535
; ENEMY: Gilgamesh
; Original HP: 65535
; New trigger HP: 24903
org $d0b674
db $47, $61

; Enemy: Tyrasaurus
; Stats: 
org $D02480
db $41, $ab, $0b, $00, $2d, $00, $2d, $00, $FC, $6C, $CF, $06, $FC, $6C, $00, $00, $00, $02, $74, $74, $10, $00, $00, $01, $11, $18, $0, $0, $00, $0, $24, $1d
; Loot: 
org $D05490
db $85, $00, $E3, $00
; --------------------------
; Original boss Tyrasaurus rank 21.0 -> Randomized boss Apocalypse rank 45.0
; HP: 5000 -> 27900
; ENEMY: Tyrasaurus

; Enemy: Abductor
; Stats: 
org $D024C0
db $22, $5b, $08, $00, $0c, $4f, $12, $00, $1D, $4E, $6E, $04, $1D, $4E, $00, $00, $00, $00, $34, $20, $00, $00, $40, $00, $00, $18, $88, $0, $00, $0, $26, $1d
; Loot: 
org $D05498
db $BA, $E1, $E0, $00
; --------------------------
; Original boss Abductor rank 22.0 -> Randomized boss Atmos rank 25.0
; HP: 2500 -> 19997
; ENEMY: Abductor

; Enemy: HiryuuPlant
; Stats: 
org $D024E0
db $1a, $10, $04, $00, $00, $14, $11, $00, $FA, $00, $93, $01, $FA, $00, $00, $00, $00, $00, $74, $74, $00, $00, $00, $00, $80, $18, $80, $0, $01, $0, $27, $21
; Loot: 
org $D0549C
db $00, $00, $00, $E3
; --------------------------
; Original boss HiryuuPlant, HiryuuFlowr, HiryuuFlowr, HiryuuFlowr, HiryuuFlowr, HiryuuFlowr rank 23.0 -> Randomized boss WingRaptor, WingRaptor rank 1.0
; HP: 12000 -> 250
; ENEMY: HiryuuPlant

; Enemy: HiryuuFlowr
; Stats: 
org $D02500
db $0d, $03, $0a, $00, $00, $0f, $0f, $0c, $0C, $00, $93, $01, $00, $00, $00, $00, $00, $00, $00, $00, $00, $00, $00, $00, $00, $18, $80, $0, $01, $0, $28, $1f
; Loot: 
org $D054A0
db $00, $00, $E4, $00
; --------------------------
; Original boss HiryuuPlant, HiryuuFlowr, HiryuuFlowr, HiryuuFlowr, HiryuuFlowr, HiryuuFlowr rank 23.0 -> Randomized boss WingRaptor, WingRaptor rank 1.0
; HP: 12000 -> 250
; ENEMY: HiryuuPlant
; ENEMY: HiryuuFlowr

; Enemy: HiryuuFlowr
; Stats: 
org $D02520
db $0b, $03, $0a, $00, $00, $0f, $0f, $0c, $0C, $00, $93, $01, $00, $00, $00, $00, $00, $00, $00, $00, $00, $00, $00, $00, $00, $18, $80, $0, $01, $0, $28, $1f
; Loot: 
org $D054A4
db $00, $00, $E4, $00
; --------------------------
; Original boss HiryuuPlant, HiryuuFlowr, HiryuuFlowr, HiryuuFlowr, HiryuuFlowr, HiryuuFlowr rank 23.0 -> Randomized boss WingRaptor, WingRaptor rank 1.0
; HP: 12000 -> 250
; ENEMY: HiryuuPlant
; ENEMY: HiryuuFlowr
; ENEMY: HiryuuFlowr

; Enemy: HiryuuFlowr
; Stats: 
org $D02540
db $10, $03, $0a, $00, $00, $0f, $0f, $0c, $0C, $00, $93, $01, $00, $00, $00, $00, $00, $00, $00, $00, $00, $00, $00, $00, $00, $18, $80, $0, $01, $0, $28, $21
; Loot: 
org $D054A8
db $00, $00, $E4, $00
; --------------------------
; Original boss HiryuuPlant, HiryuuFlowr, HiryuuFlowr, HiryuuFlowr, HiryuuFlowr, HiryuuFlowr rank 23.0 -> Randomized boss WingRaptor, WingRaptor rank 1.0
; HP: 12000 -> 250
; ENEMY: HiryuuPlant
; ENEMY: HiryuuFlowr
; ENEMY: HiryuuFlowr
; ENEMY: HiryuuFlowr

; Enemy: HiryuuFlowr
; Stats: 
org $D02560
db $0d, $03, $0a, $00, $00, $0f, $0f, $0c, $0C, $00, $93, $01, $00, $00, $00, $00, $00, $00, $00, $00, $00, $00, $00, $00, $00, $18, $80, $0, $01, $0, $28, $1f
; Loot: 
org $D054AC
db $00, $00, $E4, $00
; --------------------------
; Original boss HiryuuPlant, HiryuuFlowr, HiryuuFlowr, HiryuuFlowr, HiryuuFlowr, HiryuuFlowr rank 23.0 -> Randomized boss WingRaptor, WingRaptor rank 1.0
; HP: 12000 -> 250
; ENEMY: HiryuuPlant
; ENEMY: HiryuuFlowr
; ENEMY: HiryuuFlowr
; ENEMY: HiryuuFlowr
; ENEMY: HiryuuFlowr

; Enemy: HiryuuFlowr
; Stats: 
org $D02580
db $0b, $03, $0a, $00, $00, $0f, $0f, $0c, $0C, $00, $93, $01, $00, $00, $00, $00, $00, $00, $00, $00, $00, $00, $00, $00, $00, $18, $80, $0, $01, $0, $28, $23
; Loot: 
org $D054B0
db $00, $00, $E4, $00
; --------------------------
; Original boss HiryuuPlant, HiryuuFlowr, HiryuuFlowr, HiryuuFlowr, HiryuuFlowr, HiryuuFlowr rank 23.0 -> Randomized boss WingRaptor, WingRaptor rank 1.0
; HP: 12000 -> 250
; ENEMY: HiryuuPlant
; ENEMY: HiryuuFlowr
; ENEMY: HiryuuFlowr
; ENEMY: HiryuuFlowr
; ENEMY: HiryuuFlowr
; ENEMY: HiryuuFlowr

; Enemy: Gilgamesh
; Stats: 
org $D025A0
db $31, $64, $07, $13, $13, $47, $13, $0c, $98, $3A, $3F, $04, $98, $3A, $00, $00, $2A, $00, $74, $70, $10, $00, $00, $00, $A0, $18, $0, $0, $00, $0, $2D, $1f
; Loot: 
org $D054B4
db $00, $C9, $00, $85
; --------------------------
; Original boss Gilgamesh, Enkidou rank 24.0 -> Randomized boss Gilgamesh, Gilgamesh rank 28.0
; HP: 8888 -> 30000
; ENEMY: Gilgamesh
; Original HP: 15000
; New trigger HP: 10050
org $d0b761
db $42, $27

; Enemy: Enkidou
; Stats: 
org $D025C0
db $31, $64, $06, $1f, $00, $34, $00, $18, $98, $3A, $CA, $04, $98, $3A, $00, $00, $23, $20, $74, $70, $10, $00, $00, $00, $80, $8, $88, $0, $00, $0, $2E, $1d
; Loot: 
org $D054B8
db $00, $97, $00, $1A
; --------------------------
; Original boss Gilgamesh, Enkidou rank 24.0 -> Randomized boss Gilgamesh, Gilgamesh rank 28.0
; HP: 8888 -> 30000
; ENEMY: Gilgamesh
; Original HP: 15000
; New trigger HP: 10050
org $d0b761
db $42, $27
; ENEMY: Enkidou
; Skills: ['Aero3']
; New skill: Aero3
org $d0b7c0
db $91

; Enemy: Atmos
; Stats: 
org $D025E0
db $1f, $07, $06, $00, $0a, $39, $0e, $0e, $D0, $07, $A5, $1B, $D0, $07, $00, $00, $00, $00, $FF, $BF, $FF, $00, $00, $00, $20, $18, $0, $0, $08, $0, $2F, $29
; Loot: 
org $D054BC
db $5E, $E2, $00, $EB
; --------------------------
; Original boss Atmos rank 25.0 -> Randomized boss Crayclaw rank 11.0
; HP: 19997 -> 2000
; ENEMY: Atmos

; Enemy: Guardian
; Stats: 
org $D02600
db $36, $82, $0d, $00, $13, $16, $26, $20, $87, $13, $47, $45, $87, $13, $00, $00, $00, $1E, $74, $FC, $10, $01, $00, $00, $00, $18, $0, $0, $00, $0, $30, $4d
; Loot: 
org $D054C0
db $E3, $00, $62, $00
; --------------------------
; Original boss Guardian, Guardian, Guardian, Guardian rank 26.0 -> Randomized boss Catastroph rank 46.0
; HP: 7777 -> 19997
; ENEMY: Guardian
; Skills: ['Fire3']
; New skill: Fire3
org $d0b865
db $30
; Original HP: 4999
; New trigger HP: 1900
org $d0b85e
db $6c, $07

; Enemy: Guardian
; Stats: 
org $D02620
db $36, $82, $0d, $00, $13, $01, $26, $20, $87, $13, $47, $45, $87, $13, $00, $00, $00, $1E, $74, $FC, $10, $20, $00, $00, $00, $18, $0, $0, $00, $0, $31, $4d
; Loot: 
org $D054C4
db $E3, $00, $62, $00
; --------------------------
; Original boss Guardian, Guardian, Guardian, Guardian rank 26.0 -> Randomized boss Catastroph rank 46.0
; HP: 7777 -> 19997
; ENEMY: Guardian
; Skills: ['Fire3']
; New skill: Fire3
org $d0b865
db $30
; Original HP: 4999
; New trigger HP: 1900
org $d0b85e
db $6c, $07
; ENEMY: Guardian
; Skills: ['Quake']
; New skill: Quake
org $d0b877
db $D6
; Original HP: 4999
; New trigger HP: 1900
org $d0b874
db $6c, $07

; Enemy: Guardian
; Stats: 
org $D02640
db $3d, $82, $0d, $00, $13, $16, $26, $20, $87, $13, $47, $45, $87, $13, $00, $00, $00, $1E, $74, $FC, $10, $80, $00, $00, $00, $18, $0, $0, $00, $0, $32, $4d
; Loot: 
org $D054C8
db $E3, $00, $62, $00
; --------------------------
; Original boss Guardian, Guardian, Guardian, Guardian rank 26.0 -> Randomized boss Catastroph rank 46.0
; HP: 7777 -> 19997
; ENEMY: Guardian
; Skills: ['Fire3']
; New skill: Fire3
org $d0b865
db $30
; Original HP: 4999
; New trigger HP: 1900
org $d0b85e
db $6c, $07
; ENEMY: Guardian
; Skills: ['Quake']
; New skill: Quake
org $d0b877
db $D6
; Original HP: 4999
; New trigger HP: 1900
org $d0b874
db $6c, $07
; ENEMY: Guardian
; Skills: ['AquaRake']
; New skill: AquaRake
org $d0b889
db $84
; Original HP: 4999
; New trigger HP: 1900
org $d0b886
db $6c, $07

; Enemy: Guardian
; Stats: 
org $D02660
db $42, $82, $0d, $00, $13, $0c, $26, $20, $87, $13, $47, $45, $87, $13, $00, $00, $00, $1E, $74, $FC, $10, $40, $00, $00, $00, $18, $0, $0, $00, $0, $33, $4d
; Loot: 
org $D054CC
db $E3, $00, $62, $00
; --------------------------
; Original boss Guardian, Guardian, Guardian, Guardian rank 26.0 -> Randomized boss Catastroph rank 46.0
; HP: 7777 -> 19997
; ENEMY: Guardian
; Skills: ['Fire3']
; New skill: Fire3
org $d0b865
db $30
; Original HP: 4999
; New trigger HP: 1900
org $d0b85e
db $6c, $07
; ENEMY: Guardian
; Skills: ['Quake']
; New skill: Quake
org $d0b877
db $D6
; Original HP: 4999
; New trigger HP: 1900
org $d0b874
db $6c, $07
; ENEMY: Guardian
; Skills: ['AquaRake']
; New skill: AquaRake
org $d0b889
db $84
; Original HP: 4999
; New trigger HP: 1900
org $d0b886
db $6c, $07
; ENEMY: Guardian
; Skills: ['Aero3']
; New skill: Aero3
org $d0b89f
db $91
; Original HP: 4999
; New trigger HP: 1900
org $d0b898
db $6c, $07

; Enemy: Carbunkle
; Stats: 
org $D02680
db $1f, $1f, $06, $2f, $18, $4b, $18, $18, $10, $0E, $75, $1A, $10, $0E, $00, $00, $00, $20, $F4, $FB, $10, $00, $00, $00, $24, $18, $88, $0, $80, $0, $34, $2c
; Loot: 
org $D054D0
db $F2, $CA, $E7, $00
; --------------------------
; Original boss Carbunkle, Carbunkle rank 27.0 -> Randomized boss Byblos rank 10.0
; HP: 15000 -> 3600
; ENEMY: Carbunkle
; Original HP: 3600
; New trigger HP: 2376
org $d0b8ae
db $48, $09
; Original HP: 3600
; New trigger HP: 1188
org $d0b8d1
db $a4, $04

; Enemy: Carbunkle
; Stats: 
org $D02BC0
db $12, $05, $02, $06, $06, $06, $00, $00, $10, $0E, $A5, $02, $10, $0E, $00, $00, $00, $00, $80, $0B, $00, $00, $00, $FF, $00, $18, $0, $0, $00, $0, $5E, $01
; Loot: 
org $D05578
db $F2, $CA, $E7, $00
; --------------------------
; Original boss Carbunkle, Carbunkle rank 27.0 -> Randomized boss Byblos rank 10.0
; HP: 15000 -> 3600
; ENEMY: Carbunkle
; Original HP: 3600
; New trigger HP: 2376
org $d0b8ae
db $48, $09
; Original HP: 3600
; New trigger HP: 1188
org $d0b8d1
db $a4, $04
; ENEMY: Carbunkle

; Enemy: Gilgamesh
; Stats: 
org $D02BA0
db $34, $30, $08, $00, $06, $01, $0a, $14, $B8, $0B, $C4, $05, $B8, $0B, $00, $00, $00, $00, $F7, $FC, $10, $00, $00, $00, $A0, $98, $0, $0, $00, $0, $5D, $35
; Loot: 
org $D05574
db $C2, $E1, $00, $00
; --------------------------
; Original boss Gilgamesh, Gilgamesh rank 28.0 -> Randomized boss Hole, Hole, Hole, Sandworm, Sandworm, Sandworm rank 12.0
; HP: 30000 -> 3000
; ENEMY: Gilgamesh
; Original HP: 3000
; New trigger HP: 2280
org $d0c3a5
db $e8, $08

; Enemy: Gilgamesh
; Stats: 
org $D026C0
db $3c, $25, $01, $00, $0e, $00, $07, $00, $B8, $0B, $F3, $19, $B8, $0B, $00, $00, $5C, $00, $F4, $FC, $10, $00, $00, $00, $A0, $98, $0, $0, $01, $0, $36, $43
; Loot: 
org $D054D8
db $00, $C7, $00, $5C
; --------------------------
; Original boss Gilgamesh, Gilgamesh rank 28.0 -> Randomized boss Hole, Hole, Hole, Sandworm, Sandworm, Sandworm rank 12.0
; HP: 30000 -> 3000
; ENEMY: Gilgamesh
; Original HP: 3000
; New trigger HP: 2280
org $d0c3a5
db $e8, $08
; ENEMY: Gilgamesh

; Enemy: Antlion
; Stats: 
org $D02700
db $2a, $54, $0c, $0a, $15, $00, $0b, $0a, $E0, $2E, $31, $04, $E0, $2E, $B8, $0B, $00, $20, $F4, $30, $10, $00, $00, $80, $20, $18, $0, $0, $00, $0, $38, $22
; Loot: 
org $D054E0
db $00, $E1, $00, $F1
; --------------------------
; Original boss Antlion rank 29.0 -> Randomized boss HiryuuPlant, HiryuuFlowr, HiryuuFlowr, HiryuuFlowr, HiryuuFlowr, HiryuuFlowr rank 23.0
; HP: 8100 -> 12000
; ENEMY: Antlion

; Enemy: Halicarnaso
; Stats: 
org $D02980
db $24, $34, $0b, $00, $05, $a2, $0d, $35, $64, $19, $2C, $13, $64, $19, $00, $00, $00, $00, $E4, $78, $10, $00, $00, $00, $20, $18, $0, $0, $00, $0, $4C, $61
; Loot: 
org $D05530
db $86, $3C, $B2, $00
; --------------------------
; Original boss Halicarnaso rank 47.0 -> Randomized boss Gilgamesh rank 20.0
; HP: 33333 -> 6500
; ENEMY: Halicarnaso

; Enemy: Merugene
; Stats: 
org $D02780
db $1e, $16, $08, $06, $1a, $08, $00, $06, $DC, $05, $43, $01, $DC, $05, $00, $00, $00, $F8, $F4, $88, $00, $06, $00, $01, $20, $18, $0, $0, $00, $0, $3C, $1d
; Loot: 
org $D054F0
db $00, $9A, $E5, $00
; --------------------------
; Original boss Merugene, Merugene, Merugene, Merugene rank 34.0 -> Randomized boss Shiva, Commander, Commander, Commander rank 9.0
; HP: 20000 -> 1500
; ENEMY: Merugene
; Skills: ['Fight', 'Fight', 'Bolt', 'Fight', 'Ice', 'Fight', 'Fight', 'NoDamage', 'Bolt', 'NoDamage', 'Ice', 'NoDamage', 'Fight', 'NoDamage', 'Bolt', 'NoDamage', 'Ice', 'NoDamage', 'Ice']
; New skill: Fight
org $d0bac0
db $80
; New skill: Fight
org $d0bac1
db $80
; New skill: Bolt
org $d0bac4
db $26
; New skill: Fight
org $d0bac5
db $80
; New skill: Ice
org $d0bac8
db $25
; New skill: Fight
org $d0bac9
db $80
; New skill: Fight
org $d0bacc
db $80
; New skill: NoDamage
org $d0bacd
db $AC
; New skill: Bolt
org $d0bad0
db $26
; New skill: NoDamage
org $d0bad1
db $AC
; New skill: Ice
org $d0bad4
db $25
; New skill: NoDamage
org $d0bad5
db $AC
; New skill: Fight
org $d0bad8
db $80
; New skill: NoDamage
org $d0bad9
db $AC
; New skill: Bolt
org $d0badc
db $26
; New skill: NoDamage
org $d0badd
db $AC
; New skill: Ice
org $d0bae0
db $25
; New skill: NoDamage
org $d0bae1
db $AC
; New skill: Ice
org $d0baf1
db $25

; Enemy: Merugene
; Stats: 
org $D027A0
db $1e, $16, $08, $06, $1a, $08, $00, $06, $DC, $05, $43, $01, $DC, $05, $00, $00, $00, $F8, $F4, $88, $00, $05, $00, $02, $20, $18, $0, $0, $00, $0, $3C, $1d
; Loot: 
org $D054F4
db $00, $89, $E5, $00
; --------------------------
; Original boss Merugene, Merugene, Merugene, Merugene rank 34.0 -> Randomized boss Shiva, Commander, Commander, Commander rank 9.0
; HP: 20000 -> 1500
; ENEMY: Merugene
; Skills: ['Fight', 'Fight', 'Bolt', 'Fight', 'Ice', 'Fight', 'Fight', 'NoDamage', 'Bolt', 'NoDamage', 'Ice', 'NoDamage', 'Fight', 'NoDamage', 'Bolt', 'NoDamage', 'Ice', 'NoDamage', 'Ice']
; New skill: Fight
org $d0bac0
db $80
; New skill: Fight
org $d0bac1
db $80
; New skill: Bolt
org $d0bac4
db $26
; New skill: Fight
org $d0bac5
db $80
; New skill: Ice
org $d0bac8
db $25
; New skill: Fight
org $d0bac9
db $80
; New skill: Fight
org $d0bacc
db $80
; New skill: NoDamage
org $d0bacd
db $AC
; New skill: Bolt
org $d0bad0
db $26
; New skill: NoDamage
org $d0bad1
db $AC
; New skill: Ice
org $d0bad4
db $25
; New skill: NoDamage
org $d0bad5
db $AC
; New skill: Fight
org $d0bad8
db $80
; New skill: NoDamage
org $d0bad9
db $AC
; New skill: Bolt
org $d0badc
db $26
; New skill: NoDamage
org $d0badd
db $AC
; New skill: Ice
org $d0bae0
db $25
; New skill: NoDamage
org $d0bae1
db $AC
; New skill: Ice
org $d0baf1
db $25
; ENEMY: Merugene
; Skills: ['Fight', 'Fight', 'Bolt', 'Fight', 'Fire', 'Fight', 'Fight', 'NoDamage', 'Bolt', 'NoDamage', 'Fire', 'NoDamage', 'Fight', 'NoDamage', 'Bolt', 'NoDamage', 'Fire', 'NoDamage', 'Bolt']
; New skill: Fight
org $d0baff
db $80
; New skill: Fight
org $d0bb00
db $80
; New skill: Bolt
org $d0bb03
db $26
; New skill: Fight
org $d0bb04
db $80
; New skill: Fire
org $d0bb07
db $24
; New skill: Fight
org $d0bb08
db $80
; New skill: Fight
org $d0bb0b
db $80
; New skill: NoDamage
org $d0bb0c
db $AC
; New skill: Bolt
org $d0bb0f
db $26
; New skill: NoDamage
org $d0bb10
db $AC
; New skill: Fire
org $d0bb13
db $24
; New skill: NoDamage
org $d0bb14
db $AC
; New skill: Fight
org $d0bb17
db $80
; New skill: NoDamage
org $d0bb18
db $AC
; New skill: Bolt
org $d0bb1b
db $26
; New skill: NoDamage
org $d0bb1c
db $AC
; New skill: Fire
org $d0bb1f
db $24
; New skill: NoDamage
org $d0bb20
db $AC
; New skill: Bolt
org $d0bb30
db $26

; Enemy: Merugene
; Stats: 
org $D027C0
db $1e, $16, $08, $06, $1a, $08, $00, $06, $DC, $05, $43, $01, $DC, $05, $00, $00, $00, $F8, $F4, $88, $00, $03, $00, $04, $20, $18, $0, $0, $00, $0, $3C, $1d
; Loot: 
org $D054F8
db $00, $C0, $E5, $00
; --------------------------
; Original boss Merugene, Merugene, Merugene, Merugene rank 34.0 -> Randomized boss Shiva, Commander, Commander, Commander rank 9.0
; HP: 20000 -> 1500
; ENEMY: Merugene
; Skills: ['Fight', 'Fight', 'Bolt', 'Fight', 'Ice', 'Fight', 'Fight', 'NoDamage', 'Bolt', 'NoDamage', 'Ice', 'NoDamage', 'Fight', 'NoDamage', 'Bolt', 'NoDamage', 'Ice', 'NoDamage', 'Ice']
; New skill: Fight
org $d0bac0
db $80
; New skill: Fight
org $d0bac1
db $80
; New skill: Bolt
org $d0bac4
db $26
; New skill: Fight
org $d0bac5
db $80
; New skill: Ice
org $d0bac8
db $25
; New skill: Fight
org $d0bac9
db $80
; New skill: Fight
org $d0bacc
db $80
; New skill: NoDamage
org $d0bacd
db $AC
; New skill: Bolt
org $d0bad0
db $26
; New skill: NoDamage
org $d0bad1
db $AC
; New skill: Ice
org $d0bad4
db $25
; New skill: NoDamage
org $d0bad5
db $AC
; New skill: Fight
org $d0bad8
db $80
; New skill: NoDamage
org $d0bad9
db $AC
; New skill: Bolt
org $d0badc
db $26
; New skill: NoDamage
org $d0badd
db $AC
; New skill: Ice
org $d0bae0
db $25
; New skill: NoDamage
org $d0bae1
db $AC
; New skill: Ice
org $d0baf1
db $25
; ENEMY: Merugene
; Skills: ['Fight', 'Fight', 'Bolt', 'Fight', 'Fire', 'Fight', 'Fight', 'NoDamage', 'Bolt', 'NoDamage', 'Fire', 'NoDamage', 'Fight', 'NoDamage', 'Bolt', 'NoDamage', 'Fire', 'NoDamage', 'Bolt']
; New skill: Fight
org $d0baff
db $80
; New skill: Fight
org $d0bb00
db $80
; New skill: Bolt
org $d0bb03
db $26
; New skill: Fight
org $d0bb04
db $80
; New skill: Fire
org $d0bb07
db $24
; New skill: Fight
org $d0bb08
db $80
; New skill: Fight
org $d0bb0b
db $80
; New skill: NoDamage
org $d0bb0c
db $AC
; New skill: Bolt
org $d0bb0f
db $26
; New skill: NoDamage
org $d0bb10
db $AC
; New skill: Fire
org $d0bb13
db $24
; New skill: NoDamage
org $d0bb14
db $AC
; New skill: Fight
org $d0bb17
db $80
; New skill: NoDamage
org $d0bb18
db $AC
; New skill: Bolt
org $d0bb1b
db $26
; New skill: NoDamage
org $d0bb1c
db $AC
; New skill: Fire
org $d0bb1f
db $24
; New skill: NoDamage
org $d0bb20
db $AC
; New skill: Bolt
org $d0bb30
db $26
; ENEMY: Merugene
; Skills: ['Fight', 'Fight', 'Fire', 'Fight', 'Ice', 'Fight', 'Fight', 'NoDamage', 'Fire', 'NoDamage', 'Ice', 'NoDamage', 'Fight', 'NoDamage', 'Fire', 'NoDamage', 'Ice', 'NoDamage', 'Fire']
; New skill: Fight
org $d0bb3e
db $80
; New skill: Fight
org $d0bb3f
db $80
; New skill: Fire
org $d0bb42
db $24
; New skill: Fight
org $d0bb43
db $80
; New skill: Ice
org $d0bb46
db $25
; New skill: Fight
org $d0bb47
db $80
; New skill: Fight
org $d0bb4a
db $80
; New skill: NoDamage
org $d0bb4b
db $AC
; New skill: Fire
org $d0bb4e
db $24
; New skill: NoDamage
org $d0bb4f
db $AC
; New skill: Ice
org $d0bb52
db $25
; New skill: NoDamage
org $d0bb53
db $AC
; New skill: Fight
org $d0bb56
db $80
; New skill: NoDamage
org $d0bb57
db $AC
; New skill: Fire
org $d0bb5a
db $24
; New skill: NoDamage
org $d0bb5b
db $AC
; New skill: Ice
org $d0bb5e
db $25
; New skill: NoDamage
org $d0bb5f
db $AC
; New skill: Fire
org $d0bb6f
db $24

; Enemy: Merugene
; Stats: 
org $D027E0
db $1e, $16, $08, $00, $00, $00, $1a, $1a, $DC, $05, $43, $01, $DC, $05, $00, $00, $00, $F8, $F4, $88, $00, $07, $40, $00, $20, $18, $0, $0, $00, $0, $3C, $21
; Loot: 
org $D054FC
db $00, $81, $E5, $00
; --------------------------
; Original boss Merugene, Merugene, Merugene, Merugene rank 34.0 -> Randomized boss Shiva, Commander, Commander, Commander rank 9.0
; HP: 20000 -> 1500
; ENEMY: Merugene
; Skills: ['Fight', 'Fight', 'Bolt', 'Fight', 'Ice', 'Fight', 'Fight', 'NoDamage', 'Bolt', 'NoDamage', 'Ice', 'NoDamage', 'Fight', 'NoDamage', 'Bolt', 'NoDamage', 'Ice', 'NoDamage', 'Ice']
; New skill: Fight
org $d0bac0
db $80
; New skill: Fight
org $d0bac1
db $80
; New skill: Bolt
org $d0bac4
db $26
; New skill: Fight
org $d0bac5
db $80
; New skill: Ice
org $d0bac8
db $25
; New skill: Fight
org $d0bac9
db $80
; New skill: Fight
org $d0bacc
db $80
; New skill: NoDamage
org $d0bacd
db $AC
; New skill: Bolt
org $d0bad0
db $26
; New skill: NoDamage
org $d0bad1
db $AC
; New skill: Ice
org $d0bad4
db $25
; New skill: NoDamage
org $d0bad5
db $AC
; New skill: Fight
org $d0bad8
db $80
; New skill: NoDamage
org $d0bad9
db $AC
; New skill: Bolt
org $d0badc
db $26
; New skill: NoDamage
org $d0badd
db $AC
; New skill: Ice
org $d0bae0
db $25
; New skill: NoDamage
org $d0bae1
db $AC
; New skill: Ice
org $d0baf1
db $25
; ENEMY: Merugene
; Skills: ['Fight', 'Fight', 'Bolt', 'Fight', 'Fire', 'Fight', 'Fight', 'NoDamage', 'Bolt', 'NoDamage', 'Fire', 'NoDamage', 'Fight', 'NoDamage', 'Bolt', 'NoDamage', 'Fire', 'NoDamage', 'Bolt']
; New skill: Fight
org $d0baff
db $80
; New skill: Fight
org $d0bb00
db $80
; New skill: Bolt
org $d0bb03
db $26
; New skill: Fight
org $d0bb04
db $80
; New skill: Fire
org $d0bb07
db $24
; New skill: Fight
org $d0bb08
db $80
; New skill: Fight
org $d0bb0b
db $80
; New skill: NoDamage
org $d0bb0c
db $AC
; New skill: Bolt
org $d0bb0f
db $26
; New skill: NoDamage
org $d0bb10
db $AC
; New skill: Fire
org $d0bb13
db $24
; New skill: NoDamage
org $d0bb14
db $AC
; New skill: Fight
org $d0bb17
db $80
; New skill: NoDamage
org $d0bb18
db $AC
; New skill: Bolt
org $d0bb1b
db $26
; New skill: NoDamage
org $d0bb1c
db $AC
; New skill: Fire
org $d0bb1f
db $24
; New skill: NoDamage
org $d0bb20
db $AC
; New skill: Bolt
org $d0bb30
db $26
; ENEMY: Merugene
; Skills: ['Fight', 'Fight', 'Fire', 'Fight', 'Ice', 'Fight', 'Fight', 'NoDamage', 'Fire', 'NoDamage', 'Ice', 'NoDamage', 'Fight', 'NoDamage', 'Fire', 'NoDamage', 'Ice', 'NoDamage', 'Fire']
; New skill: Fight
org $d0bb3e
db $80
; New skill: Fight
org $d0bb3f
db $80
; New skill: Fire
org $d0bb42
db $24
; New skill: Fight
org $d0bb43
db $80
; New skill: Ice
org $d0bb46
db $25
; New skill: Fight
org $d0bb47
db $80
; New skill: Fight
org $d0bb4a
db $80
; New skill: NoDamage
org $d0bb4b
db $AC
; New skill: Fire
org $d0bb4e
db $24
; New skill: NoDamage
org $d0bb4f
db $AC
; New skill: Ice
org $d0bb52
db $25
; New skill: NoDamage
org $d0bb53
db $AC
; New skill: Fight
org $d0bb56
db $80
; New skill: NoDamage
org $d0bb57
db $AC
; New skill: Fire
org $d0bb5a
db $24
; New skill: NoDamage
org $d0bb5b
db $AC
; New skill: Ice
org $d0bb5e
db $25
; New skill: NoDamage
org $d0bb5f
db $AC
; New skill: Fire
org $d0bb6f
db $24
; ENEMY: Merugene
; Skills: ['Fire', 'Nothing', 'Ice', 'Nothing', 'Bolt', 'Nothing', 'Fire', 'NoDamage', 'Ice', 'NoDamage', 'Bolt', 'NoDamage', 'Fire', 'NoDamage', 'Ice', 'NoDamage', 'Bolt', 'NoDamage']
; New skill: Fire
org $d0bb7d
db $24
; New skill: Nothing
org $d0bb7e
db $AA
; New skill: Ice
org $d0bb81
db $25
; New skill: Nothing
org $d0bb82
db $AA
; New skill: Bolt
org $d0bb85
db $26
; New skill: Nothing
org $d0bb86
db $AA
; New skill: Fire
org $d0bb89
db $24
; New skill: NoDamage
org $d0bb8a
db $AC
; New skill: Ice
org $d0bb8d
db $25
; New skill: NoDamage
org $d0bb8e
db $AC
; New skill: Bolt
org $d0bb91
db $26
; New skill: NoDamage
org $d0bb92
db $AC
; New skill: Fire
org $d0bb95
db $24
; New skill: NoDamage
org $d0bb96
db $AC
; New skill: Ice
org $d0bb99
db $25
; New skill: NoDamage
org $d0bb9a
db $AC
; New skill: Bolt
org $d0bb9d
db $26
; New skill: NoDamage
org $d0bb9e
db $AC

; Enemy: Odin
; Stats: 
org $D02800
db $22, $33, $07, $08, $0e, $17, $0e, $2f, $D4, $30, $90, $01, $D4, $30, $00, $00, $2F, $00, $B4, $10, $00, $10, $00, $00, $A0, $18, $0, $0, $00, $0, $40, $02
; Loot: 
org $D05500
db $AF, $00, $C4, $00
; --------------------------
; Original boss Odin rank 36.0 -> Randomized boss Sol Cannon, Launcher, Launcher rank 14.0
; HP: 17000 -> 12500
; ENEMY: Odin
; Skills: ['ReaperSword']
; New skill: ReaperSword
org $d0bbb8
db $B0

; Enemy: Gargoyle
; Stats: 
org $D02820
db $16, $14, $05, $04, $04, $18, $04, $0e, $A9, $01, $93, $00, $A9, $01, $00, $00, $00, $00, $30, $10, $00, $10, $40, $00, $A0, $18, $0, $0, $00, $0, $41, $21
; Loot: 
org $D05504
db $E4, $E0, $E1, $00
; --------------------------
; Original boss Gargoyle, Gargoyle rank 30.0 -> Randomized boss Forza, Magisa rank 4.0
; HP: 5000 -> 850
; ENEMY: Gargoyle
; ENEMY: Gargoyle

; Enemy: Gargoyle
; Stats: 
org $D02820
db $16, $14, $05, $04, $04, $18, $04, $0e, $A9, $01, $93, $00, $A9, $01, $00, $00, $00, $00, $30, $10, $00, $10, $40, $00, $A0, $18, $0, $0, $00, $0, $41, $21
; Loot: 
org $D05504
db $E4, $E0, $E1, $00
; --------------------------
; Original boss Gargoyle, Gargoyle rank 30.0 -> Randomized boss Forza, Magisa rank 4.0
; HP: 5000 -> 850
; ENEMY: Gargoyle
; ENEMY: Gargoyle

; Enemy: Triton
; Stats: 
org $D02840
db $2e, $69, $10, $00, $00, $17, $27, $61, $67, $2B, $77, $46, $67, $2B, $00, $00, $00, $00, $30, $08, $04, $01, $00, $02, $01, $18, $0, $0, $00, $0, $42, $25
; Loot: 
org $D05508
db $E3, $EC, $F5, $00
; --------------------------
; Original boss Triton, Neregeid, Phobos rank 37.0 -> Randomized boss Halicarnaso rank 47.0
; HP: 13333 -> 33333
; ENEMY: Triton
; Skills: ['Fight', 'Fight', 'Fire3', 'Fire3', 'Fight', 'Fight', 'Fight', 'Flare']
; New skill: Fight
org $d0bc05
db $80
; New skill: Fight
org $d0bc06
db $80
; New skill: Fire3
org $d0bc0d
db $30
; New skill: Fire3
org $d0bc0e
db $30
; New skill: Fight
org $d0bc11
db $80
; New skill: Fight
org $d0bc12
db $80
; New skill: Fight
org $d0bc15
db $80
; New skill: Flare
org $d0bc16
db $33

; Enemy: Neregeid
; Stats: 
org $D02860
db $2e, $68, $10, $00, $00, $17, $27, $61, $67, $2B, $77, $46, $67, $2B, $00, $00, $00, $00, $30, $08, $04, $02, $00, $01, $01, $18, $0, $0, $00, $0, $43, $14
; Loot: 
org $D0550C
db $E3, $EC, $F3, $00
; --------------------------
; Original boss Triton, Neregeid, Phobos rank 37.0 -> Randomized boss Halicarnaso rank 47.0
; HP: 13333 -> 33333
; ENEMY: Triton
; Skills: ['Fight', 'Fight', 'Fire3', 'Fire3', 'Fight', 'Fight', 'Fight', 'Flare']
; New skill: Fight
org $d0bc05
db $80
; New skill: Fight
org $d0bc06
db $80
; New skill: Fire3
org $d0bc0d
db $30
; New skill: Fire3
org $d0bc0e
db $30
; New skill: Fight
org $d0bc11
db $80
; New skill: Fight
org $d0bc12
db $80
; New skill: Fight
org $d0bc15
db $80
; New skill: Flare
org $d0bc16
db $33
; ENEMY: Neregeid
; Skills: ['Fight', 'Fight', 'TidalWave', 'Snowstorm', 'Fight', 'Fight', 'Fight', 'Ice3']
; New skill: Fight
org $d0bc30
db $80
; New skill: Fight
org $d0bc31
db $80
; New skill: TidalWave
org $d0bc34
db $D1
; New skill: Snowstorm
org $d0bc35
db $CC
; New skill: Fight
org $d0bc38
db $80
; New skill: Fight
org $d0bc39
db $80
; New skill: Fight
org $d0bc3c
db $80
; New skill: Ice3
org $d0bc3d
db $31

; Enemy: Phobos
; Stats: 
org $D02880
db $2e, $69, $10, $00, $00, $17, $27, $61, $67, $2B, $77, $46, $67, $2B, $00, $00, $00, $00, $30, $08, $04, $08, $00, $20, $01, $18, $0, $0, $00, $0, $44, $27
; Loot: 
org $D05510
db $E3, $EC, $F2, $00
; --------------------------
; Original boss Triton, Neregeid, Phobos rank 37.0 -> Randomized boss Halicarnaso rank 47.0
; HP: 13333 -> 33333
; ENEMY: Triton
; Skills: ['Fight', 'Fight', 'Fire3', 'Fire3', 'Fight', 'Fight', 'Fight', 'Flare']
; New skill: Fight
org $d0bc05
db $80
; New skill: Fight
org $d0bc06
db $80
; New skill: Fire3
org $d0bc0d
db $30
; New skill: Fire3
org $d0bc0e
db $30
; New skill: Fight
org $d0bc11
db $80
; New skill: Fight
org $d0bc12
db $80
; New skill: Fight
org $d0bc15
db $80
; New skill: Flare
org $d0bc16
db $33
; ENEMY: Neregeid
; Skills: ['Fight', 'Fight', 'TidalWave', 'Snowstorm', 'Fight', 'Fight', 'Fight', 'Ice3']
; New skill: Fight
org $d0bc30
db $80
; New skill: Fight
org $d0bc31
db $80
; New skill: TidalWave
org $d0bc34
db $D1
; New skill: Snowstorm
org $d0bc35
db $CC
; New skill: Fight
org $d0bc38
db $80
; New skill: Fight
org $d0bc39
db $80
; New skill: Fight
org $d0bc3c
db $80
; New skill: Ice3
org $d0bc3d
db $31
; ENEMY: Phobos
; Skills: ['Fight', 'Fight', 'Bio', 'Bio', 'Fight', 'Fight', 'Fight', 'Holy']
; New skill: Fight
org $d0bc57
db $80
; New skill: Fight
org $d0bc58
db $80
; New skill: Bio
org $d0bc5f
db $2F
; New skill: Bio
org $d0bc60
db $2F
; New skill: Fight
org $d0bc63
db $80
; New skill: Fight
org $d0bc64
db $80
; New skill: Fight
org $d0bc67
db $80
; New skill: Holy
org $d0bc68
db $22

; Enemy: Omniscient
; Stats: 
org $D028A0
db $1d, $3b, $0d, $00, $00, $0a, $04, $00, $E8, $03, $AA, $44, $E8, $03, $00, $00, $00, $00, $F4, $50, $00, $00, $00, $40, $20, $18, $0, $0, $61, $0, $45, $35
; Loot: 
org $D05514
db $C5, $E0, $00, $00
; --------------------------
; Original boss Omniscient rank 38.0 -> Randomized boss Sergeant, Karnak, Karnak, Karnak, Iron Claw rank 7.0
; HP: 16999 -> 1000
; ENEMY: Omniscient
; Skills: ['Bolt2', 'Fire2', 'Ice2', 'Cure', 'Fire', 'Ice', 'Cure', 'Fire', 'Bolt', 'Ice']
; New skill: Bolt2
org $d0bc72
db $2C
; New skill: Fire2
org $d0bc73
db $2A
; New skill: Ice2
org $d0bc74
db $2B
; New skill: Cure
org $d0bc7c
db $12
; New skill: Fire
org $d0bc7d
db $24
; New skill: Ice
org $d0bc81
db $25
; New skill: Cure
org $d0bc8c
db $12
; New skill: Fire
org $d0bc91
db $24
; New skill: Bolt
org $d0bc94
db $26
; New skill: Ice
org $d0bc95
db $25
; Original HP: 1000
; New trigger HP: 240
org $d0bc6e
db $f0, $00

; Enemy: Minotauros
; Stats: 
org $D028C0
db $2a, $64, $0a, $00, $00, $00, $00, $00, $70, $45, $4D, $00, $70, $45, $00, $00, $00, $B8, $FF, $FF, $FF, $B8, $00, $00, $A0, $18, $0, $0, $00, $0, $46, $25
; Loot: 
org $D05518
db $5B, $C0, $00, $00
; --------------------------
; Original boss Minotauros rank 39.0 -> Randomized boss Gilgamesh, Enkidou rank 24.0
; HP: 19850 -> 17776
; ENEMY: Minotauros

; Enemy: Leviathan
; Stats: 
org $D028E0
db $2e, $4a, $0e, $08, $16, $01, $0e, $43, $98, $3A, $55, $09, $98, $3A, $00, $00, $00, $21, $F4, $F8, $10, $80, $00, $04, $30, $18, $0, $0, $00, $0, $47, $25
; Loot: 
org $D0551C
db $00, $E3, $00, $CA
; --------------------------
; Original boss Leviathan rank 40.0 -> Randomized boss Carbunkle, Carbunkle rank 27.0
; HP: 40000 -> 15000
; ENEMY: Leviathan
; Skills: ['Fight', 'Fight', 'AquaRake', 'Fight', 'Fight', 'AquaRake', 'Fight', 'Specialty', 'AquaRake', 'Fight', 'AquaRake', 'AquaRake', 'Fight', 'Fight', 'AquaRake', 'Fight', 'TidalWave', 'Specialty', 'Fight', 'AquaRake', 'AquaRake', 'AquaRake', 'TidalWave', 'Specialty', 'Specialty', 'Fight', 'TidalWave', 'Fight', 'TidalWave', 'Specialty', 'Fight', 'Fight', 'Specialty', 'Fight', 'Specialty', 'TidalWave', 'Fight', 'Specialty', 'TidalWave', 'TidalWave']
; New skill: Fight
org $d0bcde
db $80
; New skill: Fight
org $d0bcdf
db $80
; New skill: AquaRake
org $d0bce0
db $84
; New skill: Fight
org $d0bce2
db $80
; New skill: Fight
org $d0bce3
db $80
; New skill: AquaRake
org $d0bce4
db $84
; New skill: Fight
org $d0bcea
db $80
; New skill: Specialty
org $d0bceb
db $81
; New skill: AquaRake
org $d0bcec
db $84
; New skill: Fight
org $d0bcee
db $80
; New skill: AquaRake
org $d0bcef
db $84
; New skill: AquaRake
org $d0bcf0
db $84
; New skill: Fight
org $d0bcf2
db $80
; New skill: Fight
org $d0bcf3
db $80
; New skill: AquaRake
org $d0bcf4
db $84
; New skill: Fight
org $d0bcf6
db $80
; New skill: TidalWave
org $d0bcf7
db $D1
; New skill: Specialty
org $d0bcf8
db $81
; New skill: Fight
org $d0bcfa
db $80
; New skill: AquaRake
org $d0bcfb
db $84
; New skill: AquaRake
org $d0bcfc
db $84
; New skill: AquaRake
org $d0bd02
db $84
; New skill: TidalWave
org $d0bd03
db $D1
; New skill: Specialty
org $d0bd04
db $81
; New skill: Specialty
org $d0bd06
db $81
; New skill: Fight
org $d0bd07
db $80
; New skill: TidalWave
org $d0bd08
db $D1
; New skill: Fight
org $d0bd0a
db $80
; New skill: TidalWave
org $d0bd0b
db $D1
; New skill: Specialty
org $d0bd0c
db $81
; New skill: Fight
org $d0bd0e
db $80
; New skill: Fight
org $d0bd0f
db $80
; New skill: Specialty
org $d0bd10
db $81
; New skill: Fight
org $d0bd16
db $80
; New skill: Specialty
org $d0bd17
db $81
; New skill: TidalWave
org $d0bd18
db $D1
; New skill: Fight
org $d0bd1a
db $80
; New skill: Specialty
org $d0bd1b
db $81
; New skill: TidalWave
org $d0bd1c
db $D1
; New skill: TidalWave
org $d0bd24
db $D1

; Enemy: Stalker
; Stats: 
org $D02900
db $2a, $4d, $0a, $00, $08, $08, $13, $08, $10, $27, $2A, $29, $C4, $09, $00, $00, $4F, $20, $F4, $BC, $10, $80, $00, $00, $20, $18, $88, $0, $00, $0, $48, $07
; Loot: 
org $D05520
db $00, $EB, $00, $00
; --------------------------
; Original boss Stalker, Stalker, Stalker, Stalker rank 35.0 -> Randomized boss Gargoyle, Gargoyle rank 30.0
; HP: 20000 -> 10000
; ENEMY: Stalker
; ENEMY: Stalker
; ENEMY: Stalker
; ENEMY: Stalker

; Enemy: Stalker
; Stats: 
org $D02900
db $2a, $4d, $0a, $00, $08, $08, $13, $08, $10, $27, $2A, $29, $C4, $09, $00, $00, $4F, $20, $F4, $BC, $10, $80, $00, $00, $20, $18, $88, $0, $00, $0, $48, $07
; Loot: 
org $D05520
db $00, $EB, $00, $00
; --------------------------
; Original boss Stalker, Stalker, Stalker, Stalker rank 35.0 -> Randomized boss Gargoyle, Gargoyle rank 30.0
; HP: 20000 -> 10000
; ENEMY: Stalker
; ENEMY: Stalker
; ENEMY: Stalker
; ENEMY: Stalker

; Enemy: Stalker
; Stats: 
org $D02900
db $2a, $4d, $0a, $00, $08, $08, $13, $08, $10, $27, $2A, $29, $C4, $09, $00, $00, $4F, $20, $F4, $BC, $10, $80, $00, $00, $20, $18, $88, $0, $00, $0, $48, $07
; Loot: 
org $D05520
db $00, $EB, $00, $00
; --------------------------
; Original boss Stalker, Stalker, Stalker, Stalker rank 35.0 -> Randomized boss Gargoyle, Gargoyle rank 30.0
; HP: 20000 -> 10000
; ENEMY: Stalker
; ENEMY: Stalker
; ENEMY: Stalker
; ENEMY: Stalker

; Enemy: Stalker
; Stats: 
org $D02900
db $2a, $4d, $0a, $00, $08, $08, $13, $08, $10, $27, $2A, $29, $C4, $09, $00, $00, $4F, $20, $F4, $BC, $10, $80, $00, $00, $20, $18, $88, $0, $00, $0, $48, $07
; Loot: 
org $D05520
db $00, $EB, $00, $00
; --------------------------
; Original boss Stalker, Stalker, Stalker, Stalker rank 35.0 -> Randomized boss Gargoyle, Gargoyle rank 30.0
; HP: 20000 -> 10000
; ENEMY: Stalker
; ENEMY: Stalker
; ENEMY: Stalker
; ENEMY: Stalker

; Enemy: Gogo
; Stats: 
org $D02920
db $21, $34, $0d, $0d, $0d, $0f, $08, $2b, $8A, $02, $A3, $65, $8A, $02, $00, $00, $00, $80, $F5, $F8, $10, $00, $00, $80, $A0, $98, $0, $0, $00, $0, $49, $4d
; Loot: 
org $D05524
db $94, $9A, $C3, $00
; --------------------------
; Original boss Gogo rank 41.0 -> Randomized boss Karlabos rank 2.0
; HP: 47714 -> 650
; ENEMY: Gogo
; Original HP: 650
; New trigger HP: 448
org $d0be14
db $c0, $01

; Enemy: Bahamut
; Stats: 
org $D02940
db $30, $70, $14, $05, $0b, $1a, $1a, $2d, $40, $9C, $24, $3E, $40, $9C, $00, $00, $00, $20, $F4, $F8, $00, $00, $60, $00, $20, $18, $88, $0, $00, $0, $4A, $63
; Loot: 
org $D05528
db $EA, $EA, $EA, $00
; --------------------------
; Original boss Bahamut rank 42.0 -> Randomized boss Leviathan rank 40.0
; HP: 40000 -> 40000
; ENEMY: Bahamut
; Skills: ['MegaFlare', 'Flare', 'Fight', 'PoisonBreath', 'DanceoftheDead', 'Fight', 'ZombieBreath', 'DanceoftheDead', 'Fight', 'Maelstrom', 'Maelstrom', 'Fight', 'Snowstorm', 'Snowstorm', 'Fight', 'WindSlash', 'AquaRake', 'Fight', 'Thunder', 'Thunder', 'Fight', 'Flame', 'Flame', 'Fight', 'Quicksand', 'EarthShaker', 'Fight', 'Flame', 'Flame', 'Fight', 'MiniBlaze', 'MiniBlaze', 'Fight', 'MegaFlare', 'Flare', 'Flare']
; New skill: MegaFlare
org $d0be62
db $D2
; New skill: Flare
org $d0be63
db $33
; New skill: Fight
org $d0be64
db $80
; New skill: PoisonBreath
org $d0be6c
db $B6
; New skill: DanceoftheDead
org $d0be6d
db $B7
; New skill: Fight
org $d0be6e
db $80
; New skill: ZombieBreath
org $d0be70
db $B9
; New skill: DanceoftheDead
org $d0be71
db $B7
; New skill: Fight
org $d0be72
db $80
; New skill: Maelstrom
org $d0be7a
db $C2
; New skill: Maelstrom
org $d0be7b
db $C2
; New skill: Fight
org $d0be7c
db $80
; New skill: Snowstorm
org $d0be7e
db $CC
; New skill: Snowstorm
org $d0be7f
db $CC
; New skill: Fight
org $d0be80
db $80
; New skill: WindSlash
org $d0be88
db $AB
; New skill: AquaRake
org $d0be89
db $84
; New skill: Fight
org $d0be8a
db $80
; New skill: Thunder
org $d0be8c
db $DC
; New skill: Thunder
org $d0be8d
db $DC
; New skill: Fight
org $d0be8e
db $80
; New skill: Flame
org $d0be96
db $DB
; New skill: Flame
org $d0be97
db $DB
; New skill: Fight
org $d0be98
db $80
; New skill: Quicksand
org $d0be9a
db $C9
; New skill: EarthShaker
org $d0be9b
db $CF
; New skill: Fight
org $d0be9c
db $80
; New skill: Flame
org $d0bea4
db $DB
; New skill: Flame
org $d0bea5
db $DB
; New skill: Fight
org $d0bea6
db $80
; New skill: MiniBlaze
org $d0bea8
db $CB
; New skill: MiniBlaze
org $d0bea9
db $CB
; New skill: Fight
org $d0beaa
db $80
; New skill: MegaFlare
org $d0beb3
db $D2
; New skill: Flare
org $d0bebb
db $33
; New skill: Flare
org $d0bebe
db $33
; Original HP: 40000
; New trigger HP: 10000
org $d0be5e
db $10, $27
; Original HP: 40000
; New trigger HP: 15200
org $d0be68
db $60, $3b
; Original HP: 40000
; New trigger HP: 20000
org $d0be76
db $20, $4e
; Original HP: 40000
; New trigger HP: 25200
org $d0be84
db $70, $62
; Original HP: 40000
; New trigger HP: 30000
org $d0be92
db $30, $75
; Original HP: 40000
; New trigger HP: 34800
org $d0bea0
db $f0, $87
; Original HP: 40000
; New trigger HP: 10000
org $d0beb7
db $10, $27

; Enemy: Ifrit
; Stats: 
org $D006A0
db $22, $44, $07, $0e, $09, $11, $0c, $05, $C4, $09, $99, $03, $C4, $09, $00, $00, $00, $08, $30, $40, $00, $01, $00, $82, $20, $18, $0, $0, $00, $0, $35, $16
; Loot: 
org $D050D4
db $00, $E4, $00, $FC
; --------------------------
; Original boss Ifrit rank 8.0 -> Randomized boss Titan rank 18.0
; HP: 3000 -> 2500
; ENEMY: Ifrit
; Skills: ['Flame', 'Fire2', 'Fire2', 'Flame', 'Fight', 'Specialty']
; New skill: Flame
org $d0a2fb
db $DB
; New skill: Fire2
org $d0a2fc
db $2A
; New skill: Fire2
org $d0a2fd
db $2A
; New skill: Flame
org $d0a2ff
db $DB
; New skill: Fight
org $d0a300
db $80
; New skill: Specialty
org $d0a301
db $81

; Enemy: Shiva
; Stats: 
org $D024A0
db $11, $14, $05, $00, $00, $05, $05, $08, $B0, $04, $0D, $02, $B0, $04, $00, $00, $00, $00, $FA, $FF, $10, $02, $00, $01, $A0, $18, $0, $0, $00, $0, $25, $0b
; Loot: 
org $D05494
db $E4, $E1, $00, $33
; --------------------------
; Original boss Shiva, Commander, Commander, Commander rank 9.0 -> Randomized boss Galura rank 5.0
; HP: 1500 -> 1200
; ENEMY: Shiva
; Skills: ['Ice', 'Ice']
; New skill: Ice
org $d0b6c0
db $25
; New skill: Ice
org $d0b6c5
db $25

; Enemy: Commander
; Stats: 
org $D02180
db $10, $11, $05, $05, $00, $05, $00, $00, $E0, $01, $69, $00, $00, $00, $00, $00, $00, $00, $10, $00, $00, $02, $00, $01, $80, $18, $0, $0, $00, $0, $0C, $04
; Loot: 
org $D05430
db $00, $0F, $0E, $00
; --------------------------
; Original boss Shiva, Commander, Commander, Commander rank 9.0 -> Randomized boss Galura rank 5.0
; HP: 1500 -> 1200
; ENEMY: Shiva
; Skills: ['Ice', 'Ice']
; New skill: Ice
org $d0b6c0
db $25
; New skill: Ice
org $d0b6c5
db $25
; ENEMY: Commander
; ENEMY: Commander
; ENEMY: Commander

; Enemy: Commander
; Stats: 
org $D02180
db $10, $11, $05, $05, $00, $05, $00, $00, $E0, $01, $69, $00, $00, $00, $00, $00, $00, $00, $10, $00, $00, $02, $00, $01, $80, $18, $0, $0, $00, $0, $0C, $04
; Loot: 
org $D05430
db $00, $0F, $0E, $00
; --------------------------
; Original boss Shiva, Commander, Commander, Commander rank 9.0 -> Randomized boss Galura rank 5.0
; HP: 1500 -> 1200
; ENEMY: Shiva
; Skills: ['Ice', 'Ice']
; New skill: Ice
org $d0b6c0
db $25
; New skill: Ice
org $d0b6c5
db $25
; ENEMY: Commander
; ENEMY: Commander
; ENEMY: Commander

; Enemy: Commander
; Stats: 
org $D02180
db $10, $11, $05, $05, $00, $05, $00, $00, $E0, $01, $69, $00, $00, $00, $00, $00, $00, $00, $10, $00, $00, $02, $00, $01, $80, $18, $0, $0, $00, $0, $0C, $04
; Loot: 
org $D05430
db $00, $0F, $0E, $00
; --------------------------
; Original boss Shiva, Commander, Commander, Commander rank 9.0 -> Randomized boss Galura rank 5.0
; HP: 1500 -> 1200
; ENEMY: Shiva
; Skills: ['Ice', 'Ice']
; New skill: Ice
org $d0b6c0
db $25
; New skill: Ice
org $d0b6c5
db $25
; ENEMY: Commander
; ENEMY: Commander
; ENEMY: Commander

; Enemy: Calofisteri
; Stats: 
org $D02AC0
db $33, $5f, $13, $0b, $43, $26, $28, $0b, $40, $9C, $74, $06, $40, $9C, $00, $00, $3D, $00, $F0, $78, $10, $00, $20, $00, $A4, $18, $0, $0, $00, $0, $56, $44
; Loot: 
org $D05558
db $CA, $90, $A5, $00
; --------------------------
; Original boss Calofisteri rank 43.0 -> Randomized boss Bahamut rank 42.0
; HP: 18000 -> 40000
; ENEMY: Calofisteri

; Enemy: Apocalypse
; Stats: 
org $D02AE0
db $1e, $0c, $0c, $01, $05, $04, $0e, $0b, $84, $03, $A6, $5A, $84, $03, $00, $00, $2D, $00, $F4, $FC, $14, $00, $00, $08, $20, $18, $0, $0, $00, $0, $57, $39
; Loot: 
org $D0555C
db $B1, $E3, $98, $00
; --------------------------
; Original boss Apocalypse rank 45.0 -> Randomized boss Siren, Siren rank 3.0
; HP: 27900 -> 900
; ENEMY: Apocalypse
; Skills: ['Aero', 'Aero', 'Aero', 'Aero', 'Aero', 'Aero', 'Aero', 'Aero', 'Aero', 'Aero', 'Aero', 'Aero', 'Aero', 'Aero']
; New skill: Aero
org $d0c0d5
db $8F
; New skill: Aero
org $d0c0d6
db $8F
; New skill: Aero
org $d0c0d7
db $8F
; New skill: Aero
org $d0c0d9
db $8F
; New skill: Aero
org $d0c0da
db $8F
; New skill: Aero
org $d0c0db
db $8F
; New skill: Aero
org $d0c0dd
db $8F
; New skill: Aero
org $d0c0de
db $8F
; New skill: Aero
org $d0c0df
db $8F
; New skill: Aero
org $d0c0e5
db $8F
; New skill: Aero
org $d0c0e6
db $8F
; New skill: Aero
org $d0c0e7
db $8F
; New skill: Aero
org $d0c11d
db $8F
; New skill: Aero
org $d0c15d
db $8F

; Enemy: Catastroph
; Stats: 
org $D02B00
db $34, $5c, $17, $1a, $35, $1b, $1b, $2c, $B8, $56, $C6, $85, $B8, $56, $00, $00, $00, $00, $F4, $5C, $10, $20, $00, $00, $20, $18, $0, $0, $00, $0, $58, $47
; Loot: 
org $D05560
db $F1, $E3, $00, $EC
; --------------------------
; Original boss Catastroph rank 46.0 -> Randomized boss Apanda rank 44.0
; HP: 19997 -> 22200
; ENEMY: Catastroph
; Skills: ['EarthShaker', 'DemonEye', 'DemonEye', 'Fight', 'Quake', 'Specialty']
; New skill: EarthShaker
org $d0c1e0
db $CF
; New skill: DemonEye
org $d0c1e1
db $EB
; New skill: DemonEye
org $d0c1e2
db $EB
; New skill: Fight
org $d0c1e4
db $80
; New skill: Quake
org $d0c1e5
db $D6
; New skill: Specialty
org $d0c1e6
db $81

; Enemy: Necrofobia
; Stats: 
org $D02B20
db $18, $1f, $0a, $02, $0f, $0e, $0f, $1e, $B8, $0B, $14, $18, $B8, $0B, $00, $00, $1E, $00, $F4, $F8, $10, $00, $00, $FF, $20, $18, $0, $0, $02, $0, $59, $42
; Loot: 
org $D05564
db $B0, $E3, $AB, $00
; --------------------------
; Original boss Necrofobia, Barrier, Barrier, Barrier, Barrier, Gilgamesh rank 49.0 -> Randomized boss Ifrit rank 8.0
; HP: 44044 -> 3000
; ENEMY: Necrofobia
; Skills: ['Flare', 'Fire', 'Bolt', 'Ice']
; New skill: Flare
org $d0c1fe
db $33
; New skill: Fire
org $d0c21b
db $24
; New skill: Bolt
org $d0c21c
db $26
; New skill: Ice
org $d0c222
db $25

; Enemy: Barrier
; Stats: 
org $D02D40
db $01, $1e, $06, $00, $09, $00, $02, $02, $58, $02, $B8, $00, $00, $00, $00, $00, $00, $20, $3F, $FB, $00, $00, $00, $00, $20, $98, $80, $0, $80, $0, $6A, $2c
; Loot: 
org $D055A8
db $CA, $E1, $00, $00
; --------------------------
; Original boss Necrofobia, Barrier, Barrier, Barrier, Barrier, Gilgamesh rank 49.0 -> Randomized boss Ifrit rank 8.0
; HP: 44044 -> 3000
; ENEMY: Necrofobia
; Skills: ['Flare', 'Fire', 'Bolt', 'Ice']
; New skill: Flare
org $d0c1fe
db $33
; New skill: Fire
org $d0c21b
db $24
; New skill: Bolt
org $d0c21c
db $26
; New skill: Ice
org $d0c222
db $25
; ENEMY: Barrier
; Skills: ['Fire', 'Ice', 'Bolt', 'Fire', 'Ice', 'Bolt', 'Fire', 'Ice', 'Bolt', 'Fire', 'Ice', 'Bolt']
; New skill: Fire
org $d0c581
db $24
; New skill: Ice
org $d0c582
db $25
; New skill: Bolt
org $d0c583
db $26
; New skill: Fire
org $d0c589
db $24
; New skill: Ice
org $d0c58a
db $25
; New skill: Bolt
org $d0c58b
db $26
; New skill: Fire
org $d0c591
db $24
; New skill: Ice
org $d0c592
db $25
; New skill: Bolt
org $d0c593
db $26
; New skill: Fire
org $d0c599
db $24
; New skill: Ice
org $d0c59a
db $25
; New skill: Bolt
org $d0c59b
db $26
; ENEMY: Barrier
; Skills: ['Fire', 'Ice', 'Bolt', 'Fire', 'Ice', 'Bolt', 'Fire', 'Ice', 'Bolt', 'Fire', 'Ice', 'Bolt']
; New skill: Fire
org $d0c581
db $24
; New skill: Ice
org $d0c582
db $25
; New skill: Bolt
org $d0c583
db $26
; New skill: Fire
org $d0c589
db $24
; New skill: Ice
org $d0c58a
db $25
; New skill: Bolt
org $d0c58b
db $26
; New skill: Fire
org $d0c591
db $24
; New skill: Ice
org $d0c592
db $25
; New skill: Bolt
org $d0c593
db $26
; New skill: Fire
org $d0c599
db $24
; New skill: Ice
org $d0c59a
db $25
; New skill: Bolt
org $d0c59b
db $26
; ENEMY: Barrier
; Skills: ['Fire', 'Ice', 'Bolt', 'Fire', 'Ice', 'Bolt', 'Fire', 'Ice', 'Bolt', 'Fire', 'Ice', 'Bolt']
; New skill: Fire
org $d0c581
db $24
; New skill: Ice
org $d0c582
db $25
; New skill: Bolt
org $d0c583
db $26
; New skill: Fire
org $d0c589
db $24
; New skill: Ice
org $d0c58a
db $25
; New skill: Bolt
org $d0c58b
db $26
; New skill: Fire
org $d0c591
db $24
; New skill: Ice
org $d0c592
db $25
; New skill: Bolt
org $d0c593
db $26
; New skill: Fire
org $d0c599
db $24
; New skill: Ice
org $d0c59a
db $25
; New skill: Bolt
org $d0c59b
db $26
; ENEMY: Barrier
; Skills: ['Fire', 'Ice', 'Bolt', 'Fire', 'Ice', 'Bolt', 'Fire', 'Ice', 'Bolt', 'Fire', 'Ice', 'Bolt']
; New skill: Fire
org $d0c581
db $24
; New skill: Ice
org $d0c582
db $25
; New skill: Bolt
org $d0c583
db $26
; New skill: Fire
org $d0c589
db $24
; New skill: Ice
org $d0c58a
db $25
; New skill: Bolt
org $d0c58b
db $26
; New skill: Fire
org $d0c591
db $24
; New skill: Ice
org $d0c592
db $25
; New skill: Bolt
org $d0c593
db $26
; New skill: Fire
org $d0c599
db $24
; New skill: Ice
org $d0c59a
db $25
; New skill: Bolt
org $d0c59b
db $26

; Enemy: Barrier
; Stats: 
org $D02D40
db $01, $1e, $06, $00, $09, $00, $02, $02, $58, $02, $B8, $00, $00, $00, $00, $00, $00, $20, $3F, $FB, $00, $00, $00, $00, $20, $98, $80, $0, $80, $0, $6A, $2c
; Loot: 
org $D055A8
db $CA, $E1, $00, $00
; --------------------------
; Original boss Necrofobia, Barrier, Barrier, Barrier, Barrier, Gilgamesh rank 49.0 -> Randomized boss Ifrit rank 8.0
; HP: 44044 -> 3000
; ENEMY: Necrofobia
; Skills: ['Flare', 'Fire', 'Bolt', 'Ice']
; New skill: Flare
org $d0c1fe
db $33
; New skill: Fire
org $d0c21b
db $24
; New skill: Bolt
org $d0c21c
db $26
; New skill: Ice
org $d0c222
db $25
; ENEMY: Barrier
; Skills: ['Fire', 'Ice', 'Bolt', 'Fire', 'Ice', 'Bolt', 'Fire', 'Ice', 'Bolt', 'Fire', 'Ice', 'Bolt']
; New skill: Fire
org $d0c581
db $24
; New skill: Ice
org $d0c582
db $25
; New skill: Bolt
org $d0c583
db $26
; New skill: Fire
org $d0c589
db $24
; New skill: Ice
org $d0c58a
db $25
; New skill: Bolt
org $d0c58b
db $26
; New skill: Fire
org $d0c591
db $24
; New skill: Ice
org $d0c592
db $25
; New skill: Bolt
org $d0c593
db $26
; New skill: Fire
org $d0c599
db $24
; New skill: Ice
org $d0c59a
db $25
; New skill: Bolt
org $d0c59b
db $26
; ENEMY: Barrier
; Skills: ['Fire', 'Ice', 'Bolt', 'Fire', 'Ice', 'Bolt', 'Fire', 'Ice', 'Bolt', 'Fire', 'Ice', 'Bolt']
; New skill: Fire
org $d0c581
db $24
; New skill: Ice
org $d0c582
db $25
; New skill: Bolt
org $d0c583
db $26
; New skill: Fire
org $d0c589
db $24
; New skill: Ice
org $d0c58a
db $25
; New skill: Bolt
org $d0c58b
db $26
; New skill: Fire
org $d0c591
db $24
; New skill: Ice
org $d0c592
db $25
; New skill: Bolt
org $d0c593
db $26
; New skill: Fire
org $d0c599
db $24
; New skill: Ice
org $d0c59a
db $25
; New skill: Bolt
org $d0c59b
db $26
; ENEMY: Barrier
; Skills: ['Fire', 'Ice', 'Bolt', 'Fire', 'Ice', 'Bolt', 'Fire', 'Ice', 'Bolt', 'Fire', 'Ice', 'Bolt']
; New skill: Fire
org $d0c581
db $24
; New skill: Ice
org $d0c582
db $25
; New skill: Bolt
org $d0c583
db $26
; New skill: Fire
org $d0c589
db $24
; New skill: Ice
org $d0c58a
db $25
; New skill: Bolt
org $d0c58b
db $26
; New skill: Fire
org $d0c591
db $24
; New skill: Ice
org $d0c592
db $25
; New skill: Bolt
org $d0c593
db $26
; New skill: Fire
org $d0c599
db $24
; New skill: Ice
org $d0c59a
db $25
; New skill: Bolt
org $d0c59b
db $26
; ENEMY: Barrier
; Skills: ['Fire', 'Ice', 'Bolt', 'Fire', 'Ice', 'Bolt', 'Fire', 'Ice', 'Bolt', 'Fire', 'Ice', 'Bolt']
; New skill: Fire
org $d0c581
db $24
; New skill: Ice
org $d0c582
db $25
; New skill: Bolt
org $d0c583
db $26
; New skill: Fire
org $d0c589
db $24
; New skill: Ice
org $d0c58a
db $25
; New skill: Bolt
org $d0c58b
db $26
; New skill: Fire
org $d0c591
db $24
; New skill: Ice
org $d0c592
db $25
; New skill: Bolt
org $d0c593
db $26
; New skill: Fire
org $d0c599
db $24
; New skill: Ice
org $d0c59a
db $25
; New skill: Bolt
org $d0c59b
db $26

; Enemy: Barrier
; Stats: 
org $D02D40
db $01, $1e, $06, $00, $09, $00, $02, $02, $58, $02, $B8, $00, $00, $00, $00, $00, $00, $20, $3F, $FB, $00, $00, $00, $00, $20, $98, $80, $0, $80, $0, $6A, $2c
; Loot: 
org $D055A8
db $CA, $E1, $00, $00
; --------------------------
; Original boss Necrofobia, Barrier, Barrier, Barrier, Barrier, Gilgamesh rank 49.0 -> Randomized boss Ifrit rank 8.0
; HP: 44044 -> 3000
; ENEMY: Necrofobia
; Skills: ['Flare', 'Fire', 'Bolt', 'Ice']
; New skill: Flare
org $d0c1fe
db $33
; New skill: Fire
org $d0c21b
db $24
; New skill: Bolt
org $d0c21c
db $26
; New skill: Ice
org $d0c222
db $25
; ENEMY: Barrier
; Skills: ['Fire', 'Ice', 'Bolt', 'Fire', 'Ice', 'Bolt', 'Fire', 'Ice', 'Bolt', 'Fire', 'Ice', 'Bolt']
; New skill: Fire
org $d0c581
db $24
; New skill: Ice
org $d0c582
db $25
; New skill: Bolt
org $d0c583
db $26
; New skill: Fire
org $d0c589
db $24
; New skill: Ice
org $d0c58a
db $25
; New skill: Bolt
org $d0c58b
db $26
; New skill: Fire
org $d0c591
db $24
; New skill: Ice
org $d0c592
db $25
; New skill: Bolt
org $d0c593
db $26
; New skill: Fire
org $d0c599
db $24
; New skill: Ice
org $d0c59a
db $25
; New skill: Bolt
org $d0c59b
db $26
; ENEMY: Barrier
; Skills: ['Fire', 'Ice', 'Bolt', 'Fire', 'Ice', 'Bolt', 'Fire', 'Ice', 'Bolt', 'Fire', 'Ice', 'Bolt']
; New skill: Fire
org $d0c581
db $24
; New skill: Ice
org $d0c582
db $25
; New skill: Bolt
org $d0c583
db $26
; New skill: Fire
org $d0c589
db $24
; New skill: Ice
org $d0c58a
db $25
; New skill: Bolt
org $d0c58b
db $26
; New skill: Fire
org $d0c591
db $24
; New skill: Ice
org $d0c592
db $25
; New skill: Bolt
org $d0c593
db $26
; New skill: Fire
org $d0c599
db $24
; New skill: Ice
org $d0c59a
db $25
; New skill: Bolt
org $d0c59b
db $26
; ENEMY: Barrier
; Skills: ['Fire', 'Ice', 'Bolt', 'Fire', 'Ice', 'Bolt', 'Fire', 'Ice', 'Bolt', 'Fire', 'Ice', 'Bolt']
; New skill: Fire
org $d0c581
db $24
; New skill: Ice
org $d0c582
db $25
; New skill: Bolt
org $d0c583
db $26
; New skill: Fire
org $d0c589
db $24
; New skill: Ice
org $d0c58a
db $25
; New skill: Bolt
org $d0c58b
db $26
; New skill: Fire
org $d0c591
db $24
; New skill: Ice
org $d0c592
db $25
; New skill: Bolt
org $d0c593
db $26
; New skill: Fire
org $d0c599
db $24
; New skill: Ice
org $d0c59a
db $25
; New skill: Bolt
org $d0c59b
db $26
; ENEMY: Barrier
; Skills: ['Fire', 'Ice', 'Bolt', 'Fire', 'Ice', 'Bolt', 'Fire', 'Ice', 'Bolt', 'Fire', 'Ice', 'Bolt']
; New skill: Fire
org $d0c581
db $24
; New skill: Ice
org $d0c582
db $25
; New skill: Bolt
org $d0c583
db $26
; New skill: Fire
org $d0c589
db $24
; New skill: Ice
org $d0c58a
db $25
; New skill: Bolt
org $d0c58b
db $26
; New skill: Fire
org $d0c591
db $24
; New skill: Ice
org $d0c592
db $25
; New skill: Bolt
org $d0c593
db $26
; New skill: Fire
org $d0c599
db $24
; New skill: Ice
org $d0c59a
db $25
; New skill: Bolt
org $d0c59b
db $26

; Enemy: Barrier
; Stats: 
org $D02D40
db $01, $1e, $06, $00, $09, $00, $02, $02, $58, $02, $B8, $00, $00, $00, $00, $00, $00, $20, $3F, $FB, $00, $00, $00, $00, $20, $98, $80, $0, $80, $0, $6A, $2c
; Loot: 
org $D055A8
db $CA, $E1, $00, $00
; --------------------------
; Original boss Necrofobia, Barrier, Barrier, Barrier, Barrier, Gilgamesh rank 49.0 -> Randomized boss Ifrit rank 8.0
; HP: 44044 -> 3000
; ENEMY: Necrofobia
; Skills: ['Flare', 'Fire', 'Bolt', 'Ice']
; New skill: Flare
org $d0c1fe
db $33
; New skill: Fire
org $d0c21b
db $24
; New skill: Bolt
org $d0c21c
db $26
; New skill: Ice
org $d0c222
db $25
; ENEMY: Barrier
; Skills: ['Fire', 'Ice', 'Bolt', 'Fire', 'Ice', 'Bolt', 'Fire', 'Ice', 'Bolt', 'Fire', 'Ice', 'Bolt']
; New skill: Fire
org $d0c581
db $24
; New skill: Ice
org $d0c582
db $25
; New skill: Bolt
org $d0c583
db $26
; New skill: Fire
org $d0c589
db $24
; New skill: Ice
org $d0c58a
db $25
; New skill: Bolt
org $d0c58b
db $26
; New skill: Fire
org $d0c591
db $24
; New skill: Ice
org $d0c592
db $25
; New skill: Bolt
org $d0c593
db $26
; New skill: Fire
org $d0c599
db $24
; New skill: Ice
org $d0c59a
db $25
; New skill: Bolt
org $d0c59b
db $26
; ENEMY: Barrier
; Skills: ['Fire', 'Ice', 'Bolt', 'Fire', 'Ice', 'Bolt', 'Fire', 'Ice', 'Bolt', 'Fire', 'Ice', 'Bolt']
; New skill: Fire
org $d0c581
db $24
; New skill: Ice
org $d0c582
db $25
; New skill: Bolt
org $d0c583
db $26
; New skill: Fire
org $d0c589
db $24
; New skill: Ice
org $d0c58a
db $25
; New skill: Bolt
org $d0c58b
db $26
; New skill: Fire
org $d0c591
db $24
; New skill: Ice
org $d0c592
db $25
; New skill: Bolt
org $d0c593
db $26
; New skill: Fire
org $d0c599
db $24
; New skill: Ice
org $d0c59a
db $25
; New skill: Bolt
org $d0c59b
db $26
; ENEMY: Barrier
; Skills: ['Fire', 'Ice', 'Bolt', 'Fire', 'Ice', 'Bolt', 'Fire', 'Ice', 'Bolt', 'Fire', 'Ice', 'Bolt']
; New skill: Fire
org $d0c581
db $24
; New skill: Ice
org $d0c582
db $25
; New skill: Bolt
org $d0c583
db $26
; New skill: Fire
org $d0c589
db $24
; New skill: Ice
org $d0c58a
db $25
; New skill: Bolt
org $d0c58b
db $26
; New skill: Fire
org $d0c591
db $24
; New skill: Ice
org $d0c592
db $25
; New skill: Bolt
org $d0c593
db $26
; New skill: Fire
org $d0c599
db $24
; New skill: Ice
org $d0c59a
db $25
; New skill: Bolt
org $d0c59b
db $26
; ENEMY: Barrier
; Skills: ['Fire', 'Ice', 'Bolt', 'Fire', 'Ice', 'Bolt', 'Fire', 'Ice', 'Bolt', 'Fire', 'Ice', 'Bolt']
; New skill: Fire
org $d0c581
db $24
; New skill: Ice
org $d0c582
db $25
; New skill: Bolt
org $d0c583
db $26
; New skill: Fire
org $d0c589
db $24
; New skill: Ice
org $d0c58a
db $25
; New skill: Bolt
org $d0c58b
db $26
; New skill: Fire
org $d0c591
db $24
; New skill: Ice
org $d0c592
db $25
; New skill: Bolt
org $d0c593
db $26
; New skill: Fire
org $d0c599
db $24
; New skill: Ice
org $d0c59a
db $25
; New skill: Bolt
org $d0c59b
db $26

; Enemy: Gilgamesh
; Stats: 
org $D02DE0
db $41, $46, $10, $12, $15, $00, $00, $00, $30, $75, $AA, $15, $00, $00, $00, $00, $00, $00, $FF, $FF, $FF, $00, $00, $00, $A0, $98, $0, $0, $00, $0, $6F, $5d
; Loot: 
org $D055BC
db $00, $C8, $00, $00
; --------------------------
; Original boss Necrofobia, Barrier, Barrier, Barrier, Barrier, Gilgamesh rank 49.0 -> Randomized boss Ifrit rank 8.0
; HP: 44044 -> 3000
; ENEMY: Necrofobia
; Skills: ['Flare', 'Fire', 'Bolt', 'Ice']
; New skill: Flare
org $d0c1fe
db $33
; New skill: Fire
org $d0c21b
db $24
; New skill: Bolt
org $d0c21c
db $26
; New skill: Ice
org $d0c222
db $25
; ENEMY: Barrier
; Skills: ['Fire', 'Ice', 'Bolt', 'Fire', 'Ice', 'Bolt', 'Fire', 'Ice', 'Bolt', 'Fire', 'Ice', 'Bolt']
; New skill: Fire
org $d0c581
db $24
; New skill: Ice
org $d0c582
db $25
; New skill: Bolt
org $d0c583
db $26
; New skill: Fire
org $d0c589
db $24
; New skill: Ice
org $d0c58a
db $25
; New skill: Bolt
org $d0c58b
db $26
; New skill: Fire
org $d0c591
db $24
; New skill: Ice
org $d0c592
db $25
; New skill: Bolt
org $d0c593
db $26
; New skill: Fire
org $d0c599
db $24
; New skill: Ice
org $d0c59a
db $25
; New skill: Bolt
org $d0c59b
db $26
; ENEMY: Barrier
; Skills: ['Fire', 'Ice', 'Bolt', 'Fire', 'Ice', 'Bolt', 'Fire', 'Ice', 'Bolt', 'Fire', 'Ice', 'Bolt']
; New skill: Fire
org $d0c581
db $24
; New skill: Ice
org $d0c582
db $25
; New skill: Bolt
org $d0c583
db $26
; New skill: Fire
org $d0c589
db $24
; New skill: Ice
org $d0c58a
db $25
; New skill: Bolt
org $d0c58b
db $26
; New skill: Fire
org $d0c591
db $24
; New skill: Ice
org $d0c592
db $25
; New skill: Bolt
org $d0c593
db $26
; New skill: Fire
org $d0c599
db $24
; New skill: Ice
org $d0c59a
db $25
; New skill: Bolt
org $d0c59b
db $26
; ENEMY: Barrier
; Skills: ['Fire', 'Ice', 'Bolt', 'Fire', 'Ice', 'Bolt', 'Fire', 'Ice', 'Bolt', 'Fire', 'Ice', 'Bolt']
; New skill: Fire
org $d0c581
db $24
; New skill: Ice
org $d0c582
db $25
; New skill: Bolt
org $d0c583
db $26
; New skill: Fire
org $d0c589
db $24
; New skill: Ice
org $d0c58a
db $25
; New skill: Bolt
org $d0c58b
db $26
; New skill: Fire
org $d0c591
db $24
; New skill: Ice
org $d0c592
db $25
; New skill: Bolt
org $d0c593
db $26
; New skill: Fire
org $d0c599
db $24
; New skill: Ice
org $d0c59a
db $25
; New skill: Bolt
org $d0c59b
db $26
; ENEMY: Barrier
; Skills: ['Fire', 'Ice', 'Bolt', 'Fire', 'Ice', 'Bolt', 'Fire', 'Ice', 'Bolt', 'Fire', 'Ice', 'Bolt']
; New skill: Fire
org $d0c581
db $24
; New skill: Ice
org $d0c582
db $25
; New skill: Bolt
org $d0c583
db $26
; New skill: Fire
org $d0c589
db $24
; New skill: Ice
org $d0c58a
db $25
; New skill: Bolt
org $d0c58b
db $26
; New skill: Fire
org $d0c591
db $24
; New skill: Ice
org $d0c592
db $25
; New skill: Bolt
org $d0c593
db $26
; New skill: Fire
org $d0c599
db $24
; New skill: Ice
org $d0c59a
db $25
; New skill: Bolt
org $d0c59b
db $26
; ENEMY: Gilgamesh

; Enemy: Twin Tania
; Stats: 
org $D02B40
db $25, $6a, $11, $00, $22, $06, $12, $0a, $3F, $9C, $92, $3A, $3F, $9C, $00, $00, $00, $00, $F4, $F8, $10, $00, $00, $90, $24, $18, $0, $0, $00, $0, $5A, $27
; Loot: 
org $D05568
db $C4, $E4, $53, $00
; --------------------------
; Original boss Twin Tania, Twin Tania rank 48.0 -> Randomized boss Triton, Neregeid, Phobos rank 37.0
; HP: 50000 -> 39999
; ENEMY: Twin Tania
; Skills: ['MiniBlaze', 'Blaze', 'Fight', 'MiniBlaze', 'Blaze', 'Fight', 'MindBlast', 'WindSlash', 'BreathWing', 'TidalWave', 'Flare']
; New skill: MiniBlaze
org $d0c2f6
db $CB
; New skill: Blaze
org $d0c2f7
db $CD
; New skill: Fight
org $d0c2f8
db $80
; New skill: MiniBlaze
org $d0c2fa
db $CB
; New skill: Blaze
org $d0c2fb
db $CD
; New skill: Fight
org $d0c2fc
db $80
; New skill: MindBlast
org $d0c301
db $97
; New skill: WindSlash
org $d0c302
db $AB
; New skill: BreathWing
org $d0c303
db $DA
; New skill: TidalWave
org $d0c310
db $D1
; New skill: Flare
org $d0c31a
db $33

; Enemy: Twin Tania
; Stats: 
org $D02060
db $5f, $6a, $11, $00, $00, $52, $00, $00, $3F, $9C, $92, $3A, $3F, $9C, $00, $00, $00, $00, $14, $F8, $00, $00, $00, $90, $04, $18, $0, $0, $00, $0, $03, $1e
; Loot: 
org $D0540C
db $00, $6A, $2E, $00
; --------------------------
; Original boss Twin Tania, Twin Tania rank 48.0 -> Randomized boss Triton, Neregeid, Phobos rank 37.0
; HP: 50000 -> 39999
; ENEMY: Twin Tania
; Skills: ['MiniBlaze', 'Blaze', 'Fight', 'MiniBlaze', 'Blaze', 'Fight', 'MindBlast', 'WindSlash', 'BreathWing', 'TidalWave', 'Flare']
; New skill: MiniBlaze
org $d0c2f6
db $CB
; New skill: Blaze
org $d0c2f7
db $CD
; New skill: Fight
org $d0c2f8
db $80
; New skill: MiniBlaze
org $d0c2fa
db $CB
; New skill: Blaze
org $d0c2fb
db $CD
; New skill: Fight
org $d0c2fc
db $80
; New skill: MindBlast
org $d0c301
db $97
; New skill: WindSlash
org $d0c302
db $AB
; New skill: BreathWing
org $d0c303
db $DA
; New skill: TidalWave
org $d0c310
db $D1
; New skill: Flare
org $d0c31a
db $33
; ENEMY: Twin Tania
; Skills: ['MegaFlare']
; New skill: MegaFlare
org $d0b2d8
db $D2

; Enemy: Apanda
; Stats: 
org $D02C00
db $2d, $4a, $13, $14, $16, $31, $08, $1d, $10, $27, $25, $05, $10, $27, $00, $00, $00, $00, $F4, $F0, $10, $00, $00, $01, $24, $18, $0, $0, $00, $0, $60, $3b
; Loot: 
org $D05580
db $62, $62, $00, $62
; --------------------------
; Original boss Apanda rank 44.0 -> Randomized boss Ramuh rank 31.0
; HP: 22200 -> 10000
; ENEMY: Apanda
; Skills: ['WindSlash', 'WindSlash']
; New skill: WindSlash
org $d0c409
db $AB
; New skill: WindSlash
org $d0c410
db $AB

; Enemy: Crayclaw
; Stats: 
org $D02A80
db $22, $3c, $07, $00, $17, $01, $17, $0e, $B8, $0B, $BE, $01, $B8, $0B, $00, $00, $00, $00, $30, $00, $00, $80, $00, $04, $24, $18, $0, $0, $00, $0, $54, $2b
; Loot: 
org $D05550
db $00, $10, $00, $40
; --------------------------
; Original boss Crayclaw rank 11.0 -> Randomized boss Puroboros, Puroboros, Puroboros, Puroboros, Puroboros, Puroboros rank 17.0
; HP: 2000 -> 3000
; ENEMY: Crayclaw

; Enemy: Magic Pot
; Stats: 
org $D00160
db $02, $05, $01, $00, $00, $00, $05, $00, $01, $00, $03, $00, $FF, $FF, $FF, $FF, $00, $00, $FF, $FF, $10, $00, $00, $00, $20, $18, $0, $0, $60, $0, $0B, $5B
; Loot: 
org $D0502C
db $E3, $00, $E3, $00

; Enemy: Omega
; Stats: 
org $D01FA0
db $4c, $77, $19, $62, $c0, $c3, $95, $20, $EA, $D8, $1C, $ED, $00, $00, $50, $C3, $00, $1d, $ff, $bf, $ff, $62, $20, $80, $24, $98, $80, $0, $B0, $0, $FD, $7c
; Loot: 
org $D053F4
db $00, $00, $00, $F8

; Enemy: Shinryuu
; Stats: 
org $D02D20
db $57, $a9, $26, $0e, $3c, $81, $3c, $20, $CC, $D8, $38, $C7, $00, $00, $00, $00, $00, $27, $ff, $ff, $fb, $98, $00, $40, $20, $98, $0, $0, $00, $0, $69, $66
; Loot: 
org $D055A4
db $4F, $EA, $00, $F7

; Enemy: SomberMage
; Stats: 
org $D02CA0
db $1e, $51, $12, $00, $1e, $20, $32, $1e, $FF, $FF, $50, $C3, $00, $00, $00, $00, $46, $80, $FF, $7B, $F7, $40, $00, $00, $A0, $18, $00, $00, $08, $00, $65, $61
; Loot: 
org $D05594
db $00, $00, $00, $00

; Enemy: SomberMage
; Stats: 
org $D02CC0
db $23, $55, $14, $0a, $32, $28, $1e, $32, $FF, $FF, $50, $C3, $00, $00, $00, $00, $46, $00, $FF, $FF, $F3, $C0, $00, $10, $21, $18, $00, $00, $28, $00, $66, $61
; Loot: 
org $D05598
db $00, $00, $00, $00

; Enemy: SomberMage
; Stats: 
org $D02CE0
db $28, $69, $16, $0a, $37, $30, $32, $3c, $FF, $FF, $50, $C3, $00, $00, $00, $00, $46, $00, $FF, $FF, $F3, $C0, $00, $00, $A0, $18, $00, $00, $C8, $00, $67, $61
; Loot: 
org $D0559C
db $00, $00, $00, $00


;==========
;formations
;==========
; Ramuh (Rank 31.0)  > Chim.Brain (Rank 16.0) 
org $D07840
db $4c, $00 
org $D07842
db $4c, $00
; Shoat (Rank 32.0)  > Minotauros (Rank 39.0) 
org $D078C0
db $A5, $00 
org $D078C2
db $A5, $00
; Golem (Rank 33.0)  > Calofisteri (Rank 43.0) 
org $D0791C
db $BB, $00 
org $D0791E
db $BB, $00
; Byblos (Rank 10.0)  > Tyrasaurus (Rank 21.0) 
org $D07870
db $BE, $01 
org $D07872
db $BE, $01
; WingRaptor (Rank 1.0)  > Abductor (Rank 22.0) 
org $D07874
db $B7, $01 
org $D07876
db $B7, $01
; Karlabos (Rank 2.0)  > LiquiFlame (Rank 6.0) 
org $D0781C
db $B8, $01 
org $D0781E
db $B8, $01
; Siren (Rank 3.0)  > ArchaeAvis (Rank 15.0) 
org $D0783C
db $B9, $01 
org $D0783E
db $B9, $01
; Forza (Rank 4.0)  > Omniscient (Rank 38.0) 
org $D078BC
db $BA, $01 
org $D078BE
db $BA, $01
; Galura (Rank 5.0)  > Gogo (Rank 41.0) 
org $D078CC
db $BB, $01 
org $D078CE
db $BB, $01
; LiquiFlame (Rank 6.0)  > Stalker (Rank 35.0) 
org $D078B8
db $BC, $01 
org $D078BA
db $BC, $01
; Sergeant (Rank 7.0)  > Antlion (Rank 29.0) 
org $D07894
db $BD, $01 
org $D07896
db $BD, $01
; Hole (Rank 12.0)  > Twin Tania (Rank 48.0) 
org $D07928
db $BF, $01 
org $D0792A
db $BF, $01
; AdamanTiMi (Rank 13.0)  > Gilgamesh (Rank 19.0) 
org $D07850
db $C0, $01 
org $D07852
db $C0, $01
; Sol Cannon (Rank 14.0)  > Golem (Rank 33.0) 
org $D078F8
db $C3, $01 
org $D078FA
db $C3, $01
; ArchaeAvis (Rank 15.0)  > Odin (Rank 36.0) 
org $D078B0
db $C4, $01 
org $D078B2
db $C4, $01
; Chim.Brain (Rank 16.0)  > Guardian (Rank 26.0) 
org $D07884
db $C5, $01 
org $D07886
db $C5, $01
; Titan (Rank 18.0)  > AdamanTiMi (Rank 13.0) 
org $D0782C
db $C6, $01 
org $D0782E
db $C6, $01
; Puroboros (Rank 17.0)  > Shoat (Rank 32.0) 
org $D078FC
db $C7, $01 
org $D078FE
db $C7, $01
; Gilgamesh (Rank 19.0)  > Merugene (Rank 34.0) 
org $D078AC
db $C9, $01 
org $D078AE
db $C9, $01
; Gilgamesh (Rank 20.0)  > Necrofobia (Rank 49.0) 
org $D0792C
db $D0, $01 
org $D0792E
db $D0, $01
; Tyrasaurus (Rank 21.0)  > Apocalypse (Rank 45.0) 
org $D07920
db $D1, $01 
org $D07922
db $D1, $01
; Abductor (Rank 22.0)  > Atmos (Rank 25.0) 
org $D07880
db $D2, $01 
org $D07882
db $D2, $01
; HiryuuPlant (Rank 23.0)  > WingRaptor (Rank 1.0) 
org $D07804
db $D3, $01 
org $D07806
db $D3, $01
; Gilgamesh (Rank 24.0)  > Gilgamesh (Rank 28.0) 
org $D0788C
db $D4, $01 
org $D0788E
db $D4, $01
; Atmos (Rank 25.0)  > Crayclaw (Rank 11.0) 
org $D078D4
db $D5, $01 
org $D078D6
db $D5, $01
; Guardian (Rank 26.0)  > Catastroph (Rank 46.0) 
org $D07924
db $D6, $01 
org $D07926
db $D6, $01
; Carbunkle (Rank 27.0)  > Byblos (Rank 10.0) 
org $D07824
db $D7, $01 
org $D07826
db $D7, $01
; Gilgamesh (Rank 28.0)  > Hole (Rank 12.0) 
org $D07828
db $D8, $01 
org $D0782A
db $D8, $01
; Antlion (Rank 29.0)  > HiryuuPlant (Rank 23.0) 
org $D07878
db $DA, $01 
org $D0787A
db $DA, $01
; Halicarnaso (Rank 47.0)  > Gilgamesh (Rank 20.0) 
org $D0786C
db $DE, $01 
org $D0786E
db $DE, $01
; Merugene (Rank 34.0)  > Shiva (Rank 9.0) 
org $D07814
db $E0, $01 
org $D07816
db $E0, $01
; Odin (Rank 36.0)  > Sol Cannon (Rank 14.0) 
org $D07838
db $E1, $01 
org $D0783A
db $E1, $01
; Gargoyle (Rank 30.0)  > Forza (Rank 4.0) 
org $D07810
db $E2, $01 
org $D07812
db $E2, $01
; Triton (Rank 37.0)  > Halicarnaso (Rank 47.0) 
org $D078E0
db $E3, $01 
org $D078E2
db $E3, $01
; Omniscient (Rank 38.0)  > Sergeant (Rank 7.0) 
org $D07820
db $E4, $01 
org $D07822
db $E4, $01
; Minotauros (Rank 39.0)  > Gilgamesh (Rank 24.0) 
org $D0787C
db $E5, $01 
org $D0787E
db $E5, $01
; Leviathan (Rank 40.0)  > Carbunkle (Rank 27.0) 
org $D07888
db $E6, $01 
org $D0788A
db $E6, $01
; Stalker (Rank 35.0)  > Gargoyle (Rank 30.0) 
org $D078B4
db $E7, $01 
org $D078B6
db $E7, $01
; Gogo (Rank 41.0)  > Karlabos (Rank 2.0) 
org $D07808
db $E8, $01 
org $D0780A
db $E8, $01
; Bahamut (Rank 42.0)  > Leviathan (Rank 40.0) 
org $D078C4
db $E9, $01 
org $D078C6
db $E9, $01
; Ifrit (Rank 8.0)  > Titan (Rank 18.0) 
org $D07844
db $EE, $01 
org $D07846
db $EE, $01
; Shiva (Rank 9.0)  > Galura (Rank 5.0) 
org $D07818
db $F1, $01 
org $D0781A
db $F1, $01
; Calofisteri (Rank 43.0)  > Bahamut (Rank 42.0) 
org $D078D0
db $F2, $01 
org $D078D2
db $F2, $01
; Apocalypse (Rank 45.0)  > Siren (Rank 3.0) 
org $D0780C
db $F3, $01 
org $D0780E
db $F3, $01
; Catastroph (Rank 46.0)  > Apanda (Rank 44.0) 
org $D078D8
db $F4, $01 
org $D078DA
db $F4, $01
; Necrofobia (Rank 49.0)  > Ifrit (Rank 8.0) 
org $D078E4
db $F5, $01 
org $D078E6
db $F5, $01
; Twin Tania (Rank 48.0)  > Triton (Rank 37.0) 
org $D078C8
db $F6, $01 
org $D078CA
db $F6, $01
; Apanda (Rank 44.0)  > Ramuh (Rank 31.0) 
org $D078F4
db $F8, $01 
org $D078F6
db $F8, $01
; Crayclaw (Rank 11.0)  > Puroboros (Rank 17.0) 
org $D07848
db $FA, $01 
org $D0784A
db $FA, $01

;=====================
;Kuzar Reward Text Fix
;=====================
; GuardOff Blue Magic
org $E23F98
db  $66, $8E, $7A, $8B, $7D, $6E, $7F, $7F, $96, $61, $85, $8E, $7E, $96, $6C, $7A, $80, $82, $7C, $00
; Chemist Job Crystal
org $E240A5
db  $62, $81, $7E, $86, $82, $8C, $8D, $96, $69, $88, $7B, $96, $62, $8B, $92, $8C, $8D, $7A, $85, $00
; X-Magic
org $E23F7A
db  $77, $C5, $6C, $7A, $80, $82, $7C, $00
; Kick
org $E2404C
db  $6A, $82, $7C, $84, $00
; HP +20%
org $E240C4
db  $67, $6F, $96, $E2, $55, $53, $CD, $00
; Ramuh Esper Magic
org $E23FD6
db  $71, $7A, $86, $8E, $81, $96, $64, $8C, $89, $7E, $8B, $96, $6C, $7A, $80, $82, $7C, $00
; Bio Sword Magic
org $E24011
db  $61, $82, $88, $96, $72, $90, $88, $8B, $7D, $96, $6C, $7A, $80, $82, $7C, $00
; Staff
org $E24088
db  $72, $8D, $7A, $7F, $7F, $00
; Revive
org $E23FF4
db  $71, $7E, $8F, $82, $8F, $7E, $00
; Thunder Whip
org $E2406A
db  $73, $81, $8E, $87, $7D, $7E, $8B, $96, $76, $81, $82, $89, $00
; Requiem Song Magic
org $E23FB7
db  $71, $7E, $8A, $8E, $82, $7E, $86, $96, $72, $88, $87, $80, $96, $6C, $7A, $80, $82, $7C, $00
; Mythril Armor
org $E2402D
db  $6C, $92, $8D, $81, $8B, $82, $85, $96, $60, $8B, $86, $88, $8B, $00
; Character Names
org $C0BEC9
db $6B, $7E, $87, $87, $7A, $FF, $FF, $FF
org $C0BED1
db $66, $7A, $85, $8E, $7F, $FF, $FF, $FF
org $C0BED9
db $65, $7A, $8B, $82, $8C, $FF, $FF, $FF
org $C0BEE1
db $6A, $8B, $82, $85, $7E, $FF, $FF, $FF
; Odin location animation fix (resolve softlocks)
org $D04C4F
db $60
;CONFIG SETTINGS
;RGB
org $C0F343
db $00, $00
;Reward Mult
org $C0F342
db $2A
; Hints
org $E19AD3
db $73, $81, $7E, $92, $96, $8C, $7A, $92, $96, $8D, $81, $7A, $8D, $96, $8D, $81, $7E, $96, $61, $8B, $7A, $7C, $7E, $85, $7E, $8D, $01, $82, $8C, $96, $89, $8B, $7E, $8C, $7E, $87, $8D, $96, $82, $87, $96, $76, $88, $8B, $85, $7D, $96, $54, $A3, $53, $A3, $00
org $E149DD
db $73, $81, $7E, $92, $96, $8C, $7A, $92, $96, $8D, $81, $7A, $8D, $96, $65, $88, $8B, $84, $96, $73, $88, $90, $7E, $8B, $01, $81, $88, $85, $7D, $8C, $96, $8D, $81, $7E, $96, $6C, $82, $8B, $7A, $80, $7E, $96, $71, $7A, $7D, $7A, $8B, $A3, $00
org $E19ED6
db $73, $81, $7E, $92, $96, $8C, $7A, $92, $96, $8D, $81, $7A, $8D, $96, $79, $7E, $93, $7A, $96, $65, $85, $7E, $7E, $8D, $01, $81, $88, $85, $7D, $8C, $96, $8D, $81, $7E, $96, $73, $8B, $7E, $87, $7C, $81, $96, $6F, $7A, $80, $7E, $A3, $00
org $E35380
db $73, $81, $7E, $92, $96, $8C, $7A, $92, $96, $8D, $81, $7A, $8D, $96, $8D, $81, $7E, $96, $67, $82, $8B, $92, $8E, $8E, $96, $62, $7A, $85, $85, $01, $82, $8C, $96, $89, $8B, $7E, $8C, $7E, $87, $8D, $96, $82, $87, $96, $76, $88, $8B, $85, $7D, $96, $55, $A3, $53, $A3, $00
org $E176C0
db $73, $81, $7E, $92, $96, $8C, $7A, $92, $96, $8D, $81, $7A, $8D, $96, $8D, $81, $7E, $96, $57, $8D, $81, $96, $73, $7A, $7B, $85, $7E, $8D, $01, $82, $8C, $96, $89, $8B, $7E, $8C, $7E, $87, $8D, $96, $82, $87, $96, $76, $88, $8B, $85, $7D, $96, $54, $A3, $53, $A3, $00
org $E281F7
db $73, $81, $7E, $92, $96, $8C, $7A, $92, $96, $8D, $81, $7A, $8D, $96, $6F, $92, $8B, $7A, $86, $82, $7D, $01, $82, $8C, $96, $88, $87, $96, $8D, $81, $7E, $96, $89, $7A, $8D, $81, $96, $8D, $88, $96, $8D, $81, $7E, $96, $75, $88, $82, $7D, $A3, $00
org $E26328
db $73, $81, $7E, $92, $96, $8C, $7A, $92, $96, $8D, $81, $7A, $8D, $96, $66, $8B, $7E, $7A, $8D, $96, $73, $8B, $7E, $87, $7C, $81, $01, $81, $88, $85, $7D, $8C, $96, $8D, $81, $7E, $96, $72, $7A, $87, $7D, $90, $88, $8B, $86, $96, $61, $7A, $82, $8D, $A3, $00
org $E1079B
db $73, $81, $7E, $92, $96, $8C, $7A, $92, $96, $8D, $81, $7A, $8D, $96, $8D, $81, $7E, $96, $72, $81, $8B, $82, $87, $7E, $96, $6F, $7A, $80, $7E, $01, $82, $8C, $96, $89, $8B, $7E, $8C, $7E, $87, $8D, $96, $82, $87, $96, $76, $88, $8B, $85, $7D, $96, $56, $A3, $53, $A3, $00
org $E23975
db $73, $81, $7E, $92, $96, $8C, $7A, $92, $96, $8D, $81, $7A, $8D, $96, $8D, $81, $7E, $96, $6F, $92, $8B, $7A, $86, $82, $7D, $96, $6F, $7A, $80, $7E, $01, $82, $8C, $96, $89, $8B, $7E, $8C, $7E, $87, $8D, $96, $82, $87, $96, $76, $88, $8B, $85, $7D, $96, $54, $A3, $53, $A3, $00
org $E33A31
db $73, $81, $7E, $92, $96, $8C, $7A, $92, $96, $8D, $81, $7A, $8D, $96, $73, $88, $8B, $87, $7A, $96, $62, $7A, $87, $7A, $85, $01, $82, $8C, $96, $88, $87, $96, $8D, $81, $7E, $96, $89, $7A, $8D, $81, $96, $8D, $88, $96, $8D, $81, $7E, $96, $75, $88, $82, $7D, $A3, $00
org $E30595
db $73, $81, $7E, $92, $96, $8C, $7A, $92, $96, $8D, $81, $7A, $8D, $96, $8D, $81, $7E, $96, $60, $7D, $7A, $86, $7A, $87, $8D, $82, $8D, $7E, $01, $82, $8C, $96, $89, $8B, $7E, $8C, $7E, $87, $8D, $96, $82, $87, $96, $76, $88, $8B, $85, $7D, $96, $56, $A3, $53, $A3, $00
org $E30518
db $73, $81, $7E, $92, $96, $8C, $7A, $92, $96, $8D, $81, $7A, $8D, $96, $8D, $81, $7E, $96, $54, $8C, $8D, $96, $73, $7A, $7B, $85, $7E, $8D, $01, $82, $8C, $96, $89, $8B, $7E, $8C, $7E, $87, $8D, $96, $82, $87, $96, $76, $88, $8B, $85, $7D, $96, $54, $A3, $53, $A3, $00
org $E36AFA
db $73, $81, $7E, $92, $96, $8C, $7A, $92, $96, $8D, $81, $7A, $8D, $96, $65, $85, $92, $82, $87, $80, $96, $6B, $88, $87, $84, $7A, $96, $71, $8E, $82, $87, $8C, $01, $82, $8C, $96, $88, $87, $96, $8D, $81, $7E, $96, $89, $7A, $8D, $81, $96, $8D, $88, $96, $8D, $81, $7E, $96, $75, $88, $82, $7D, $A3, $00
org $E36A7F
db $73, $81, $7E, $92, $96, $8C, $7A, $92, $96, $8D, $81, $7A, $8D, $96, $8D, $81, $7E, $96, $72, $8D, $7E, $7A, $86, $8C, $81, $82, $89, $96, $6A, $7E, $92, $01, $82, $8C, $96, $89, $8B, $7E, $8C, $7E, $87, $8D, $96, $82, $87, $96, $76, $88, $8B, $85, $7D, $96, $55, $A3, $53, $A3, $00
org $E36B52
db $73, $81, $7E, $92, $96, $8C, $7A, $92, $96, $8D, $81, $7A, $8D, $96, $6C, $8E, $7A, $96, $65, $88, $8B, $7E, $8C, $8D, $01, $82, $8C, $96, $88, $87, $96, $8D, $81, $7E, $96, $89, $7A, $8D, $81, $96, $8D, $88, $96, $8D, $81, $7E, $96, $75, $88, $82, $7D, $A3, $00

;HASH CODE
org $E73400
db $67, $7A, $8C, $81, $CF, $96, $EE, $96, $E7, $96, $ED, $96, $CA, $96, $E9, $96, $00


                    org $C33320
                
                dw $0100
                dw $0000
                
                !color_num = 15
                while !color_num > 0 
                    dw $F401
                    !color_num #= !color_num-1
                endif
                
                
                    
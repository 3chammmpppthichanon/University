[org 7c00h]            ; BIOS will load us to this address
mov ax, 0b800h         ; Console memory is at 0xb8000
                        ; set up a segment
mov es, ax             ; for the start of the console text.
;
; Let's clear the screen....
;
xor di, di             ; Start at beginning of screen
mov cx, 80*25          ; Number of chars in the screen 
mov al, ' '            ; Space character
mov ah, 0fh            ; Color (white on black)
repne stosw            ; Copy!


mov byte [es:0], '6'
mov byte [es:1], 0x1f 

mov byte [es:2], '6' 
mov byte [es:3], 0x2f

mov byte [es:4], '0'
mov byte [es:5], 0x3f 

mov byte [es:6], '5' 
mov byte [es:7], 0x4f 

mov byte [es:8], '0' 
mov byte [es:9], 0x5f

mov byte [es:10], '0'
mov byte [es:11], 0x6f

mov byte [es:12], '6'
mov byte [es:13], 0x7f

mov byte [es:14], '6'
mov byte [es:15], 0x8f

mov byte [es:16], '9'
mov byte [es:17], 0x9f

mov byte [es:18], '8'
mov byte [es:19], 0xAf

mov byte [es:20], 'C'
mov byte [es:21], 0xBf

mov byte [es:22], 'O'
mov byte [es:23], 0xCf

mov byte [es:24], 'S'
mov byte [es:25], 0xDf

mov byte [es:26], '3'
mov byte [es:27], 0xEf

mov byte [es:28], '1'
mov byte [es:29], 0xF1

mov byte [es:30], '0'
mov byte [es:31], 0x70

mov byte [es:32], '5'
mov byte [es:33], 0x62

sleep:
hlt                    ; Halts CPU until the next external
                        ;interrupt is fired
jmp sleep              ; Loop forever

times 510-($-$$) db 0  ; Pad to 510 bytes
dw 0aa55h              ; Add boot magic word to mark us
                        ; as bootable
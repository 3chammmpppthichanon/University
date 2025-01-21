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


mov byte [es:0], 'H'   ; Write an 'H'
mov byte [es:1], 08ch


sleep:
hlt                    ; Halts CPU until the next external
                        ;interrupt is fired
jmp sleep              ; Loop forever

times 510-($-$$) db 0  ; Pad to 510 bytes
dw 0aa55h              ; Add boot magic word to mark us
                        ; as bootable
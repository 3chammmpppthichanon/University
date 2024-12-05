[org 7c00h]              ; BIOS will load us to this address
mov ax, 0b800h           ; Console memory is at 0xb8000
mov es, ax               ; Set up the segment for video memory

; Clear the screen
xor di, di               ; Start at the beginning of the screen
mov cx, 80*25            ; Number of characters on the screen
mov al, ' '              ; Space character
mov ah, 0fh              ; Color (white on black)
rep stosw                ; Fill the screen with spaces

; Write "Hello World!" to the screen
mov si, msg              ; Load the address of the message
xor di, di               ; Start writing at the top-left of the screen
next_char:
lodsb                    ; Load the next byte from [si] into AL
cmp al, 0                ; Check if it's the null terminator
je done                  ; If null, we're done
mov ah, 0fh              ; Set the color (white on black)
stosw                    ; Write character and color to video memory
jmp next_char            ; Repeat for the next character

done:
sleep:
hlt                      ; Halt the CPU until the next external interrupt
jmp sleep                ; Loop forever

msg db 'Hello World!', 0 ; Null-terminated string

times 510-($-$$) db 0    ; Pad to 510 bytes
dw 0aa55h                ; Add boot signature to mark as bootable


;mov byte [es:0], 'H'	; Write an 'H'
;mov byte [es:1], 08ch

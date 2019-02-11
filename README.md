# Plover retro text transform

Perform various text transforms, such as titlecase, retroactively.

## Meta actions

`{:retro:retro_capitalise:n}`: Capitalise nth word back leaving other words as is.

`{:retro:retro_title:n}`: Capitalise previous n words.

`{:retro:retro_upper:n}`: Convert previous n words to uppercase.

`{:retro:retro_lower:n}`: Convert previous n words to lowercase. Note that this doesn't work with forced uppercase (`{<}` and `{MODE:CAPS}`.

`{:retro:retro_replace_space:n:c}`: Replace spaces between previous n words.

## Usage

Create some dictionary entries to trigger the retroactive transform:

```
"KPA*D": "{:retro_capitalise:1}",
"KPA*D/KPA*D": "{:retro_capitalise:2}",
"KPA*D/KPA*D/KPA*D": "{:retro_capitalise:3}",
"KPA*D/KPA*D/KPA*D/KPA*D": "{:retro_capitalise:4}",
"KPA*D/KPA*D/KPA*D/KPA*D/KPA*D": "{:retro_capitalise:5}",
"KPAD": "{:retro_title:1}",
"KPAD/KPAD": "{:retro_title:2}",
"KPAD/KPAD/KPAD": "{:retro_title:3}",
"KPAD/KPAD/KPAD/KPAD": "{:retro_title:4}",
"KPAD/KPAD/KPAD/KPAD/KPAD": "{:retro_title:5}",
"AUPD": "{:retro_upper:1}",
"AUPD/AUPD": "{:retro_upper:2}",
"AUPD/AUPD/AUPD": "{:retro_upper:3}",
"AUPD/AUPD/AUPD/AUPD": "{:retro_upper:4}",
"AUPD/AUPD/AUPD/AUPD/AUPD": "{:retro_upper:5}",
"HR*UD": "{:retro_lower:1}",
"HR*UD/HR*UD": "{:retro_lower:2}",
"HR*UD/HR*UD/HR*UD": "{:retro_lower:3}",
"HR*UD/HR*UD/HR*UD/HR*UD": "{:retro_lower:4}",
"HR*UD/HR*UD/HR*UD/HR*UD/HR*UD": "{:retro_lower:5}",
"STPH-BGD": "{:retro_replace_space:1:_}",
```

Then you can use the strokes like this:

```
HEL/LOE/WORLD/KPA*D
hello World

HEL/LOE/WORLD/KPA*D/KPA*D
Hello world

HEL/LOE/WORLD/KPAD
hello World

HEL/LOE/WORLD/KPAD/KPAD
Hello World

HEL/LOE/WORLD/AUPD
hello WORLD

HEL/LOE/WORLD/AUPD/AUPD
HELLO WORLD

TP-PL/HEL/LOE/WORLD/L*UD
. Hello world

TP-PL/HEL/LOE/WORLD/L*UD/L*UD
. hello world

HEL/LOE/WORLD/STPH-BGD
hello_world
```

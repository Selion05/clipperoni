# clipperoni
A simple clipboard manager with dmenu

I recently found [clipmenu](https://github.com/cdown/clipmenu) and I liked the idea of having multiple clipboards, but I didn't like that every clipboard change gets stored. 

So I wrote this. 

## Usage

```
clipperoni save <name>
```
Saves the current clipboard in `$XDG_RUNTIME_DIR`

If no name is given You can enter one with dmenu.

```
clipperoni load <name>
```
Loads saved text to clipboard

If no name is given You can select one with dmenu.

You can bind hot keys like `Super+c` and `Super+v` to  `clipperoni save` `clipperoni load` respectively and you are good to go. 

## Install
I have a working PKGBUILD, once I have figured out how to submit it
it will be available in the aur. For now 
```bash
git clone https://github.com/Selion05/clipperoni.git
cd clipperoni
# You need pyperclip and python>=3.6
python setup.py install
cp bin/clipperoni  /some-bin-dir-in$PATH

```

## Todo 
I guess with time it will be annoying to do `Super+v` and then `CTRL+v` so actually it should do this automatically. I haven't found a good solution so far. Suggestions are very welcome :) 

Possible solution https://unix.stackexchange.com/a/399638/308214

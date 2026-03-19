# Sketcher
A simple command line based sketching app written in python using curses.

## Usage
`python3 sketcher <COMMANDS_KEYS>`

## Commands
|Command|Key|Desc|
|-|-|-|
|Move Up|`w`|Moves the cursor up one space|
|Move Down|`s`|Moves the cursor down one space|
|Move Left|`a`|Moves the cursor left one space|
|Move Right|`d`|Moves the cursor right one space|
|Shift Up|`W`|Moves the cursor up to the edge|
|Shift Down|`S`|Moves the cursor down to the edge|
|Shift Left|`A`|Moves the cursor left to the edge|
|Shift Right|`D`|Moves the cursor right to the edge|
|Place Tile|`#`|Places a tile at the cursor location|
|Clear Tile|`BACKSPACE`|Clears the tile at the cursor location|
|Fill Area|`~`|Fills the area under the cursor with tiles|
|Toggle Trail|`t`|Toggles trail mode on/off|
|Show Color Palette|`C`|Shows the color palette|
|Toggle Cursor|`h`|Toggles the visibility of the cursor|
|New Sketch|`N`|Clears all tiles|
|Line|`l`|Draws a line to the cursor from the last placed tile|
|Quick Save|`]`|Quickly saves the sketch to `./sketch.json`|
|Save|`}`|Saves the sketch to the specified file|
|Quick Load|`[`|Quickly loads the sketch from `./sketch.json`|
|Load|`{`|Loads the sketch from the specified file|
|Quit|`Q`|Quits the application|
|Quick Save & Quit|`X`|Saves to `./sketch.json` and then quits|

## TODO
- Rebinding
- Custom commands

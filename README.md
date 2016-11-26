# Game Code Encryption

## Spectacularly well-written plotline

Brooks is the lead programmer of Fallout 5, gets word that an evil malicious hacker named "Crsn" is attempting to steal all the data and shut down all their servers. Brooks calls up his friend, Tristan, a top hacker who happens to be a lead programmer of Persona 6 to encrypt his data.

## Your Mission

Help Brooks and Tristan write a program to encrypt the valuable Fallout 5 files and protect them from Crsn. Write a function called `changeChar`, which will take in three parameters. The first parameter will be a line of text. The second parameter is a letter found in the line of text to be replaced. The third parameter is a letter to replace the value of the second parameter. `changeChar` replaces all instances of a given letter with another letter in a line of text recursively. (Do not use loops.)

## Parameters

`lineOfText` - the line of text which need certain letters to replace.

`charA` - the character you want to be replaced.

`charB` - the character you want `charA` to be replaced with.

## Return Value

The function returns a single string, `lineOfText` with all instances of `charA` replaced with `charB`

## Example function call

`changeChar('The Jr DevLeague Academy is awesome!!', 'e', 'o')` will return  `"Tho Jr DovLoaguo Acadomy is awosomo!!"`

## Important Hints

- Strings have indices too, not just lists
- You can slice both strings and lists, and a quick way of slicing to either end of a list/string is only having the colon:
  - If you want to slice to the end of the list, instead of [5:len(list)] you can use [5:]
  - If you want slice to the beginning of the list, instead of [0:5], you can use [:5]
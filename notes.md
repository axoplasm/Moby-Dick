Text Conversion Notes
=====================

# Scriptable edits

## Format chapter title

### Markdown:

`### Chapter [n].`   
`The Chapter Title.`   
`====================`   

## em-dash double hyphens
`:%s/--/ — /g`

## Smarten double quotes
`%s/^"/“/g `
`%s/ "/ “/g `
`%s/"$/”/g `
`%s/" /” /g `


# Manual edits

## Wrap long paragraphs to 80col

As I read.

`gqap`

## Smarten single quotes

Scan text for single-quoted dialogue (i.e. nested dialogue.) For that range:

`[address]s/“'/“‘/g`
`[address]s/'”/’”/g`
`[address]s/ '/ ‘/g`
`[address]s/' /’ /g`
`[address]s/^'/‘/g`
`[address]s/'$/’/g`

## Smarten apostrophes

Any remaining tick marks are likely to be apostrophes.

`%s/'/’/g`

## \*emphasize\* ALL-CAPS TEXT

`EMPHASIZED TEXT` becomes `*emphasized text.*` 

`CITATIONS` become `_Citations_`. 

`[STAGE DIRECTIONS]` e.g. Chapter 36 et al. become `_*[Stage directions]*_` These may further be set off by horizontal rules (`----`). 

`ACTOR INDICTORS` e.g. Chapter 40 become `__ACTOR INDICATORS__`.

In a few other  places (e.g. the epitaphs in Chapter 6), I have preserved ALL CAPS, usually bolding it, as a stylistic choice.

## Blockquote poetry or other unusual text (e.g. printed handbills or carven letters), usually with ragged right margins.

May also be set off with horizontal rules (`----`).

### Markdown:

`> this is a short line.    `    
`> Followed by another short line    `    

*__Note:__ Ragged lines need two or more spaces at the end of the line to force soft line breaks (\<br\>.)*

## Other conventions:

* Spelling, paragraph breaks, and punctuation as per source file.
* For stage directions, added square braces `[ ]` (or substituted for parentheses) where appropriate — not consistent in source text.
* Punctuation inside quotations.
* `Ship’s Proper Name` (usually not styled in source text) becomes `*Ship’s Proper Name*`.
* `Fremde Wort` (foreign words, usually not styled in source text) become `*Fremde Wort*`.
* Markup captures quotations and punctuation.
* No changes to `....` or `...` or `..` as ellipses. No space before or after ellipses.
* __Bold__ text  and lists where appropriate, while reading. 



 

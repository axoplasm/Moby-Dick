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

`EMPHASIZED TEXT` (generally in dialogue) becomes `*emphasized text.*` `CITATIONS` become `_Citations_`.

In some places (e.g. the epitaphs in Chapter 6), I have preserved ALL CAPS, usually bolding it, as a stylistic choice.

## Blockquote poetry or other unusual text (e.g. printed handbills or carven letters), usually with ragged right margins.

### Markdown:

`> this is a short line.    `    
`> Followed by another short line    `    

*__Note:__ Ragged lines need two or more spaces at the end of the line to force soft line breaks (\<br\>.)*

## Other conventions:

* Spelling, paragraph breaks, and punctuation as per source file.
* Punctuation inside quotations.
* Markup captures quotations and punctuation.
* No changes to `....` or `...` or `..` as ellipses. No space before or after ellipses.
* __Bold__ text  and lists where appropriate, while reading. 



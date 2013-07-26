File Conversion Notes
=====================

## Wrap long paragraphs to 80col

Generally: I do this line-by-line while reading

### Vim:
`gqap`

## Smarten double quotes
### Vim:
`:%s/"\(.*\)"/“\1“/g`

## Smarten single quotes
### Vim:
`:%s/'\(.*\)'/‘\1’/g`

## Smarten apostrophes

Generally do this on a case-by-case basis.

### Vim:
`/'`   
`r’`   
`n`   

## em-dash double hyphens

...with one space on either side of the double hyphen.

Haven’t yet encountered a need for en-dashes.

### Vim:
`:%s/--/ — /g`

## \*emphasize\* ALL-CAPS TEXT

No regex for this yet, I do it manually as I read. `EMPHASIZED TEXT` becomes `*emphasized text.*` `CITATIONS` become `_Citations_`.


## Blockquote poetry or other text with ragged right margins
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



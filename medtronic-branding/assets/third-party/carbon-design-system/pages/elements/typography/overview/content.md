# Typography – Carbon Design System

Source: https://www.carbondesignsystem.com/elements/typography/overview/

# Typography

Our approach to the typographic system uses IBM Plex as its typeface. It has
been carefully engineered with suitable scales, styles, and weights to help
create clear hierarchies and organize information that guides users through IBM
products or experiences.

- [Type tokens and sets](https://carbondesignsystem.com/elements/typography/overview/#type-tokens-and-sets)

- [Typeface: IBM Plex](https://carbondesignsystem.com/elements/typography/overview/#typeface:-ibm-plex)

- [Scale](https://carbondesignsystem.com/elements/typography/overview/#scale)

- [Style](https://carbondesignsystem.com/elements/typography/overview/#style)

- [Type color](https://carbondesignsystem.com/elements/typography/overview/#type-color)

- [Resources](https://carbondesignsystem.com/elements/typography/overview/#resources)

## Type tokens and sets

Carbon uses type tokens across two type sets to manage typography. Type tokens
are pre-set configurations of typographic elements such as font size, weight, or
leading (line height) that are specifically calibrated for use alongside
[IBM Plex](http://ibm.com/plex) in product. Selecting the appropriate type style
is determined by layout or template structure. Layouts may have several levels
of architecture or areas that require varying typographic hierarchies.

### Productive and expressive type sets

The productive type set is primarily used within product spaces, where users
benefit from a more condensed treatment of content to maintain focus on tasks.
The productive styles work together to support the hierarchy of information and
set user expectations. On the other hand, the larger expressive type styles
allow for a more dramatic, graphic use of type in editorial and marketing
design. These type styles are excellent for long form reading and scanning, but
would be distracting if used in product.

Within **Body styles** and **Utility styles**, the same set of styles are
offered. Productive styles are named with a suffix of `-01` and expressive style
names have a suffix of `-02`.

There are two heading sets and the major difference between them is in how they
are implemented in code. The productive type set uses fixed headings. Expressive
headings are responsive and the type styles change size at different
breakpoints.

For more detail, see [Style strategies](https://carbondesignsystem.com/elements/typography/style-strategies/)
and [Type sets](https://carbondesignsystem.com/elements/typography/type-sets/).

## Typeface: IBM Plex

Carbon uses the open-source typeface **IBM Plex**. It has been carefully
designed to meet IBM’s needs as a global technology company and reflect IBM’s
spirit, beliefs, and design principles. IBM Plex can be accessed and downloaded
from the [Plex GitHub Repo](https://github.com/ibm/plex).

IBM Plex Sans

IBM Plex Serif

IBM Plex Mono

### Sans-serif font stack

```

font-family: 'IBM Plex Sans', 'Helvetica Neue', Arial, sans-serif;Copy to clipboard

```

### Serif font stack

```

font-family: 'IBM Plex Serif', 'Georgia', Times, serif;Copy to clipboard

```

### Mono font stack

```

font-family: 'IBM Plex Mono', 'Menlo', 'DejaVu Sans Mono',  'Bitstream Vera Sans Mono', Courier, monospace;Copy to clipboard

```

## Scale

The IBM type scale is built on a single equation. The formula for our scale was
created to provide hierarchy for all types of experiences. The formula assumes
that y₀=12 px.

| rem | px |

| --- | --- |

| 0.75 | Plex 12 |

| 0.875 | Plex 14 |

| 1 | Plex 16 |

| 1.125 | Plex 18 |

| 1.25 | Plex 20 |

| 1.5 | Plex 24 |

| 1.75 | Plex 28 |

| 2 | Plex 32 |

| 2.25 | Plex 36 |

| 2.625 | Plex 42 |

| 3 | Plex 48 |

| 3.375 | Plex 54 |

| 3.75 | Plex 60 |

| 4.25 | Plex 68 |

| 4.75 | Plex 76 |

| 5.25 | Plex 84 |

| 5.75 | Plex 92 |

```

Xn = Xn-1 + {INT[(n-2)/4] + 1} * 2
Xn: step n type size Xn-1: step n-1 type size

```

## Style

Typography creates purposeful texture, guiding users to read and understand the
hierarchy of information. The right typographic treatment and the controlled
usage of type styles helps manage the display of content, keeping it useful,
simple, and effective.

### Weights

Font weight is an important typographic variable that can add emphasis and
differentiate content hierarchy. Font weight and size pairings must be carefully
balanced. A bold weight will always have more emphasis than a lighter weight
font of the same size. However, a lighter weight font can rank hierarchically
higher than a bold font if the lighter weight type size is significantly larger
than the bold one.

We suggest using IBM Plex Light, Regular, and SemiBold for digital experiences.
The semibold weight is ideal for section headers, but should not be used for
long text.

Semibold (600)

Regular (400)

Light (300)

### Italic

Each weight has an italic style, which should only be used when you need to
emphasize certain words in a sentence (i.e., titles of works, technical terms,
names of devices, and captions).

Semibold Italic (600)

Regular (400)

Light (300)

## Type color

Type color should be carefully considered, with legibility and accessibility as
paramount concerns. Keep type color neutral in running text. Use primary blue
for primary actions.

Core blue colors are used for text links and primary actions

Secondary actions use Gray 100 and icons

Other use cases for colored type are code snippets, warnings, alerts, etc.

## Resources

## Code samples

```
font-family: 'IBM Plex Sans', 'Helvetica Neue', Arial, sans-serif;Copy to clipboard
```

```scss
font-family: 'IBM Plex Sans', 'Helvetica Neue', Arial, sans-serif;
```

```
font-family: 'IBM Plex Serif', 'Georgia', Times, serif;Copy to clipboard
```

```scss
font-family: 'IBM Plex Serif', 'Georgia', Times, serif;
```

```
font-family: 'IBM Plex Mono', 'Menlo', 'DejaVu Sans Mono',  'Bitstream Vera Sans Mono', Courier, monospace;Copy to clipboard
```

```scss
font-family: 'IBM Plex Mono', 'Menlo', 'DejaVu Sans Mono',  'Bitstream Vera Sans Mono', Courier, monospace;
```

```
Xn = Xn-1 + {INT[(n-2)/4] + 1} * 2
Xn: step n type size Xn-1: step n-1 type size
```

```
Xn = Xn-1 + {INT[(n-2)/4] + 1} * 2
Xn: step n type size Xn-1: step n-1 type size
```

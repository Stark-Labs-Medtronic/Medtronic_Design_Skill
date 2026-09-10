# Accessibility – Carbon Design System

Source: https://www.carbondesignsystem.com/guidelines/accessibility/developers/

# Accessibility

Write code that is clear and logical. Be detailed in alt text and image
descriptions, and at each step consider users who experience your product
through alternative technologies.

- [HTML best practices](https://carbondesignsystem.com/guidelines/accessibility/developers/#html-best-practices)

- [CSS best practices](https://carbondesignsystem.com/guidelines/accessibility/developers/#css-best-practices)

- [Mouse-specific events](https://carbondesignsystem.com/guidelines/accessibility/developers/#mouse-specific-events)

## HTML best practices

### Structuring code and navigation

Think of code hierarchy when structuring your content. Be sure screen readers
and keyboard-only users can access interactive elements in a logical and
predictable order via tabbing. Begin with the header, followed by the main
navigation, then page navigation (from left to right, top to bottom), and end
with the footer. Keyboard users should encounter an intentional experience that
is comparable to the experience of mouse users.

### Use semantic HTML

Use native HTML elements as much as you can. These elements have built-in
accessibility benefits. They inform screen readers what they are and what they
do, and standard interactive elements, such as a button, include keyboard
functionality. Aside from making a page accessible, native HTML is easier to
develop and maintain, better on mobile, and improves search engine optimization.

```

<button>Play Video</button><header></header><main></main><nav></nav><footer></footer><aside></aside><section></section><article></article>Copy to clipboard

```

### Use clear language

When adding content, consider cognitive disabilities, anyone whose native
language isn’t the language your content is written in, and screen readers. When
possible, avoid dashes, abbreviations, acronyms (at least the first time), and
table layouts if a table is not needed. If abbreviating, use the native
`<abbr />` element with title attribute.

```

"9 to 5" "November" <abbr title="November">Nov</abbr>Copy to clipboard

```

### Use meaningful text labels

Consider visually impaired people when labeling elements. Make sure there is
textual context for screen readers.

```

<a>Read more about pricing</a>Copy to clipboard

```

```

<a>Click here</a>Copy to clipboard

```

### Designing accessible data tables

Always specify table headers with `<th />` elements, and make sure they stand
out. Utilize `scope` attributes if necessary to specify if they are headers for
rows or columns. Utilize alternative text along with tables for visually
impaired users. `<caption />` is preferred, but `<table />` summary works too.

```

<table summary="Names and Ages of My Coworkers">  <caption>    Names and Ages of My Coworkers  </caption>  <thead>    <tr>      <th scope="col">Firstname</th>      <th scope="col">Lastname</th>      <th scope="col">Age</th>Copy to clipboardShow more

```

### Designing accessible data visualizations

Consider visually impaired users when including data visualizations. Consider
accompanying visuals with a data table as an alternative for users who rely on
screen readers. Also consider color choices for color-blind users.

### Multimedia text alternatives

Every image that is not decorative must include `alt` text with a meaningful
description of the image. If the image is decorative, use an empty `alt`
attribute; otherwise the screen reader will read the whole image URL if the
`alt` is left out.

```

<img src="puppy.jpg" alt="Sleeping puppy in a cup" />Copy to clipboard

```

```

<img src="puppy.jpg" alt="" />Copy to clipboard

```

### Audio alternatives

Provide closed-captioning with videos or transcriptions of audio files.

```

<video controls>  <source src="example.mp4" type="video/mp4" />  <source src="example.webm" type="video/webm" />  <track kind="subtitles" src="subtitles_english.vtt" srclang="en" /></video>Copy to clipboard

```

### Avoid font icon libraries

Use SVG’s instead of font icon libraries.

```

<svg width="80" height="10">  <line class="line" x1="200" y1="0" x2="0" y2="0" /></svg>Copy to clipboard

```

### Utilize ARIA roles and landmark roles

ARIA (Accessible Rich Internet Application) roles convey the intent or meaning
of an element to assistive technology. This helps users navigate when they can’t
see the layout and provides further context about different functionalities.

Landmark roles identify regions in a page, and act much like native HTML tags
would when it comes to semantics. Signpost roles describe other information
about a given element’s functionality on a page. These are especially helpful
when building complex, custom interfaces or to reinforce semantics in native
HTML elements.

```

<nav role="navigation"></nav><main role="main"></main>Copy to clipboard

```

```

<div role="banner">This is a banner.</div><div role="tabgroup"><div role="tab"></div></div><div role="combobox"></div><div role="slider"></div><button role="button"></button>Copy to clipboard

```

## CSS best practices

### CSS rule of thumb

You can style a page feature to fit your design, but don’t change it to the
point that it doesn’t look or behave as expected.

### Style focus indicators

Add styling to tabbable elements on hover and focus, so that keyboard-only users
can have a clear visual of where they are navigating. Never suppress the focus
indicator altogether.

### Hiding elements

When hiding content from a screen reader, consider source order. Use
`visibility: hidden`, along with `display: none` in your CSS.

## Mouse-specific events

Double up mouse-specific events with other events for keyboard-only users.

```

const foo = document.querySelector('.foo-class');
foo.onmouseover = someFunction();
foo.onmouseout = anotherFunction();
foo.onfocus = someFunction();
foo.onblur = anotherFunction();Copy to clipboard

```

## Code samples

```
<button>Play Video</button><header></header><main></main><nav></nav><footer></footer><aside></aside><section></section><article></article>Copy to clipboard
```

```html
<button>Play Video</button><header></header><main></main><nav></nav><footer></footer><aside></aside><section></section><article></article>
```

```
"9 to 5" "November" <abbr title="November">Nov</abbr>Copy to clipboard
```

```html
"9 to 5" "November" <abbr title="November">Nov</abbr>
```

```
<a>Read more about pricing</a>Copy to clipboard
```

```html
<a>Read more about pricing</a>
```

```
<a>Click here</a>Copy to clipboard
```

```html
<a>Click here</a>
```

```
<table summary="Names and Ages of My Coworkers">  <caption>    Names and Ages of My Coworkers  </caption>  <thead>    <tr>      <th scope="col">Firstname</th>      <th scope="col">Lastname</th>      <th scope="col">Age</th>Copy to clipboardShow more
```

```html
<table summary="Names and Ages of My Coworkers">  <caption>    Names and Ages of My Coworkers  </caption>  <thead>    <tr>      <th scope="col">Firstname</th>      <th scope="col">Lastname</th>      <th scope="col">Age</th>
```

```
<img src="puppy.jpg" alt="Sleeping puppy in a cup" />Copy to clipboard
```

```html
<img src="puppy.jpg" alt="Sleeping puppy in a cup" />
```

```
<img src="puppy.jpg" alt="" />Copy to clipboard
```

```html
<img src="puppy.jpg" alt="" />
```

```
<video controls>  <source src="example.mp4" type="video/mp4" />  <source src="example.webm" type="video/webm" />  <track kind="subtitles" src="subtitles_english.vtt" srclang="en" /></video>Copy to clipboard
```

```html
<video controls>  <source src="example.mp4" type="video/mp4" />  <source src="example.webm" type="video/webm" />  <track kind="subtitles" src="subtitles_english.vtt" srclang="en" /></video>
```

```
<svg width="80" height="10">  <line class="line" x1="200" y1="0" x2="0" y2="0" /></svg>Copy to clipboard
```

```html
<svg width="80" height="10">  <line class="line" x1="200" y1="0" x2="0" y2="0" /></svg>
```

```
<nav role="navigation"></nav><main role="main"></main>Copy to clipboard
```

```html
<nav role="navigation"></nav><main role="main"></main>
```

```
<div role="banner">This is a banner.</div><div role="tabgroup"><div role="tab"></div></div><div role="combobox"></div><div role="slider"></div><button role="button"></button>Copy to clipboard
```

```html
<div role="banner">This is a banner.</div><div role="tabgroup"><div role="tab"></div></div><div role="combobox"></div><div role="slider"></div><button role="button"></button>
```

```
const foo = document.querySelector('.foo-class');
foo.onmouseover = someFunction();
foo.onmouseout = anotherFunction();
foo.onfocus = someFunction();
foo.onblur = anotherFunction();Copy to clipboard
```

```javascript
const foo = document.querySelector('.foo-class');
foo.onmouseover = someFunction();
foo.onmouseout = anotherFunction();
foo.onfocus = someFunction();
foo.onblur = anotherFunction();
```

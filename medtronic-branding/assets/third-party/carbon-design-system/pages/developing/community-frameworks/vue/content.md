# Community frameworks – Carbon Design System

Source: https://www.carbondesignsystem.com/developing/community-frameworks/vue/

# Community frameworks

The library provides front-end developers & engineers a collection of reusable
Vue components to build websites and user interfaces. Adopting the library
enables developers to use consistent markup, styles, and behavior in prototype
and production work.

The Vue library is maintained by members of the Carbon community. For support,
contact the
[Carbon Vue team](https://github.com/carbon-design-system/carbon-components-vue/issues/new/choose).

## Resources

## Getting started

Assuming we’re starting with a new Vue CLI project:

```

npm create vue@latestcd vue-projectCopy to clipboard

```

```

npm install @carbon/vueCopy to clipboard

```

In src/main.js, after `import App from './App.vue'`, add the following to
include the carbon styles and components.

```

import 'carbon-components/css/carbon-components.css';import CarbonComponentsVue from '@carbon/vue';
const app = createApp(App);app.use(CarbonComponentsVue);app.mount('#app');// remove the line: createApp(App).mount('#app')Copy to clipboard

```

Replace the contents of src/components/HelloWorld.vue with the following

```

<script setup>  import { ref } from 'vue';
  const yourName = ref('');  const visible = ref(false);  function onClick() {    visible.value = true;  }  function modalClosed() {Copy to clipboardShow more

```

That’s it! Now start the server and start building.

```

npm run devCopy to clipboard

```

_Note: This isn’t the only way to bootstrap a_ `carbon-components-vue`
_application, but the combination of_ `Vue CLI` _and the_ `carbon-components`
_scss is our recommended setup._ See
[Hello carbon vue3](https://github.com/IBM/hello-carbon-vue3) for a complete
example app.

### List of available components

View available Vue Components [here](http://vue.carbondesignsystem.com/). Usage
information is available in the notes provided with each story.

## Troubleshooting

If you experience any issues while getting set up with Carbon Components Vue,
please head over to the
[GitHub repo](https://github.com/carbon-design-system/carbon-components-vue) for
more guidelines and support. Please
[create an issue](https://github.com/carbon-design-system/carbon-components-vue/issues)
if your issue does not already exist.

## Code samples

```
npm create vue@latestcd vue-projectCopy to clipboard
```

```bash
npm create vue@latestcd vue-project
```

```
npm install @carbon/vueCopy to clipboard
```

```bash
npm install @carbon/vue
```

```
import 'carbon-components/css/carbon-components.css';import CarbonComponentsVue from '@carbon/vue';
const app = createApp(App);app.use(CarbonComponentsVue);app.mount('#app');// remove the line: createApp(App).mount('#app')Copy to clipboard
```

```js
import 'carbon-components/css/carbon-components.css';import CarbonComponentsVue from '@carbon/vue';
const app = createApp(App);app.use(CarbonComponentsVue);app.mount('#app');// remove the line: createApp(App).mount('#app')
```

```
<script setup>  import { ref } from 'vue';
  const yourName = ref('');  const visible = ref(false);  function onClick() {    visible.value = true;  }  function modalClosed() {Copy to clipboardShow more
```

```html
<script setup>  import { ref } from 'vue';
  const yourName = ref('');  const visible = ref(false);  function onClick() {    visible.value = true;  }  function modalClosed() {
```

```
npm run devCopy to clipboard
```

```bash
npm run dev
```

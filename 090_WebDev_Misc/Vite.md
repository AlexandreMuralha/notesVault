
[Vite](https://vitejs.dev/) is a no bundler DEV environment for Vue.js.

Vite is a **build tool that significantly improves the front-end development experience**. You can use Vite to set up a development environment for frameworks like Vue and React, and even for a vanilla JavaScript app with a dev server and hot reloading in just three commands.

---
#### Create Vite Project
npm:
```
$ npm init vite@latest
```

Yarn:
```
$ yarn create vite
```

Then follow the prompts!

You can also directly specify the project name and the template you want to use via additional command line options. For example, to scaffold a Vite + Vue project, run:

```
# npm 6.x
npm init vite@latest my-vue-app --template vue

# npm 7+, extra double-dash is needed:
npm init vite@latest my-vue-app -- --template vue

# yarn
yarn create vite my-vue-app --template vue
```

See [create-vite](https://github.com/vitejs/vite/tree/main/packages/create-vite) for more details on each supported template: `vanilla`, `vanilla-ts`, `vue`, `vue-ts`, `react`, `react-ts`, `preact`, `preact-ts`, `lit`, `lit-ts`, `svelte`, `svelte-ts`.

---
https://vitejs.dev/

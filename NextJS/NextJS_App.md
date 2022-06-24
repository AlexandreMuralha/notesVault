---
title: NextJs _App
date: 2021-09-25T20:47
---


# NextJs `./pages/_app.js`

Os imports passados para o ficheiro `./pages/_app.js` serão passados para todas as pages.

---

Next.js usa o componente `App` para inicializar as páginas, de forma a obter controle sobre esse processo de inicialização das páginas, podemos criar, caso não exista, o ficheiro `./pages/_app.js`, o qual permite:
- Persistir o Layout entre páginas.
- Manter o estado a quando da navegação entre páginas
- error handling usando `componentDidCatch`
- Injetar data adicional nas pages
- Adicionar estilos CSS globais [Add global CSS](https://nextjs.org/docs/basic-features/built-in-css-support#adding-a-global-stylesheet)

Exemplo Ficheiro `./pages/_app.js` : 

```jsx
// import App from 'next/app'

function MyApp({ Component, pageProps }) {
 	return (
		<div>
		
			<Component {...pageProps} />
			
		</div>
	);
}

// Only uncomment this method if you have blocking data requirements for
// every single page in your application. This disables the ability to
// perform automatic static optimization, causing every page in your app to
// be server-side rendered.
//
// MyApp.getInitialProps = async (appContext) => {
//   // calls page's `getInitialProps` and fills `appProps.pageProps`
//   const appProps = await App.getInitialProps(appContext);
//
//   return { ...appProps }
// }

export default MyApp
```

The `Component` prop is the active `page`, so whenever you navigate between routes, `Component` will change to the new `page`. Therefore, any props you send to `Component` will be received by the `page`.

`pageProps` is an object with the initial props that were preloaded for your page by one of our [data fetching methods](https://nextjs.org/docs/basic-features/data-fetching), otherwise it's an empty object.

---
**ID**:  2109252047
**tags**: #
**links**: https://nextjs.org/docs/advanced-features/custom-app

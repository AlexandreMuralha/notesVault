# NextJS Pre-rendering
---

## [Pre-rendering](https://nextjs.org/docs/basic-features/pages#pre-rendering)

By default, Next.js **pre-renders** every page. This means that Next.js generates HTML for each page in advance, instead of having it all done by client-side JavaScript. Pre-rendering can result in better performance and SEO.

Each generated HTML is associated with minimal JavaScript code necessary for that page. When a page is loaded by the browser, its JavaScript code runs and makes the page fully interactive. (This process is called _hydration_.)

### [Two forms of Pre-rendering](https://nextjs.org/docs/basic-features/pages#two-forms-of-pre-rendering)

Next.js has two forms of pre-rendering: **Static Generation** and **Server-side Rendering**. The difference is in **WHEN** it generates the HTML for a page.

-   [**Static Generation (Recommended)**](https://nextjs.org/docs/basic-features/pages#static-generation-recommended): The HTML is generated at **build time** and will be reused on each request.
-   [**Server-side Rendering**](https://nextjs.org/docs/basic-features/pages#server-side-rendering): The HTML is generated on **each request**.

Importantly, Next.js lets you **choose** which pre-rendering form you'd like to use for each page. You can create a "hybrid" Next.js app by using Static Generation for most pages and using Server-side Rendering for others.

> We **recommend** using **Static Generation** over Server-side Rendering for performance reasons. Statically generated pages can be cached by CDN with no extra configuration to boost performance. However, in some cases, Server-side Rendering might be the only option.

You can also use **Client-side Rendering** along with Static Generation or Server-side Rendering. That means some parts of a page can be rendered entirely by client side JavaScript. To learn more, take a look at the [Data Fetching](https://nextjs.org/docs/basic-features/data-fetching#fetching-data-on-the-client-side) documentation.

If your app is a plain React.js app (without Next.js), there’s no [pre-rendering](https://nextjs.org/docs/basic-features/pages#pre-rendering), so you won’t be able to see the app if you disable JavaScript. For example:

-   Enable JavaScript in your browser and [check out this page](https://create-react-app.examples.vercel.com/). This is a plain React.js app built with [Create React App](https://create-react-app.dev/).
-   Now, disable JavaScript and access [the same page](https://create-react-app.examples.vercel.com/) again.
-   You won’t see the app anymore — instead, it’ll say “You need to enable JavaScript to run this app.” This is because the app is not pre-rendered into static HTML.

### When to Use [Static Generation](https://nextjs.org/docs/basic-features/pages#static-generation-recommended) v.s. [Server-side Rendering](https://nextjs.org/docs/basic-features/pages#server-side-rendering)

We recommend using [**Static Generation**](https://nextjs.org/docs/basic-features/pages#static-generation-recommended) (with and without data) whenever possible because your page can be built once and served by CDN, which makes it much faster than having a server render the page on every request.

You can use [Static Generation](https://nextjs.org/docs/basic-features/pages#static-generation-recommended) for many types of pages, including:

-   Marketing pages
-   Blog posts
-   E-commerce product listings
-   Help and documentation

You should ask yourself: "Can I pre-render this page **ahead** of a user's request?" If the answer is yes, then you should choose [Static Generation](https://nextjs.org/docs/basic-features/pages#static-generation-recommended).

On the other hand, [Static Generation](https://nextjs.org/docs/basic-features/pages#static-generation-recommended) is **not** a good idea if you cannot pre-render a page ahead of a user's request. Maybe your page shows frequently updated data, and the page content changes on every request.

In that case, you can use [**Server-side Rendering**](https://nextjs.org/docs/basic-features/pages#server-side-rendering). It will be slower, but the pre-rendered page will always be up-to-date. Or you can skip pre-rendering and use client-side JavaScript to populate frequently updated data.

---
**ID**:  2109211726
**tags**: #
**links**:

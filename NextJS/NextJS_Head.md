
next/head is a Built-in component for appending elements to the `head` of the page:

```Javascript
import Head from "next/head";
  
function HomePage() {
	return (
		 <>
		 <Head>
			 <title>Home</title>
			 <meta name="description" value="This is a blog" />
		 </Head>
		 <main>
			 <h1>My Blog</h1>
		 </main>
		 </>
 	)
}

export default HomePage;
```


https://nextjs.org/docs/api-reference/next/head
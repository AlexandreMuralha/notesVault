# Sitemap
O sitemap.xml é um arquivo que tem a finalidade de listar as páginas de um site que gostaríamos de ter presentes nos resultados de busca.

https://www.sitemaps.org/protocol.html

### 💡 Exemplo 

```xml

<?xml version="1.0" encoding="UTF-8"?>

<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">

    <url>
        <loc>https://www.omeusite.com/</loc>
        <lastmode>2020-01-01</lastmode>
        <changefreq>monthly</changefreq>
        <priority>0.8</priority>
    </url>

    <url>
        <loc>https://www.omeusite.com/about</loc>
        <lastmode>2020-01-01</lastmode>
        <changefreq>monthly</changefreq>
        <priority>0.7</priority>
    </url>

    <url>
        <loc>https://www.omeusite.com/projects</loc>
        <lastmode>2020-01-01</lastmode>
        <changefreq>monthly</changefreq>
        <priority>0.6</priority>
    </url>
    
</urlset>

```


### Tags

`<urlset>` 
- required
- Encapsulates the file and references the current protocol standard.

`<url>`
- required
- Parent tag for each URL entry. The remaining tags are children of this tag.

`<loc>`
- required
- URL of the page. This URL must begin with the protocol (such as http) and end with a trailing slash, if your web server requires it. This value must be less than 2,048 characters.

`<lastmod>`
- **optional**
- The date of last modification of the page. This date should be in [W3C Datetime](http://www.w3.org/TR/NOTE-datetime) format. This format allows you to omit the time portion, if desired, and use YYYY-MM-DD.
- Note that the date must be set to the date the linked page was last modified, not when the sitemap is generated.
- Note also that this tag is separate from the If-Modified-Since (304) header the server can return, and search engines may use the information from both sources differently.

`<changefreq>`
- **optional**
- How frequently the page is likely to change. This value provides general information to search engines and may not correlate exactly to how often they crawl the page. Valid values are: ``always, hourly, daily, weekly, monthly, yearly, never.``

- The value "always" should be used to describe documents that change each time they are accessed. The value "never" should be used to describe archived URLs.
- Please note that the value of this tag is considered a _hint_ and not a command. Even though search engine crawlers may consider this information when - making decisions, they may crawl pages marked "hourly" less frequently than that, and they may crawl pages marked "yearly" more frequently than that. Crawlers may periodically crawl pages marked "never" so that they can handle unexpected changes to those pages.

`<priority>`
**optional**
- The priority of this URL relative to other URLs on your site. Valid values range from 0.0 to 1.0. This value does not affect how your pages are compared to pages on other sites—it only lets the search engines know which pages you deem most important for the crawlers.
- The default priority of a page is 0.5.
- Please note that the priority you assign to a page is not likely to influence the position of your URLs in a search engine's result pages. Search engines may use this information when selecting between URLs on the same site, so you can use this tag to increase the likelihood that your most important pages are present in a search index.
- Also, please note that assigning a high priority to all of the URLs on your site is not likely to help you. Since the priority is relative, it is only used to select between URLs on your site.



### Adding the sitemap.xml to your React/Angular App

The next step is to add your sitemap.xml file to your app. You should copy and paste the file into the base of your Angular app in the /src folder.

If you're not sure if you are adding it to the right folder, the /src folder should contain your index.html, main.ts, and `robots.txt` files that make up the base of your Angular App.

```json
.........
"prefix": "app", 
"architect": 
    { "build": { 
        "builder": "@angular-devkit/build-angular:browser", 
        "options": { 
            "outputPath": "public", 
            "index": "src/index.html", 
            "main": "src/main.ts", 
            "polyfills": 
            "src/polyfills.ts", 
            "tsConfig": 
            "tsconfig.app.json", 
            "aot": true, 
            "assets": [ 
                "src/favicon.ico", 
                "src/assets", 
                "src/robots.txt", 
                "src/sitemap.xml", 
            ],
    ...................
```
# NextJS
---
Next.js é um framework front-end React de código aberto criada por Vercel que permite funcionalidades como renderização do lado do servidor e geração de sites estáticos para aplicativos da web baseados em React.


[[NextJS_Pre-rendering]]
[NextJS_App](NextJS_App.md)

---


### CLI Commands:
create-next-app:
```bash
yarn create next-app
npx create next-app
npx create-next-app my-app-name
npx create-next-app --ts //typescript project
```


Dev, build and start:
```bash
yarn dev  //starts the application in development mode with hot-code reloading and error reporting.
npx next dev -p 4000 ////starts the application in development mode at http://localhost:4000 
// instead of: http://localhost:3000 (default)

yarn build   // creates an optimized production build of your application. The output displays information about each route.
yarn start   //starts the application in production mode. The application should be compiled with next build first.

```

Telemetry:
```bash
npx next telemetry disable // opt-out
npx next telemetry status // check the status of telemetry collection
```

---
**ID**:  2109101456
**tags**: #
**links**:

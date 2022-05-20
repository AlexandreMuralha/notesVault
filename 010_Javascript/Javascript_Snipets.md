# Javascript Snipets
[Array](#Array)
[Date](#Date)
[Number](#Number)
[String](#String)
[DOM](#DOM)
[Function](#Function)
[Misc](#Misc)


## Array
### Shuffle an Array

Shuffling an array is super easy with `sort` and `random` methods.  

```javascript
const shuffleArray = (arr) => arr.sort(() => 0.5 - Math.random());

console.log(shuffleArray([1, 2, 3, 4]));
// Result: [ 1, 4, 3, 2 ]
```
### Remove Duplicated from Array

You can easily remove duplicates with `Set` in JavaScript. Its a life saver.  

```javascript
const removeDuplicates = (arr) => [...new Set(arr)];

console.log(removeDuplicates([1, 2, 3, 3, 4, 4, 5, 5, 6]));
// Result: [ 1, 2, 3, 4, 5, 6 ]
```

### Convert an array of strings to numbers

```jsx
const toNumbers = arr => arr.map(Number);
// Or
const toNumbers = arr => arr.map(x => +x);
// toNumbers(['2', '3', '4']) returns [2, 3, 4]
```

### Check if an array contains a value matching some criterias

```jsx
const contains = (arr, criteria) => arr.some(v -> criterias(v));
// contains([10, 20, 30], v => v > 25 )  === true
// contains([10, 20, 30], v => v > 100 || v < 15 )  === true
// contains([10, 20, 30], v => v > 100 )  === false
```

### Find the maximum / minimum item of an array

```jsx
const max = arr => Math.max(...arr);
const min = arr => Math.min(...arr);
```

### Get a random item from an array

```jsx
const randomItem = arr => arr[(Math.random() * arr.length) | 0];
```

### Merge two arrays

```jsx
// Merge but don't remove the duplications
const merge = (a, b) => a.concat(b);
// Or
const merge = (a, b) => [...a, ...b];

// Merge and remove the duplications
const merge = [...new Set(a.concat(b))];
// Or
const merge = [...new Set([...a, ...b])];
```

### Difference between two arrays

```jsx
const difference = (a, b) => {  
	const s = new Set(b);  
	return a.filter(x => !s.has(x));
};

difference([1, 2, 3], [1, 2, 4]); // [3]
//This snippet finds the difference between two arrays.
```

---

## Date

### Calculate the number of difference days between two dates

```jsx
const diffDays = (date, otherDate) => Math.ceil(Math.abs(date - otherDate) / (1000 * 60 * 60 * 24));
// diffDays(new Date('2014-12-19'), new Date('2020-01-01')) === 1839
```

### Check if a date is between two dates

```jsx
// `min`, `max` and `date` are `Date` instances
const isBetween = (date, min, max) => (date.getTime() >= min.getTime() && date.getTime() <= max.getTime());
```

### Check if a date is today

```jsx
// `date` is a Date object
const isToday = (date) => date.toISOString().slice(0, 10) === new Date().toISOString().slice(0, 10);
```

### Convert a date to yyyy mm dd format

```jsx
// `date` is a `Date` object
const formatYmd = date => date.toISOString().slice(0, 10);
// formatYmd(new Date()) returns `2020-05-06`
```

### Get the current timestamp in seconds

```jsx
const ts = () => Math.floor(new Date().getTime() / 1000);
```

### Get the month name of a date

```jsx
// `date` is a Date object
const getMonthName = date => ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',' November', 'December'][date.getMonth()];
```

### Get the number of days in given month

```jsx
// `month` is zero-based index
const daysInMonth = (month, year) => new Date(year, month, 0).getDate();
```

### Get the weekday of a date

```jsx
// `date` is a Date object
const getWeekday = date => ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday',
```

---

## Number

### Generate a random floating point number in given range

```jsx
const randomFloat = (min, max) => Math.random() * (max - min) + min;
```

### Generate a random integer in given range

```jsx
const randomInteger = (min, max) => Math.floor(Math.random() * (max - min + 1)) + min;
```

### Find Average of Numbers

Find the average between multiple numbers using `reduce` method.  

```jsx
const average = (...args) => args.reduce((a, b) => a + b) / args.length;

average(1, 2, 3, 4);
// Result: 2.5
```
---

## String

### Capitalize a string

```jsx
const capitalize = str => `${str.charAt(0).toUpperCase()}${str.slice(1)}`;
// capitalize('hello world') === 'Hello world'
```

### Reverse a string
You can easily reverse a string using `split`, `reverse` and `join` methods.  

```jsx
const reverse = str => str.split('').reverse().join('');

reverse('hello world');     
// Result: 'dlrow olleh'
```

---

## DOM

### Array to html list

```jsx
const arrayToHtmlList = (arr, listID) =>  
	(el => (    
		(el = document.querySelector('#' + listID)),    
		(el.innerHTML += arr.map(item => `<li>${item}
</li>`).join(''))  
	))();

arrayToHtmlList(['item 1', 'item 2'], 'myListID');
// converts the elements of an array into  <li>  tags and appends them to the list of the given ID.
```

### Returns current URL

```jsx
const currentURL = () => window.location.href;
//This snippet returns the current URL
```

---

## Function

### Create an empty function

```jsx
const noop = () => {};
// Or
const noop = Function.prototype;
```

---

## Misc

### Generate a Random Hex Color

```jsx
var randomColor = 
Math.floor(Math.random()*16777215).toString(16);
```

### Emulate a dice throw

```jsx
const throwdice = () => ~~(Math.random() * 6) + 1;
```

### Wait for an amount of time

```jsx
const wait = async (milliseconds) => new Promise((resolve) => setTimeout(resolve, milliseconds)
```

### Toggle (Show/Hide) element

```jsx
function toggle_visibility(id) {     
		var e = document.getElementById(id);     
		if(e.style.display == 'block') e.style.display = 'none';     
		else e.style.display = 'block'; 
}
```
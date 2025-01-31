# Referencing and Outsourcing in Coding

## Introduction
My Cogrammar Bootcamp has a plagiarism policy, I'm going to take myse;f through the best ways to reference my work as I go through the bootcamp.

## Outsourcing is Key to Coding!
One of the things I'll notice fairly early on in my coding journey is that in order to deal with the steep learning curve, I'm going to need to get help from somewhere. They provide with mentor support specifically for this purpose, but Cogrammar also encourages that I look up my questions online, ask fellow students, or even get help from friends and family members!

While this may seem an odd thing to encourage, learning to find help from others is one of the most important lessons they hope I will learn during your time with us because it will be a huge portion of your problem-solving process when I get out into the real world.

However, seeing as this is my coding journey (not your cousin’s or the guy on StackOverflow), we want to see that myself is learning while asking for help, not just blindly copy-pasting someone else’s code.

So where I have received help, simply add an inline comment to my code describing where I got the help from, why I needed the help, and what changes you made to the original code, if necessary.

---

### Examples of Referencing

#### JavaScript Example
```javascript
// Used the Mozilla Developer Network's reference for class expressions to parameterise the superclass:
// https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/class
// I wasn't sure of the superclass beforehand but I wanted to write my subclass
// I made the code in the article a function
const derive = Parent => class Child extends Parent { }

# Javascript Missions

### Mission 1

Challenge link [here](https://www.hackthissite.org/missions/javascript/1/)

There is a javascript function which checks input with the string "cookies". If matches give the password otherwise alert "Fail".

```javascript

function check(x)
{
        if (x == "cookies")
        {
                        alert("win!");
                        window.location += "?lvl_password="+x;
        } else {
                        alert("Fail D:");
	}
}

```

Input = **cookies**

----

### Mission 2

Challenge link [here](https://www.hackthissite.org/missions/javascript/2/)

In this challenge, we are redirected to another page using javascript. Just block the javascript from your browser to win.

----

### Mission 3

Challenge link [here](https://www.hackthissite.org/missions/javascript/3/)

This time some javascript code is given.

```javascript

var foo = 5 + 6 * 7 
var bar = foo % 8
var moo = bar * 2
var rar = moo / 3
function check(x)
{
        if (x.length == moo)
        {
                        alert("win!");
                        window.location += "?lvl_password="+x;
        } else {
                        alert("fail D:");
	 }
}

```

Decoding

```
	foo = 5 + 6 * 7 = 47
	bar = foo % 8 = 47 % 8 = 7
	moo = bar * 2 = 7 * 2 = 14
	rar = moo / 3 = 14 / 3 = 4

```

If input string's length is equal to 14, then we will pass this challenge.

----

### Mission 4

Challenge link [here](https://www.hackthissite.org/missions/javascript/4/) 

```javascript

RawrRawr = "moo";
function check(x)
{
        "+RawrRawr+" == "hack_this_site"
	if (x == ""+RawrRawr+"")
        {
		alert("Rawr! win!");
                window.location = "../../../missions/javascript/4/?lvl_password="+x;
        } else {
		alert("Rawr, nope, try again!");
	}
}

```

Use your javascript console, copy paste the code and get the value of variable "+RawrRawr+" which is equal to "moo" itself.

----

### Mission 5

Challenge link [here](https://www.hackthissite.org/missions/javascript/5/) 

```javascript

moo = unescape('%69%6C%6F%76%65%6D%6F%6F');
      function check (x) {
        if (x == moo)
        {
          alert("Ahh.. so that's what she means");
          window.location = "../../../missions/javascript/5/?lvl_password="+x;
        }
        else {
          alert("Nope... try again!");
        }
}

```

Get the value of variable moo from the console.

moo = "ilovemoo"

----

### Mission 6

Challenge link [here](https://www.hackthissite.org/missions/javascript/6/) 

```javascript

RawrRawr = "moo";
function check(x)
{
"+RawrRawr+" == "hack_this_site"
if (x == ""+RawrRawr+"")
{
alert("Rawr! win!");
window.location = "about:blank";
} else {
alert("Rawr, nope, try again!");
}
}

function checkpassw(moo)
{
RawrRawr = moo;
checkpass(RawrRawr);
}

```

After looking at the source code we find that Check Password is calling the function checkpass(), which is not defined in the above code. Looking at the source code again, we find that there is an external javascript file named checkpass.js. On opening this we found the code of the function checkpass().

```javascript

dairycow="moo";
moo = "pwns";
rawr = "moo";

function checkpass(pass)
{
if(pass == rawr+" "+moo)
{	
alert("How did you do that??? Good job!");
window.location = "../../../missions/javascript/6/?lvl_password="+pass;
} else {
alert("Nope, try again");
}
}

```

Here function checkpass() compare the input with "moo pwns".

Input = **moo pwns**

----

### Mission 7

Challenge link [here](https://www.hackthissite.org/missions/javascript/7/)

This is JS Obfuscation. I use [this](http://www.dcode.fr/javascript-unobfuscator) online tool to decode. After that, with the help of the console, i was able to make the code into readable format.

```

<button onclick='javascript:if (document.getElementById("pass").value=="j00w1n"){alert("You WIN!");window.location += "?lvl_password="+document.getElementById("pass").value}else {alert("WRONG! Try again!")}'>Check Password</button>

```

Input = **j00w1n**


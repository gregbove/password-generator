# Password Generator

## OVERVIEW

I wrote this program in attempt to solve a fun password management problem I have been having lately. More specifically, I was trying to find a balance between the following _two_ problems:

- I didn't want all of my passwords to be _the same_
- I didn't want all of my passwords to be _different_

Fun problem, huh?

## The Solution

TL; DR - I take my universal passcode, add the platform name, take a hash of that value, trim it to a length I like, and then add some special characters to make sure it passes as a password.

### PART ONE

So I want to be able to have a bunch of passwords, while only remembering 1? I have an idea! The password for each platform will just be the password I remember, and then the platform's name. Let's see what my passwords look like, with my dog's name (Buster) as my main password!

| Platforms | Platform Passwords |
| :-------: | :----------------: |
| Instagram |  BusterInstagram   |
|  Twitter  |   BusterTwitter    |
| Discover  |   BusterDiscover   |

Not exacly 'secure' passwords...

### PART TWO

So, I'll take a hash based on the name of the platform that the password is for, along with the only password I am caring to remember! I am mentioning this special password a lot, so lets give it a name - `universal_password`.

| Platform  | Value Getting Hashed |                             Password                             |
| :-------: | :------------------: | :--------------------------------------------------------------: |
| Instagram |   BusterInstagram    | dd19d69f912e3768c25b722148f2322355323505f8ee65baf3c79267d211fa97 |
|  Twitter  |    BusterTwitter     | 1beb8fb7252c91fa1aeaf458e6dea39a5c348a6be2f39638679e229dffcd1643 |
| Discover  |    BusterDiscover    | a8dd0d030e7455ccba63a62c23abdc6c88e2f6170ccb9becbce17e57fafa55dc |

Ehhh... okay, they're complicated and different! But those are too long and complicated. What if I need to type it out by hand? And what about passwords requiring that a special character is added? Or a number?

### PART THREE

Lets configure these passwords a bit more to my liking.

First, let's consider the problem of length - Right away, I can tell that a password like the ones in the table above would be _quite_ difficult to type out, if needed. So, let's take a substring of some length and only take the first few characters of the hash. For that, I have defined a constant of `PASSWORD_HASH_LENGTH`, which I think 16 is a fair value for.

Next, let's consider the problem of complexity - Most platforms will require that a password has some capitals, some special characters, etc. For that, I'll just append a string with these funky characters to the end of the hash - and I defined this as `RULE_SATISFYING_STRING`.

Let's look at an example with this again! (_With `universal_password=Buster`, `PASSWORD_HASH_LENGTH=16`, `RULE_SATISFYING_STRING=aA123!?$`_)

| Platform  | Value Getting Hashed |         Password         |
| :-------: | :------------------: | :----------------------: |
| Instagram |   BusterInstagram    | dd19d69f912e3768aA123!?$ |
|  Twitter  |    BusterTwitter     | 1beb8fb7252c91faaA123!?$ |
| Discover  |    BusterDiscover    | a8dd0d030e7455ccaA123!?$ |

Much more digestable, and not horrible to copy!

Speaking of copying - I added a few lines to copy the password to your clipboard when the program is run, so you can simply paste the password into wherever you are entering the value.

## Other Solutions

Yes, I am sure there are other routes I could go.

- Use some password manager
- Write down these passwords in a book somewhere
- ~~Be better at remebering~~

But what's the fun in that?

## Future

I would like to get this running on my IPhone, so I could simply generate the password and then paste it into whatever app I am in.

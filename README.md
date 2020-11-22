## luhnpy

**A simple implementation of luhn algorithm in Python.**

### What is luhn algorithm?

**The Luhn algorithm, also known as the Luhn formula or module 10, tests the sum of the numbers in the card number and indicates whether the quantities are equal to what is predicted or if there is an error in the sequence of numbers.**

## How luhn works?

### Step 1

**The algorithm starts at the end of the number, from the most right digit to the first left digit. Double all digits of even rank.**

![luhn](https://help.objectiflune.com/files/howto-luhndigit-1.png)

### Step 2

**If the double of a digit is equal or greater than 10, replace the result by the sum of digits in the double. Alternatively, simply take away 9 from the result of the double.**

![luhn](http://help.objectiflune.com/files/howto-luhndigit-2.png)

**Then sum all the digits: 8+(1+4)+2+(1+0)+6+(0)+0+(4)+1+(8)+3+(1+8)+7+(8)+6+(8)+4+(1+0) = 81**

### Step 3

**The control digit number is equal to 10-(sum%10): 10-(81%10) =10-1=9 The Luhn Check Digit at position 19 will, therefore, be 9.**

**Font: https://learn.objectiflune.com/howto/calculating-luhn-check-digit-connect/**

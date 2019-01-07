# securus
A way to generate secure and unique passwords and not even having to store then. 
By entering in unique parameters, such as your email, a master password, and other information, a unique password is generated. 
This password is generated through SHA256 with a random salt. PBKDF2 is also used, with a 100,000 iterations, it becomes harder 
to brute force the password generated.

How it works:

Using SHA256 and variable salts,  a unique string is produced. This string, along with PBDKF2 with 100, iterations makes this string more secure and harder to crack.

The string produced is then used to create another one, which can contain:

	Lowercase
	Uppercase
	Numbers
	Special characters

if the user desires. 

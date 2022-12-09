#Chapter 2 - Exercise 3
#Stripping names - Tidy up a code so its easier to understand
name = (f"  Arwen\t") #A value that has whitespace characters
print(f"Text before .strip: \n'{name}'") 
name = name.strip() #Removes the whitespace characters
print(f"\nText after .strip: \n'{name}'")
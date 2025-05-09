### Given the time in numerals, we may convert it into words, as shown below:

      5:00 -> five o' clock
      5:01 -> one minute past five
      5:10 -> ten minutes past five
      5:15 -> quarter past five
      5:30 -> half past five
      5:40 -> twenty minutes to six
      5:45 -> quarter to six
      5:47 -> thirteen minutes to six
      5:28 -> twenty eight minutes past five

- At minutes = 0. use o' clock. For 1 ≤ minutes ≤ 30, use past, and for 30 < minutes use to. Note the space between the apostrophe and clock in o'clock. 
# Function Description
- Complete the timelnWords function in the editor below.
- timelnWords has the following parameter(s):
  
        int h: the hour of the day
        int m: the minutes after the hour
- Returns
  
      string: a time string as described

# Input Format
- The first line contains h, the hours portion.
-  The second line contains m, the minutes portion

# Constraints
- 1 <= h <= 12
- 0 <= m <= 59

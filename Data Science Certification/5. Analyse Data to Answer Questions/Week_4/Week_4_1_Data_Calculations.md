Revision on fuunction 
_ Use conditional formating on a Row. We can choose color ratio as per the greatness of a number from white to a chosen color.

More on Functions 

=COUNTIF("Value", Range)
=SUMIF(B3:B50,">1",C3:C50) - ("Where tocheck", What to check, "What to add ")
=AVERAGEIF(B3:B50,">1",C3:C50) - Same as above

To check Multiple criterions
 =SUMIFS(sum_range, criteria_range1, criterion1, [criteria_range2, criterion2, ...])
 =COUNTIFS(criteria_range1, criterion1, [criteria_range2, criterion2, ...])
 =MAXIFS(max_Range,criteria_range1, criterion1, [criteria_range2, criterion2, ...]) -This is a bit different from the othersmentioned above. The reason being that it will find the max only in a given range. The rest are just if conditions that need to be true 

 More functions
 https://www.coursera.org/learn/analyze-data/supplement/s9khi/functions-with-multiple-conditions


Composite function 

SUMPRODUCT is a function that multiplies arrays and returns the sum of those products
You Multiply and then you return the SUM of the results
=SUMPRODUCT(B3:B7,C3:C7)
=SUMPRODUCT(Range1,Range2)
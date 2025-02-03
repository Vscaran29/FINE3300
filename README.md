The following code calculates for the users’ mortgage payment based on parameters set out.


The function requires users to provide the following 3 key inputs in the specified format to receive the output:

1)	Principal amount- The $ amount outstanding on the mortgage
2)	Rate- The annual interest rate associated with the mortgage rate as a percentage (ex 5.5% would be entered as 5.5 into the function)
3)	Amortization period- The number of years the mortgage is being amortized over

Key Assumptions:
•	The function is only valid for calculating fixed rate mortgage payments, the function is not made to handle variable rate mortgage structures
•	By the end of the amortization period the principal balance on the mortgage will be equal to 0
•	User inputs must follow the specified formats outlined in the inputs section. User inputs are not validated to check for errors or erroneous inputs.

Using the 3 inputs, the function will return to users the different options they have, and the payment amounts for different mortgage payment structures. Note that all the widely available mortgage options are quoted as outputs for the function

The different payment options include the following payment schedules:

•	Monthly 
•	Semi-Monthly 
•	Biweekly
•	Weekly
•	Accelerated Biweekly
•	Accelerated Weekly


# i257-symtrackdb
Final project repo for i257 DBM course - Lyme Symptom Tracking


## List of SQL queries to be designed

No. | App Screen | Name | Definition | Input/Cal/Output
----|------------|------|------------|-----------------
1 | Progress | Average symptom score [this period] | Sum of severity score of all symptoms being tracked, averaged for current period. | INPUT: User ID, Start date, End date <br>CALC: Average of sum of all symptom values for current period <br>OUT: Single number
2 | Progress | Average symptom category score [this period] | Break-up of the above by symptom category | INPUT: User ID, Start date, End date <br>CALC: Average sum of the above for each symptom category <br>OUT: Dictionary with category names and corresponding numbers
3 | Progress | Average symptom severity for each symptom - this week and previous period | Average of symptom severity for each symptom separately, for both current week and previous week | INPUT: User ID, Start date, End date <br>CALC: Average symptom severity for each symptom, for current and previous period <br>OUT: Dictionary with symptom name, this period's avg. and previous period's avg.
4 | Progress | Day-wise symptom severity for [this and previous period] | Individual severity values of a symptom over current and past period | INPUT: User ID, Start date, End date <br>CALC: Average symptom severity for each symptom, for current and previous period <br>OUT: Dictionary with symptom name and corresponding array of values for the date range
5 | Progress | Total symptom score date-wise for [date range] | Sum of severity score of all symptoms for each day in the date range | INPUT: User ID, Start date, End date <br>CALC: Average symptom severity for each symptom, for each date in the range <br>OUT: Array of total sypmptom scores for each date in range

[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/hiWoDjT-)
# HW4
HW 4
(Due 2/17)
Part 1 (50 points): Normalization and Standardization 
Take the iris data set and create two new .csv data sets (25 points each). One that normalizes all columns to have values between 0 and 1 and a second that standardizes all columns to have a mean of 0 and standard deviation of 1.
Push both files to github. 

Part 2 (50 points): ER Diagram 
Create an ER diagram that models a zoo:
Define at least three entities that have several attributes for each entity, their relationship between entities, and their constraints. Argue your decisions. You will graded based on your explanation on why you chose certain constraints. 
What to submit 
Either create a markdown readme file that has a copy of your ER diagram and explanation or .pdf version and push that to github.
Please also submit a link to your github submission to Canvas as well. This helps the TA grade faster. 

# Zoo ERD with Explanation
The following ERD illustrates a database concerned with the feeding schedules of the animals, as well as the support staff responsible for feeding the animals in the different regions of the zoo. I imagined that we might want to keep track of where an animal is in the zoo, so we'd need a zoo 'region' as well as a container of some sort within the region. The containers might contain one or more animals, and the container might allow one or more species. The diet of each animal might consist of a single feeding once a day, or several feedings throughout the day or night. The Feed_Schedule table allows as many rows as needed per animal per day. What the animal eats might vary by time of day, so we might create a row in Diet for breakfast for a monkey, another for lunch, and a third for dinner. Then, each of those Diet rows are associated with a row in Feed_Schedule for a given time on a specific date. We can re-use the Diet entries as many times as needed within Feed_Schedule. I wasn't exactly sure what we might want to store in terms of the Diet entries. If a zoo buys ingredients in bulk that different animals can share, perhaps they can mix and match them to get the correct macro profile for each animal? I'm not sure, so that design would depend upon the types of food and food preparation operations the zoo conducts. If I were really building this system, I would collect those requirements before creating the database design, of course. I think the remaining tables are pretty self-explanatory. 

![Zoo ERD](Zoo ERD.svg?raw=false "Zoo ERD")

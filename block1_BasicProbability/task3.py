# 3. If a bag contains 3 red balls and 2 green balls, what is the probability of picking a red ball?

# To calculate the probability of picking a red ball from the bag, you need to divide the number of 
# favorable outcomes (picking a red ball) by the total number of possible outcomes.

# In this case, the bag contains 3 red balls and 2 green balls, so there are a total of 5 balls.

# The probability (P) can be calculated using the formula:

#           P(Red)= Number of Favorable Outcomes/ Total Number of Possible Outcomes

# Substituting the values:
#           P(Red)= 5 / 3

# So, the probability of picking a red ball from the bag is  5 / 3 or 0.6 (60%).

#           **************************python code***************************

# Define the number of red balls
red_balls = 3
# Define the total number of balls in the bag
total_balls = 5  # (3 red + 2 green)
# Calculate the probability of picking a red ball
probability_red = red_balls / total_balls
print("The probability of picking a red ball is:", probability_red)

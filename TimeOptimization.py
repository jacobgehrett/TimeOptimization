# by Jacob Gehrett
#
# This linear program solver helps me make the most of my typical Saturday. As is the case with any subjective work,
# the specifics would greatly vary by person. However, I believe the principles can apply to anyone, with constraints
# adjusted to fit their specific lifestyles.
#
# This solver is built with the PuLP Python package published by MIT.

from pulp import LpVariable, LpProblem, LpStatus, value, LpMaximize

# Below are decision variable declarations (my ideal summer Saturday activities)
x = LpVariable("sleep", 0, None)
y = LpVariable("shower", 0, None)
z = LpVariable("change", 0, None)
w = LpVariable("breakfast", 0, None)
a = LpVariable("lunch", 0, None)
b = LpVariable("dinner", 0, None)
c = LpVariable("climbing", 0, None)
d = LpVariable("movie", 0, None)
e = LpVariable("videoGames", 0, None)
f = LpVariable("cardGames", 0, None)
g = LpVariable("dog", 0, None)
h = LpVariable("tv", 0, None)
i = LpVariable("cuddle", 0, None)
j = LpVariable("golfing", 0, None)
k = LpVariable("driving", 0, None)
m = LpVariable("joyriding", 0, None)
n = LpVariable("restaurant", 0, None)
o = LpVariable("hammock", 0, None)
p = LpVariable("Frisbee", 0, None)
q = LpVariable("park", 0, None)
r = LpVariable("friends", 0, None)
s = LpVariable("swimming", 0, None)
t = LpVariable("nothing", 0, None)
u = LpVariable("date", 0, None)
v = LpVariable("reading", 0, None)

# The objective function seeks to maximize utility. This is the set of decision variables multiplied by some
# arbitrary number that I assign, roughly proportional to how much happiness or personal satisfaction that activity
# gives me.
prob = LpProblem("utility", LpMaximize)
prob += 1*x - 1*y + 10*c + 7*d + 8*e + 6*f + 6*h + 1*i + 3*j - 2*k + 3*m + 7*n + 4*o + 4*p + 2*q + 9*r + 5*s + 1*t +\
        4*u + 4*v


# The set of constraints follows:

prob += x + y + z + w + a + b + c + d + e + f + g + h + i + j + k + m + o + p + s + t + u + v <= 24
# 24 hrs in day

prob += x >= 4.5
# Need more than 4.5 hrs sleep

prob += x <= 7.5
# No more than 7.5 hrs sleep

prob += z >= 0.5
# More than 0.5 hrs to get ready

prob += w >= 0.5
# More than 0.5 hrs for breakfast

prob += a >= 0.5
# More than 0.5 hrs for lunch

prob += b >= 0.5
# More than 0.5 hrs for dinner

prob += c <= 5
# No more than 5 hrs climbing

prob += c + y >= c + 0.5
# If climbing, need a shower after

prob += c + z >= c + 1
# If climbing, days total time getting ready is at least 1 hr instead of 0.5

prob += c + x >= c + 6
# If climbing, need at least 6 hrs of sleep

prob += c + k >= c + 0.67
# If climbing, need to alot 0.67 hours driving

prob += d <= 3
# No more than 3 hrs watching movies

prob += e <= 4
# No more than 4 hrs playing video games

prob += f <= 3
# No more than 3 hrs playing card games

prob += g >= 0.25
# No less than 0.25 hrs walking dog

prob += h <= 2
# No more than 2 hrs watching tv

prob += i >= 0.5
# No less than 0.5 hrs cuddling (wife would kill me)

prob += n <= 1
# No more than 1 hr at restaurant

prob += q <= o + p + g
# Total time in park must be less than hammock, Frisbee, and dog-walking time combined

prob += r <= 12
# Time with friends should not exceed 12 hrs

prob += s <= 3
# No more than 3 hrs swimming

prob += u <= 4
# No more than 4 hrs on date

prob += v <= 3
# No more than 3 hrs reading

prob += d + e + h <= 4
# All screen time should be less than 4 hrs

prob += r <= w + a + b + c + d + e + f + k + p + s + t
# Only certain activities can be done with friends

prob += o <= 1
# No more than 1 hr in hammock

prob += p <= 1
# No more than 1 hr playing Frisbee

prob += n + k >= n + 0.33
# Going to a restaurant takes at least 0.33 hrs of driving

prob += n + k + c >= n + c + 1
# Climbing and going to a restaurant in the same day takes at least 1 hr of driving

status = prob.solve()
print(LpStatus[status])

print(str(value(x)) + " hrs sleep")
print(str(value(y)) + " hrs shower")
print(str(value(z)) + " hrs changing")
print(str(value(w)) + " hrs eating breakfast")
print(str(value(a)) + " hrs eating lunch")
print(str(value(b)) + " hrs eating dinner")
print(str(value(c)) + " hrs climbing")
print(str(value(d)) + " hrs watching movies")
print(str(value(e)) + " hrs playing video games")
print(str(value(f)) + " hrs playing card games")
print(str(value(g)) + " hrs walking dog")
print(str(value(h)) + " hrs watching tv")
print(str(value(i)) + " hrs cuddling")
print(str(value(j)) + " hrs golfing")
print(str(value(k)) + " hrs driving")
print(str(value(m)) + " hrs joyriding")
print(str(value(n)) + " hrs at restaurant")
print(str(value(o)) + " hrs in hammock")
print(str(value(p)) + " hrs playing Frisbee")
print(str(value(q)) + " hrs at the park")
print(str(value(r)) + " hrs with friends")
print(str(value(s)) + " hrs swimming")
print(str(value(t)) + " hrs doing nothing")
print(str(value(u)) + " hrs on a date")
print(str(value(v)) + " hrs reading")

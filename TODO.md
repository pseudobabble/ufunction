# README:

## Goals:
- Goals are state definitions - they use *Stative verbs*: Be, have, understand. Goals satisfy X-condition by Y date.
- https://en.wikipedia.org/wiki/Stative_verb
- Actions are performed to transition from current state to goal state - they are *Dynamic verbs*

## Actions
- Actions are performed every day until the desired metric is reached.
- https://en.wikipedia.org/wiki/Dynamic_verb
- Actions contain Intentions and Measurements.

## Intentions:
- Intentions are daily commitments to carry out the action, with metrics to track progress.

#  Measurements:
- Measurements record the outcome of your Intentions. Each is associated with an Action, and a Measurement.

### Examples:
If you wanted to maintain your level of something, you would set an Action with the verb 'maintain'.
 
If you wanted to reach a state, and then maintain it, you would first create an Action with the verb 'increase',
then once the target metric on that is reached, create a 'maintain' action, and continue.

#### Form for thinking about actions:
- Action Verb + Metric Name + Target (+ Unit) 
- Reduce + Calorie intake + to 2000kcal
- Increase + Squat weight + to 70kg/Squat
- Maintain + Meditation time + at 40mins
- Reduce + Expenditures + to £50,000
- Increase + Savings + to £50,000
- Maintain + Net Worth + at £50,000


# SERVER:
##################################
#### REWRITE FOR PYTHON 3!!! #####
##################################
Add ordering to all models



- Create a title dynamic property on Action
- Create services to create chart data, plus required API infrastructure
- Create Progress against goal
- Add Goal id, action id, measurement id
- Add Pagination
- Create Filter


#CLIENT:
- Customise each list to show what you want
- titles on each list
- Create create buttons for actions, reviews, rewards on goaledit
- Create Charts for Intention Alignment and Progress vs Goal
- Customise forms
- Fields showing parent ids should be ReferenceFields enclosing TextFields
- Create Dashboard with chart allowing selection of goal, then shows Progress, and intention alignment
- make charts resizeable with https://github.com/STRML/react-grid-layout
